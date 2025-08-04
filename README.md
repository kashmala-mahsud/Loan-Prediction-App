# 🏦 Loan Prediction App

A machine learning web application built with **Streamlit** that predicts whether a loan will be approved based on user-input details such as income, loan amount, credit history, and property area.

## 🚀 Features

- Real-time prediction of loan approval status (✅ Approved / ❌ Rejected)
- User-friendly interface with form inputs
- Trained with Support Vector Machine (SVM)
- Clean UI built using Streamlit

## 📁 Project Structure

```
Loan-Prediction-App/
├── app.py               # Streamlit frontend
├── model.pkl            # Trained SVM model
├── scaler.pkl           # Scaler for feature normalization
├── columns.pkl          # Feature columns used during training
├── requirements.txt     # Dependencies
└── README.md
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kashmala-mahsud/Loan-Prediction-App.git
cd Loan-Prediction-App
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
# source .venv/bin/activate   # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🧠 Model Inputs

The prediction model uses the following features:

- Gender
- Marital Status
- Dependents
- Applicant Income
- Loan Amount
- Credit History
- Property Area

## ❗ When Can Loans Be Rejected?

- Low applicant income compared to loan amount
- Poor or missing credit history (0)
- Risky property areas (like rural with poor credit)
- Unfavorable combinations of categorical features

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ by [Kashmala Mahsud]
