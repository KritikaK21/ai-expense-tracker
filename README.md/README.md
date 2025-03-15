# 💰 AI-Powered Expense Tracker with Alexa & Firebase 🚀

Welcome to **AI Expense Tracker**, a smart system that lets you **track, categorize, and analyze your expenses** using **Alexa, AI, Firebase, and AWS**! 🎙️💡📊

---

## 📌 Features

- ✅ **Voice-enabled Expense Tracking** (via Alexa)
- ✅ **Automatic Categorization of Expenses using AI/ML**
- ✅ **Secure Cloud Data Storage using Firebase**
- ✅ **Future Ready for AWS Lambda, SageMaker, SNS, and DynamoDB Integration**
- ✅ **Expense Summary & Analytics Ready for Visualization**

---

## ⚙️ Tech Stack

| Feature                                | Tech Used                            |
|---------------------------------------|-------------------------------------|
| Voice Interaction                      | **Amazon Alexa** (Custom Skill)     |
| Expense Storage                        | **Firebase Realtime Database**      |
| AI-based Categorization                | **Python + Scikit-learn (ML Model)** |
| Lambda Function (Serverless Backend)   | **AWS Lambda (Python Runtime)**     |
| (Optional/Extendable) AI Model Hosting | **AWS SageMaker**                   |

---

## 🚀 How It Works

1. **User talks to Alexa** 📢  
   ➤ Example: _"I spent 500 on groceries"_  

2. **Alexa Skill triggers Lambda**  
   ➤ Lambda handles backend and AI logic.  

3. **Expense is stored securely in Firebase** 🔒  

4. **AI Model auto-categorizes expense**  
   ➤ Example: "groceries" recognized as "Food" 🍕  

5. **Analytics ready for future dashboards!** 📊  

---

## 🧠 AI/ML Model
- Built using **Scikit-learn**.
- Trained on real-life expense patterns.
- Models and vectorizers are stored securely (excluded from repo for safety).
- Example categories: `Food`, `Medical`, `Shopping`, `Bills`, `Entertainment`, `Transport`, etc.

---

## 🔐 Security & Privacy
- 🚫 **Secrets & Credentials** are **excluded** via `.gitignore`.
- Firebase & AI models are **used locally or securely stored in cloud**.

---

## 📊 Future Scope & Integrations
- 🌩️ **AWS Lambda + DynamoDB for storage**
- 🧠 **AWS SageMaker for AI Model Hosting**
- 🔔 **AWS SNS for notifications on budget limits**
- 📈 **Amplify/QuickSight Dashboards** for analytics
- ✅ **Full Serverless Expense Tracking System**

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/KritikaK21/ai-expense-tracker.git
## 🚀 How to Setup & Run Locally

### 1. **Clone the Repository**
```bash
git clone https://github.com/KritikaK21/ai-expense-tracker.git
```

---

### 2. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

---

### 3. **Add the following files locally** (⚠️ Not pushed to GitHub for security reasons):
- `serviceAccountKey.json` (Firebase Admin SDK)
- `firebase-config.json` (Firebase App Config)

### AI Models (required):
- `expense_vectorizer.pkl`
- `expense_categorizer_model.pkl`

---

### 4. **Run Expense Tracker App Locally**
```bash
python app.py
```

---

## 🏆 Achievements & Learning

- ✅ Hands-on with **Alexa Skill Development**
- ✅ Built and trained **AI/ML Models** for text classification
- ✅ Used **Firebase as Realtime DB**
- ✅ Learned **AWS Lambda integrations**

---

> ⭐ **Don't forget to give this repo a star if you like it!** ⭐






