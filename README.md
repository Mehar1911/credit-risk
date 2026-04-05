# 💳 ML-Powered Credit Risk Assessment Tool

A machine learning web application that predicts the creditworthiness of loan applicants in real time. Built with an **Extra Trees Classifier** trained on the German Credit Dataset, the app evaluates applicants across key financial and demographic features and classifies them as **Good** or **Bad** credit risks.

---

## 🚀 Demo

> Run locally with `streamlit run app2.py`

---

## 📌 Features

- Real-time credit risk classification (Good / Bad)
- Interactive input form covering applicant financial profile
- Pre-trained Extra Trees model serialized with joblib for lightweight deployment
- Clean, user-friendly Streamlit interface — no technical knowledge required

---

## 🧠 Model

| Detail | Info |
|---|---|
| Algorithm | Extra Trees Classifier |
| Dataset | German Credit Dataset (1,000 applicants) |
| Target | Binary — Good (1) / Bad (0) credit risk |
| Input Features | Age, Sex, Job, Housing, Saving Accounts, Checking Account, Credit Amount, Duration |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend / UI |
| scikit-learn | Model training & evaluation |
| pandas & NumPy | Data processing |
| joblib | Model serialization |

---

## 📁 Project Structure

```
credit-risk/
│
├── app.py                        # Streamlit app
├── extra_trees_credit_model.pkl  # Trained model
├── analysis_model.ipynb          # Training & EDA notebook
├── Sex_encoder.pkl               # Label encoders (legacy)
├── Housing_encoder.pkl
├── Saving accounts_encoder.pkl
├── Checking account_encoder.pkl
└── README.md
```

---

## ⚙️ Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/your-username/credit-risk-assessment.git
cd credit-risk-assessment
```

**2. Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install streamlit scikit-learn pandas numpy joblib
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Input Features

| Feature | Type | Description |
|---|---|---|
| Age | Numeric | Applicant age (18–80) |
| Sex | Categorical | male / female |
| Job | Numeric | Job category (0–3) |
| Housing | Categorical | own / rent / free |
| Saving Accounts | Categorical | little / moderate / rich / quite rich |
| Checking Account | Categorical | little / moderate / rich / quite rich |
| Credit Amount | Numeric | Loan amount requested |
| Duration | Numeric | Loan duration in months |

---

## 📂 Dataset

[German Credit Dataset](https://www.kaggle.com/datasets/uciml/german-credit) — 1,000 loan applicants with 10 features and a binary credit risk label, widely used as a benchmark in credit scoring research.

---
