
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('creditcard.csv')

# Separate legitimate and fraudulent transactions
legitimate = data[data.Class == 0]
fraud = data[data.Class == 1]

# Undersample legitimate transactions to balance the classes
legitimate_sample = legitimate.sample(n=len(fraud), random_state=2)
data = pd.concat([legitimate_sample, fraud], axis=0)

# Split data into training and testing sets
X = data.drop(columns="Class", axis=1)
y = data["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)  # added max_iter
model.fit(X_train, y_train)

# Evaluate model performance
train_acc = accuracy_score(model.predict(X_train), y_train)
test_acc = accuracy_score(model.predict(X_test), y_test)

# Function to verify login credentials (replace with your actual login logic)
def verify_credentials(username, password):
    # This is a placeholder - replace with your actual user authentication
    if username == "user" and password == "pass":
        return True
    else:
        return False

# Streamlit app with login feature
st.title("Credit Card Fraud Detection Model")

# Login Section
username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
    if verify_credentials(username, password):
        st.session_state.logged_in = True  # Set session state variable
    else:
        st.error("Incorrect username or password")

if "logged_in" in st.session_state and st.session_state.logged_in:

    st.write("Enter all required features values")
    input_df = st.text_input("Features (comma-separated)")
    input_df_splited = input_df.split(',')

    submit = st.button("Submit")

    if submit:
        try:
            features = np.asarray(input_df_splited, dtype=np.float64)
            prediction = model.predict(features.reshape(1, -1))

            if prediction[0] == 0:
                st.write("Legitimate transaction")
            else:
                st.write("fraud")
        except ValueError:
            st.error("Invalid input. Please enter numeric values.")

    # --- Confusion Matrix ---
    st.subheader("Confusion Matrix")
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicted Labels')
    ax.set_ylabel('True Labels')
    ax.set_title('Confusion Matrix')
    st.pyplot(fig)

    # --- Accuracy Metrics ---
    st.subheader("Accuracy Metrics")
    st.write(f"Training Accuracy: {train_acc:.4f}")
    st.write(f"Testing Accuracy: {test_acc:.4f}")

else:
    st.write("Please log in to use the application.")