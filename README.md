# 💳 Credit Card Fraud Detection System

## 🚀 Project Overview

This project implements a **robust Credit Card Fraud Detection System** designed to identify and flag fraudulent transactions using machine learning.

Built as a **web-based application** with a Streamlit frontend and a Python backend, it empowers financial analysts and security teams with real-time insights into suspicious activities. The system learns from transaction patterns and distinguishes between legitimate and fraudulent behavior—even with imbalanced data.

---

## 🎯 Key Features

- 🔐 **User Authentication**: Secure login for users and admin authentication for managing models and users.
- 📂 **Dataset Upload**: Upload CSV files containing credit card transaction data for analysis.
- ⚠️ **Fraud Prediction**: Classifies transactions as fraudulent or legitimate using a pre-trained Logistic Regression model.
- 📊 **Prediction Output & Evaluation**: Displays predictions with:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix (visualized)
- ⏱ **Real-Time Feedback**: Immediate display of results, including:
  - Suspicious transactions
  - Total transactions
  - Fraud count
  - Model confidence
- 🔧 **Model Management** *(Admin-only)*: Upload and manage ML models and scalers with version tracking.
- 🛠 **Settings & Customization**: Toggle light/dark mode and notification preferences.
- 📉 **Data Preprocessing**: Feature scaling and preparation for model training.
- ⚖️ **Imbalanced Data Handling**: Undersampling techniques via imblearn to tackle class imbalance.

---
## 📸 Screenshots
### 🔐 Login Page
Secure login page for user and admin authentication.
![image alt](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/ef1bb7276e804183c87e9ca668568de109f31de2/Screenshot%202025-07-06%20194110.png)
### ⚠️ Legitimate Detection Results
Visual feedback highlighting legitimate transactions.
![image alt](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194215.png)
### ⚠️ Fraud Detection Results
Visual feedback highlighting fraudulent transactions.
![image alt](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194245.png)
### 🧮 Confusion Matrix
![image alt](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194309.png)
## 🏗 System Architecture

The application follows a lightweight **client-server architecture**, blending a minimal UI with powerful backend logic.

- **Frontend**: Built using **Streamlit**, offering an interactive, clean, and responsive UI.
- **Backend**: Powered by **Python**, it:
  - Handles uploaded data
  - Loads and runs the Logistic Regression model
  - Displays prediction results
- **Machine Learning Module**: Trained with **scikit-learn** on labeled data to predict fraud probability.

---

## 🧰 Tech Stack

| Category              | Technologies Used                               |
|-----------------------|--------------------------------------------------|
| Programming Language  | Python                                           |
| Web Framework         | Streamlit                                       |
| Data Manipulation     | pandas, numpy                                   |
| Machine Learning      | scikit-learn, imbalanced-learn (imblearn)     |
| Visualization         | matplotlib, seaborn                             |
| Version Control       | Git, GitHub                                     |
| Env Management        | pip                                             |

---

## ▶️ Getting Started

To launch the application locally:

bash
streamlit run app.py
