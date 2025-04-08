# ☁️ Cloud Intrusion Detection System (CIDS)

This project is a Cloud-based Intrusion Detection System that uses a **Stacked Contractive Auto-Encoder (SCAE)** for feature extraction and a **Support Vector Machine (SVM)** for classification of malicious traffic. The system is deployed on AWS and integrates cloud-native services for real-time detection and alerting.

---

## 🔍 Overview

The Cloud Intrusion Detection System (CIDS) leverages a hybrid of deep learning and classical machine learning techniques to detect anomalies in network traffic.

### 🚦 How It Works

1. **Data Collection** – Captures traffic using SDN-enabled infrastructure.
2. **Data Preprocessing** – Normalizes and transforms traffic into feature vectors.
3. **Feature Extraction** – Applies SCAE to extract important features.
4. **Classification** – SVM classifies traffic as normal or malicious.
5. **Alerting & Logging** – Intrusions are logged and alerted using AWS CloudWatch.

---

## ☁️ Deployment on AWS

The following AWS services are used to deploy the IDS:

- **EC2** – Hosts the machine learning models and Flask API.
- **S3** – Stores pre-trained models for scalability.
- **Lambda** – Handles real-time processing of network logs.
- **CloudWatch** – Monitors intrusion events and sends alerts.

---

## 💻 Sample API Call

The system provides a simple REST API endpoint for intrusion detection.

```bash
curl -X POST "http://your-api-endpoint/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [0.1, 0.2, 0.3, ..., 1.0]}'
```

---
## 📁 Project Structure

```
.
├── arff dataset.csv               # dataset
├── ids_project/
│   ├── app.py                     # Flask API for prediction
│   ├── encoder_model.h5           # Trained encoder model (SCAE)
│   ├── scae_model.keras           # Full SCAE model
│   ├── svm_model.pkl              # Trained SVM classifier
│   ├── templates/
│   │   └── index.html             # Web interface for testing predictions
```

---

## 🚀 Future Enhancements

- Improve feature engineering pipeline with auto-feature selection
- Integrate with **AWS GuardDuty** for threat intelligence
- **Lambda** – Handle network log processing in real-time
- **CloudWatch** – Enhance alerting with metrics and alarms
- Add Docker support and CI/CD pipeline for deployment

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📫 Contact

For any inquiries or suggestions, feel free to open an issue or contact the repository owner.
```

---

### ✅ `requirements.txt`

```txt
Flask==2.2.5
numpy==1.24.4
pandas==2.1.4
scikit-learn==1.3.2
tensorflow==2.15.0
joblib==1.3.2
```

---

Let me know if you also want a `Dockerfile`, `run.sh`, or deployment script for AWS EC2 or Lambda setup!
