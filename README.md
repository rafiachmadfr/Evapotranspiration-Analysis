# Evapotranspiration-Analysis
##  Evaluasi Metode Blaney-criddle, Hargreaves-samani, dan Penman-monteith Dalam Menentukan Evapotranspirasi Tanaman Alpukat

SKRIPSI - Fisika - Universitas Jember - Rafi Achmad Fahreza 211810201054  


### Deskripsi Proyek
Proyek ini bertujuan untuk menghitung nilai evapotranspirasi (ET) dengan menggunakan tiga model berbeda: Gravimetri, Blaney-Criddle, dan Hargreaves-Samani. Proyek ini mengolah data curah hujan, suhu udara, dan irigasi untuk menentukan kebutuhan air tanaman di beberapa kelompok kode media tanaman. Hasil perhitungan ET ini dapat digunakan untuk analisis pertanian dan irigasi.

### Model yang Digunakan:
Gravimetri: Menghitung evapotranspirasi dengan metode penimbangan massa tanaman yang terpengaruh oleh curah hujan dan irigasi.
Blaney-Criddle: Model empiris yang menghitung ET berdasarkan suhu udara dan persentase hari terang.
Hargreaves-Samani: Model yang menggunakan suhu maksimum, minimum, dan rata-rata untuk menghitung evapotranspirasi dengan mempertimbangkan radiasi atmosfer.

### Instalasi
Untuk menjalankan proyek ini, pastikan Anda memiliki Python terinstal dengan beberapa pustaka berikut:
1. pandas: Untuk manipulasi data.
2. numpy: Untuk perhitungan numerik.
3. matplotlib: Untuk visualisasi data.
4. seaborn: Untuk visualisasi data lebih lanjut, khususnya heatmap.
Anda dapat menginstal pustaka yang dibutuhkan dengan menjalankan perintah berikut:

`pip install pandas numpy matplotlib seaborn`

### Penggunaan
#### 1. Persiapkan dataset:

Proyek ini membutuhkan dua file Excel: Dataset_ET.xlsx dan dataset_sekunder.xlsx.
Pastikan kedua file tersebut memiliki data yang relevan sesuai dengan struktur yang digunakan dalam kode.

#### 2. Langkah-langkah:

Ubah nilai-nilai parameter seperti latitude, massa jenis air, dan persentase hari terang sesuai dengan kebutuhan spesifik Anda.
Jalankan perhitungan dengan model Gravimetri, Blaney-Criddle, atau Hargreaves-Samani. Hasilnya akan dihitung dan ditampilkan dalam bentuk tabel dan heatmap.

#### 3. Visualisasi:

Setelah perhitungan selesai, proyek ini akan menghasilkan heatmap yang menggambarkan nilai ET total untuk setiap grup kode.

### Dependensi
Python 3.x
pandas
numpy
matplotlib
seaborn

### Lisensi
Proyek ini dilisensikan di bawah MIT License. Anda dapat mengubah, mendistribusikan, dan menggunakannya untuk tujuan pribadi atau komersial.

### Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka issue jika ada masalah yang perlu diperbaiki. Semua kontribusi diterima dan dihargai.

### Kontak
Untuk pertanyaan lebih lanjut, Anda dapat menghubungi saya melalui email: rafiachmadfr@gmail.com.
