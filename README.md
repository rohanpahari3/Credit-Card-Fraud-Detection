#  Smart Credit Card Fraud Detection

A machine learning-powered tool to intelligently detect suspicious credit card transactions in real time — designed for analysts, security teams, and anyone dealing with high-volume transaction data.

---

##  What It Does

This application helps you identify fraudulent transactions **as they happen**, even when dealing with highly imbalanced data (where fraud is rare but costly). Using a trained logistic regression model behind a simple UI, users can upload transaction files, get immediate predictions, and visually assess model performance — all from their browser.

---

##  How It Works

Instead of a bulky dashboard or enterprise software, this is a **Streamlit-based interface** backed by a **Python-powered ML engine**. It scans uploaded CSV files, preprocesses the data (like scaling features), and instantly classifies transactions as either **legitimate** or **fraudulent**.

Admins get extra control — they can upload newer models, manage users, and even configure detection settings.

---

##  Application Modules

Here’s a breakdown of what’s included:

###  Authentication
- Users can securely log in
- Admins have extended privileges (model & user management)

###  Upload Interface
- Simple CSV uploader for credit card transaction data

###  Prediction Engine
- Powered by a pre-trained **Logistic Regression model**
- Real-time prediction of each transaction
- Confidence score and probability-based feedback

###  Metrics + Evaluation
- Evaluation scores: **Accuracy**, **Precision**, **Recall**, **F1-score**
- Confusion Matrix visualization
- Summary of fraud stats (e.g., how many flagged out of total)

###  Admin Controls
- Upload/manage ML models and scalers
- Track model versions

###  Customization
- Light/dark mode toggle
- Control notification behavior

---

##  Visual Walkthrough

> A quick peek into the system in action:

### 1. Login Page  
Secure authentication for users and admins  
![Login](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/ef1bb7276e804183c87e9ca668568de109f31de2/Screenshot%202025-07-06%20194110.png)

---

### 2. Legitimate Transactions Output  
Visual indicator showing clean, non-fraud transactions  
![Legit](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194215.png)

---

### 3. Fraudulent Transactions Output  
Clearly highlights red-flagged activity  
![Fraud](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194245.png)

---

### 4. Confusion Matrix  
Model performance at a glance  
![Matrix](https://github.com/rohanpahari3/Credit-Card-Fraud-Detection/blob/a29997a3592e5d1d5766eedc745b8bc2be1fe01c/Screenshot%202025-07-06%20194309.png)

---

##  Under the Hood

The system follows a clean **client-server architecture**:

- **Frontend**: Built with Streamlit for fast prototyping and sleek UI
- **Backend**: Python handles all logic, including:
  - Model loading
  - Data preprocessing
  - Prediction & metrics
- **ML Engine**: Trained with `scikit-learn`, tuned to handle imbalanced classes using `imblearn`

---

##  Tech Behind It

| Part                 | Tools Used                                    |
|----------------------|-----------------------------------------------|
| Programming          | Python                                        |
| ML & Preprocessing   | scikit-learn, imbalanced-learn, pandas, numpy |
| UI                   | Streamlit                                     |
| Visualization        | matplotlib, seaborn                          |
| Version Control      | Git + GitHub                                  |
| Package Management   | pip                                           |

---

## 🚦 How to Launch

Get started in one command:

```bash
streamlit run app.py
