import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd
import pickle

# Load your trained model (save it first if not done)
model = pickle.load(open("model.pkl", "rb"))

def predict_toxicity(smiles):
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is None:
        return "Invalid SMILES"
    
    features = {
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "NumHDonors": Descriptors.NumHDonors(mol),
        "NumHAcceptors": Descriptors.NumHAcceptors(mol)
    }
    
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)[0]
    
    return "Toxic" if prediction == 1 else "Non-Toxic"

st.title("Drug Toxicity Predictor")

smiles = st.text_input("Enter SMILES:")

if smiles:
    result = predict_toxicity(smiles)
    st.write("Prediction:", result)