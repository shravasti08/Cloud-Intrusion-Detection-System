from flask import Flask, render_template, request
import tensorflow as tf
import joblib
import numpy as np
from tensorflow.keras.utils import register_keras_serializable
from tensorflow.keras.losses import Loss

@register_keras_serializable()
class ContractiveLoss(Loss):
    def __init__(self, autoencoder=None, lam=1e-4, reduction=tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE, name="contractive_loss"):
        super().__init__(reduction=reduction, name=name)
        self.autoencoder = autoencoder
        self.lam = lam

    def call(self, y_true, y_pred):
        encoder_layer = self.autoencoder.get_layer(index=1)
        W = encoder_layer.weights[0]
        W = tf.transpose(W)

        h = encoder_layer(y_pred)
        dh = tf.cast(h > 0, tf.float32)

        contractive_penalty = self.lam * tf.reduce_sum(dh ** 2 * tf.reduce_sum(W ** 2, axis=1))
        return tf.reduce_mean(tf.square(y_true - y_pred)) + contractive_penalty

# Load models
scae_model = tf.keras.models.load_model("scae_model.keras", custom_objects={"ContractiveLoss": ContractiveLoss()})
encoder_model = tf.keras.models.load_model("encoder_model.h5")
svm_model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            features = [
                float(request.form.get("protocol_type")),
                float(request.form.get("service")),
                float(request.form.get("flag")),
                float(request.form.get("logged_in")),
                float(request.form.get("count")),
                float(request.form.get("same_srv_rate")),
                float(request.form.get("diff_srv_rate")),
                float(request.form.get("dst_host_srv_count")),
                float(request.form.get("dst_host_same_srv_rate")),
                float(request.form.get("dst_host_same_src_port_rate"))
            ]
            input_data = np.array([features])
            encoded = encoder_model.predict(input_data)
            prediction = svm_model.predict(encoded)
            result = "🚨 Intrusion Detected!" if prediction[0] else "✅ Normal Traffic"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
