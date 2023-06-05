import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime

# Membaca data pasang surut
data = pd.read_excel("Dataset_Pasut_2020-2022_rev.xlsx")

# Menghapus tanda koma dari kolom "Water level"
data["Water level"] = data["Water level"].str.replace(",", "").astype(float)

# Memisahkan kolom Time menjadi kolom terpisah
data["Time"] = pd.to_datetime(data["Time"])
data["Year"] = data["Time"].dt.year
data["Month"] = data["Time"].dt.month
data["Day"] = data["Time"].dt.day
data["Hour"] = data["Time"].dt.hour

print(data["Time"])

# Menampilkan judul aplikasi
st.title("Prediksi Pasang Surut Ancol Jakarta")

# Memisahkan fitur dan target
X = data[["Year", "Month", "Day", "Hour"]].values
y = data["Water level"].values

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Melatih model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Membuat prediksi menggunakan data uji
y_pred = model.predict(X_test)

# foto
st.image("static\img\wncol-tide.png", width=696)

# garis horizontal
st.markdown("<hr>", unsafe_allow_html=True)

# Memasukkan input pengguna
st.subheader("Prediksi")
input_year = st.number_input("Masukkan tahun", min_value=2020, step=1)
input_month = st.number_input(
    "Masukkan bulan", min_value=1, max_value=12, step=1)
input_day = st.number_input(
    "Masukkan tanggal", min_value=1, max_value=31, step=1)
input_hour = st.number_input("Masukkan jam", min_value=0, max_value=23, step=1)
input_datetime = datetime(input_year, input_month, input_day, input_hour)

# Tombol untuk menghasilkan prediksi
if st.button("Prediksi"):
    input_data = np.array([[input_year, input_month, input_day, input_hour]])
    prediksi_tinggi = model.predict(input_data)
    # garis horizontal
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("Tanggal dan Waktu:", input_datetime)
    st.write("Tinggi pasang surut yang diprediksi:", prediksi_tinggi[0])
