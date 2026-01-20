import streamlit as st

st.title("ℹ️ Tentang Aplikasi")

st.markdown("""
### Metode Penelitian
Aplikasi ini dibangun berdasarkan penelitian tugas akhir mengenai **Klasifikasi Kualitas Air**. 
Metode utama yang digunakan adalah **Random Forest Classifier**.

### Penjelasan Parameter
1.  **pH**: Tingkat keasaman (Aman: 6.5 - 8.5).
2.  **Hardness**: Kandungan mineral (kalsium & magnesium).
3.  **Solids (TDS)**: Total zat padat terlarut.
4.  **Chloramines**: Desinfektan pembunuh bakteri.
5.  **Sulfate**: Mineral alami.
6.  **Conductivity**: Daya hantar listrik air.
7.  **Organic Carbon**: Indikator bahan organik.
8.  **Trihalomethanes**: Produk sampingan klorinasi.
9.  **Turbidity**: Tingkat kekeruhan air.
""")