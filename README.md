# Credit-Card-Fraud-Detection

Project Overview

This project implements a robust Credit Card Fraud Detection System designed to identify and flag fraudulent transactions using machine learning. Developed as a web-based application with a Streamlit frontend and a Python backend, it provides financial analysts and security teams with real-time insights into potentially suspicious activity. The system analyzes transaction patterns and behaviors to distinguish between legitimate and illicit activities, aiming to minimize financial losses and enhance security.

The primary goal is to build an intelligent, accessible, and user-friendly system that can learn from historical transaction patterns and accurately predict the likelihood of fraud, even with imbalanced datasets.

Features:

User Authentication: Secure login functionality for registered users and administrative authentication for managing models and users.

Dataset Upload: Users can securely upload credit card transaction data in CSV format for analysis.

Fraud Prediction: Utilizes a pre-trained Logistic Regression model to classify transactions as 'fraudulent' or 'legitimate' in real-time.

Prediction Output & Evaluation Display: Clearly presents transaction predictions, highlights suspicious transactions, and shows key evaluation metrics (Accuracy, Precision, Recall, F1-Score) along with a Confusion Matrix visualization.

Real-Time Feedback: Provides immediate highlighting of suspicious transactions and a dashboard summary (total transactions, fraud count, model confidence).

Model Management: (Admin-only) Allows administrators to upload and manage updated ML models and scalers with version tracking.

Settings & Customization: Users can adjust preferences like light/dark mode and notification settings.

Data Preprocessing: Handles feature scaling and prepares raw transaction data for model training.

Imbalanced Data Handling: Employs techniques (e.g., undersampling) to address the class imbalance inherent in fraud detection datasets.


System Architecture
The Credit Card Fraud Detection System follows a simple yet effective client-server architecture, combining a minimal frontend with a robust backend that handles all machine learning logic.

Frontend (Streamlit): Provides a clean, responsive interface for uploading data, displaying results, and user interaction.

Backend (Python with scikit-learn): Processes uploaded data, loads the trained Logistic Regression model, performs classification, and handles core logic.

Machine Learning Module: Built using scikit-learn and trained on labeled transaction data, specifically using a Logistic Regression model for fraud probability prediction.

Technologies Used:

Programming Language: Python

Web Framework: Streamlit
Data Manipulation: pandas, numpy
Machine Learning: scikit-learn, imblearn (for imbalanced data)
Data Visualization: matplotlib, seaborn
Version Control: Git, GitHub
Environment Management: pip


Start the Streamlit application:

streamlit run app.py

Access the application:
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).


Feel free to star this repository if you found it helpful!
