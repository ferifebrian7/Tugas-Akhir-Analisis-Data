# -*- coding: utf-8 -*-
"""Tugas Akhir Proyek Analisis Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsUkub99dJ07fYuGODa-33HmeKGA44wI

# Proyek Analisis Data: Nama Dataset

*   Nama: Feri Dwi Febrianto
*   Email: ferifebian678@gmail.com
*   ID Dicoding: feridwifebrianto
*   Dataset: PRSA_Data_Aotizhongxin_20130301-20170228.csv

# Menentukan Pertanyaan Bisnis
*   Pertanyaan 1: Tampilkan visualisasi dan analisis dari parameter RAIN
*   Pertanyaan 2: Tampilkan visualisasi dan analisis dari parameter TEMP

# Menyiapkan semua library yang dibutuhkan
"""

# Mengimpor library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

"""# Data Wrangling

**Gathering Data**
"""

# Mengunggah file
uploaded = files.upload()

"""**Assessing Data**

Membaca data dari file CSV
"""

# Membaca data dari file CSV
for fn in uploaded.keys():
  data = pd.read_csv(fn)

"""Melihat 5 baris pertama dari data"""

# Melihat 5 baris pertama dari data
print(data.head())

"""Deskripsi statistik dari data"""

# Deskripsi statistik dari data
print(data.describe())

"""**Cleaning Data**

Membaca Dataframe
"""

df = pd.DataFrame(data)

"""Menampilkan data awal"""

# Tampilkan data awal
print("Data Awal:")
print(df)

"""Menghapus baris yang memiliki nilai kosong(NaN)"""

# Hapus baris yang memiliki nilai kosong (NaN)
df_cleaned = df.dropna()

"""Menampilkan data setelah dibersihkan"""

# Tampilkan data setelah dibersihkan
print("\nData Setelah Dibersihkan:")
print(df_cleaned)

"""# Exploratory Data Analysis (EDA)

Explore
"""

# Tampilkan statistik deskriptif
print("\nStatistik Deskriptif:")
print(df.describe(include='all'))

"""# Visualization & Explanatory Analysis

Menampilkan visualisasi data
"""

# Visualisasi data
data.hist()
plt.show()

"""Pertanyaan 1:"""

# Analisis kualitas air
# Misalnya, kita ingin menganalisis parameter RAIN
ph = data['RAIN']
print(ph.describe())
ph.hist()
plt.title('Distribusi RAIN')
plt.show()

"""Pertanyaan 2:"""

# Analisis kualitas air
# Misalnya, kita ingin menganalisis parameter TEMP
ph = data['TEMP']
print(ph.describe())
ph.hist()
plt.title('Distribusi TEMP')
plt.show()

"""# Conclusion
*   Conclusion 1: Nilai distribusi RAIN tertinggi sebesar 35000
*   Conclusion 2: Nilai distribusi TEMP tertinggi sebesar 6000



"""