import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

st.title("📊 Uji Kelayakan Air")
st.markdown("Masukkan data parameter air di bawah ini untuk mendapatkan hasil analisis.")

# --- PATH CHECKER (Untuk Debugging) ---
# Memastikan file model terbaca dari folder root
model_path = 'water_quality_rf_model_advanced.pkl'
scaler_path = 'scaler_advanced.pkl'

@st.cache_resource
def load_assets():
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except FileNotFoundError:
        return None, None

model, scaler = load_assets()

if model is None:
    st.error(f"⚠️ File model tidak ditemukan! Pastikan '{model_path}' dan '{scaler_path}' ada di folder utama project (bukan di dalam folder pages).")
    st.stop()

# --- FORM INPUT ---
with st.form("prediction_form"):
    st.subheader("Parameter Fisika & Kimia")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ph = st.number_input("pH (Derajat Keasaman)", 0.0, 14.0, 7.0, help="Normal: 6.5 - 8.5")
        hardness = st.number_input("Hardness (mg/L)", 0.0, 500.0, 200.0)
        solids = st.number_input("Solids/TDS (ppm)", 0.0, 60000.0, 20000.0)
    
    with col2:
        chloramines = st.number_input("Chloramines (ppm)", 0.0, 15.0, 7.0)
        sulfate = st.number_input("Sulfate (mg/L)", 0.0, 500.0, 330.0)
        conductivity = st.number_input("Conductivity (μS/cm)", 0.0, 800.0, 400.0)
        
    with col3:
        organic_carbon = st.number_input("Organic Carbon (ppm)", 0.0, 30.0, 14.0)
        trihalomethanes = st.number_input("Trihalomethanes (µg/L)", 0.0, 130.0, 66.0)
        turbidity = st.number_input("Turbidity (NTU)", 0.0, 10.0, 4.0)
        
    submit_btn = st.form_submit_button("🔍 Analisis Sekarang", use_container_width=True)

# --- LOGIKA PREDIKSI ---
if submit_btn:
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]],
                              columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    
    try:
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        proba = model.predict_proba(input_scaled)
        
        st.markdown("---")
        result_col1, result_col2 = st.columns([1, 2])
        
        with result_col1:
            if prediction[0] == 1:
                st.success("### ✅ LAYAK MINUM")
                st.write("Air memenuhi standar potabilitas.")
            else:
                st.error("### ❌ TIDAK LAYAK")
                st.write("Air berbahaya untuk dikonsumsi.")
        
        with result_col2:
            st.metric("Tingkat Keyakinan AI", f"{proba[0][int(prediction[0])]*100:.1f}%")
            if prediction[0] == 0:
                st.warning("Rekomendasi: Lakukan penyaringan ulang atau rebus air hingga mendidih.")
            else:
                st.info("Rekomendasi: Air aman digunakan.")
                
    except Exception as e:
        st.error(f"Error: {e}")