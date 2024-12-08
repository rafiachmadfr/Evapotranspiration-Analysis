# 🌱 Evapotranspiration-Analysis  
## Evaluasi Metode Blaney-Criddle, Hargreaves-Samani, dan Penman-Monteith Dalam Menentukan Evapotranspirasi Tanaman Alpukat

**Skripsi - Fisika - Universitas Jember**  
**Rafi Achmad Fahreza | NIM: 211810201054**  

---

### 📋 Deskripsi Proyek  
Proyek ini bertujuan untuk mengevaluasi dan membandingkan beberapa metode dalam menghitung **evapotranspirasi (ET)** pada tanaman alpukat 🥑. Dengan menggunakan model **Gravimetri**, **Blaney-Criddle**, dan **Hargreaves-Samani**, proyek ini menghitung kebutuhan air tanaman berdasarkan data curah hujan 🌧️, suhu udara 🌡️, dan irigasi 🚿. Hasil analisis evapotranspirasi ini dapat digunakan untuk merancang sistem irigasi yang lebih efisien dan membantu pengelolaan sumber daya air 💧 dalam pertanian.

### 🧑‍🔬 Metode yang Digunakan  
1. **Gravimetri**: Menghitung evapotranspirasi dengan menimbang massa tanaman yang terpengaruh oleh curah hujan dan irigasi. Metode ini memberikan pendekatan langsung dengan pengukuran fisik.
   
2. **Blaney-Criddle**: Model empiris yang memperkirakan evapotranspirasi berdasarkan suhu udara dan persentase hari terang ☀️, sering digunakan dalam perhitungan irigasi pertanian.

3. **Hargreaves-Samani**: Menggunakan suhu maksimum, minimum, dan rata-rata untuk memperkirakan evapotranspirasi dengan memperhitungkan radiasi atmosfer, yang memberikan estimasi yang lebih akurat dalam kondisi tertentu 🌤️.

### 🛠️ Instalasi  
Sebelum menjalankan proyek ini, pastikan Anda telah menginstal **Python** dan pustaka-pustaka berikut:  
1. **pandas**: Untuk manipulasi dan analisis data 📊.  
2. **numpy**: Untuk perhitungan numerik dan komputasi array 🔢.  
3. **matplotlib**: Untuk visualisasi grafik 📈.  
4. **seaborn**: Untuk visualisasi data lebih lanjut, terutama dalam bentuk **heatmap** 🔥.

Anda dapat menginstal pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal: 
bash
```pip install pandas numpy matplotlib seaborn```

### ⚙️ Cara Penggunaan  

#### 1. Menyiapkan Dataset  
Proyek ini membutuhkan dua file Excel:  
- `Dataset_ET.xlsx`: Berisi data utama yang digunakan untuk perhitungan evapotranspirasi.  
- `dataset_sekunder.xlsx`: Berisi data sekunder yang digunakan sebagai referensi tambahan.  

Pastikan kedua file tersebut berisi data yang relevan dan sesuai dengan struktur yang digunakan dalam kode. File-file ini harus berada dalam folder yang sama dengan file skrip Python Anda agar dapat diakses dengan mudah.

#### 2. Langkah-langkah Perhitungan  
- **Sesuaikan Parameter**:  
  Sebelum menjalankan kode, sesuaikan beberapa parameter yang ada dalam kode sesuai dengan kondisi lokal Anda. Beberapa parameter yang perlu disesuaikan antara lain:  
  - **latitude** 🌍: Koordinat geografis lokasi tempat percobaan dilakukan.  
  - **massa jenis air** 💧: Nilai massa jenis air yang digunakan untuk perhitungan evapotranspirasi.  
  - **persentase hari terang** 🌞: Estimasi jumlah hari terang dalam periode yang dianalisis.

- **Pilih Model Perhitungan**:  
  Anda dapat memilih salah satu dari tiga model perhitungan evapotranspirasi yang disediakan dalam proyek ini:  
  - **Gravimetri**: Metode berbasis pengukuran massa tanaman.  
  - **Blaney-Criddle**: Model empiris yang memperhitungkan suhu dan jumlah hari terang.  
  - **Hargreaves-Samani**: Model yang menggunakan suhu harian maksimum dan minimum untuk estimasi ET.

- **Jalankan Kode**:  
  Setelah Anda menyesuaikan parameter dan memilih model, jalankan kode Python. Hasil perhitungan evapotranspirasi akan dihitung dan ditampilkan dalam bentuk **tabel** 📑 dan **grafik heatmap** 🔥.

#### 3. Visualisasi  
Setelah perhitungan selesai, proyek ini akan menghasilkan **heatmap** yang menggambarkan nilai evapotranspirasi (ET) total untuk setiap grup kode media tanaman. **Heatmap** ini memberikan gambaran visual yang jelas tentang distribusi kebutuhan air tanaman di berbagai kondisi yang dihitung, membantu Anda memahami pola konsumsi air dalam sistem irigasi yang dianalisis.
