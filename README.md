# drug-toxicity-predictor
Explainable AI model to predict drug toxicity using molecular descriptors

Drug Toxicity Prediction using Machine Learning

📌 Overview
Drug toxicity is a major reason for failure in drug development. Early prediction of toxic compounds can reduce cost and improve patient safety.
This project builds a machine learning model to predict drug toxicity using molecular descriptors derived from chemical structures.

🎯 Objective
Predict toxicity of compounds from SMILES representation
Analyze key molecular features contributing to toxicity
Build an interactive tool for real-time prediction

⚙️ Workflow
SMILES → RDKit → Molecular Descriptors → ML Model → Prediction

📊 Dataset
Tox21 Dataset
~12,000 chemical compounds
Multiple toxicity endpoints

This project focuses on:
👉 SR-HSE (Stress Response Pathway)

🧠 Features Used
Molecular Weight (MolWt)
LogP (lipophilicity)
Number of H-bond donors
Number of H-bond acceptors

🤖 Models Used
Logistic Regression 
Random Forest

🔍 Key Insight

Logistic Regression outperformed Random Forest, indicating a largely linear relationship between molecular descriptors and toxicity.
Class imbalance significantly affected model performance and was handled using class_weight="balanced"

📈 Results
Model Performance
Feature Importance

🌐 Web Application
Users can input SMILES strings to predict toxicity.
example app output:
Output: toxic
Output: non-toxic

🚀 How to Run
pip install -r requirements.txt
streamlit run app.py

🔍 Example

Input:
CCO
Output:
Non-Toxic
