import streamlit as st

# Konfigurasi Halaman (Wajib di baris pertama logic Streamlit)
st.set_page_config(
    page_title="Water Potability AI",
    page_icon="💧",
    layout="wide"
)

# Header Utama
st.title("💧 Sistem Cerdas Prediksi Kualitas Air")
st.markdown("### Tugas Akhir - Penerapan Algoritma Random Forest")

# Deskripsi
st.markdown("""
Selamat datang di aplikasi **Water Potability Prediction**. 

Aplikasi ini dirancang untuk memprediksi kelayakan air minum berdasarkan parameter kualitas air (Fisika & Kimia) menggunakan teknologi **Machine Learning**.

#### Fitur Utama:
* **Akurasi Tinggi:** Menggunakan algoritma Random Forest yang telah dioptimasi.
* **Analisis Cepat:** Hasil prediksi keluar dalam hitungan detik.
* **Parameter Lengkap:** Menganalisis 9 parameter vital air (pH, TDS, Sulfat, dll).

👈 **Silakan pilih menu di Sidebar sebelah kiri untuk memulai:**
1.  Pilih **Prediksi** untuk melakukan pengujian air.
2.  Pilih **Tentang** untuk mempelajari parameter dan metode.
""")

st.info("Dikembangkan oleh Steve Audie, Radhitya Wahyu, Pradipa- Universitas Dian Nuswantoro")