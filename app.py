from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime

app = Flask(__name__)

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

# Memisahkan fitur dan target
X = data[["Year", "Month", "Day", "Hour"]].values
y = data["Water level"].values


# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


print("NILAI X")
print(X)

# Melatih model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Membuat prediksi menggunakan data uji
y_pred = model.predict(X_test)

print(data["Time"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/prediksi")
def prediksi():
    return render_template("prediksi.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/result")
def result():

    tahun = request.args.get('tahun')
    bulan = request.args.get('bulan')
    hari = request.args.get('hari')
    jam = request.args.get('jam')

    input_data = np.array([[tahun, bulan,hari,jam]])
    prediksi_tinggi = model.predict(input_data)
    return str(prediksi_tinggi[0])

if __name__ == "__main__":
    app.run(debug=True)

