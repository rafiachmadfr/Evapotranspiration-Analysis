import math

# Fungsi untuk menghitung radiasi ekstraterestrial (Ra) dalam MJ/m²/hari
def calc_Ra(latitude, day_of_year):
    # Konstanta
    Gsc = 0.0820  # Konstanta surya (MJ/m²/menit)
    
    # Konversi lintang ke radian
    phi = math.radians(latitude)
    
    # Deklinasi matahari (rad)
    delta = 0.409 * math.sin(2 * math.pi * day_of_year / 365 - 1.39)
    
    # Sudut matahari (rad)
    dr = 1 + 0.033 * math.cos(2 * math.pi * day_of_year / 365)
    
    # Sudut waktu matahari (jam)
    omega_s = math.acos(-math.tan(phi) * math.tan(delta))
    
    # Radiasi matahari ekstraterestrial (Ra)
    Ra = (24 * 60 / math.pi) * Gsc * dr * (omega_s * math.sin(phi) * math.sin(delta) + math.cos(phi) * math.cos(delta) * math.sin(omega_s))
    
    return Ra

# Fungsi untuk menghitung ET₀ menggunakan Penman-Monteith
def calc_ET0(T_mean, RH, n, N, u2, latitude, day_of_year, elevation):
    # Konstanta
    G = 0  # Fluks panas tanah harian (dianggap 0)
    cp = 0.34  # Koefisien psikrometrik (kPa/°C)
    
    # Langkah 1: Menghitung radiasi matahari Rs (MJ/m²/hari)
    a_s = 0.25
    b_s = 0.50
    Ra = calc_Ra(latitude, day_of_year)  # Radiasi matahari ekstraterestrial
    Rs = (a_s + b_s * (n / N)) * Ra
    
    # Langkah 2: Menghitung tekanan uap jenuh (e_s) dan tekanan uap aktual (e_a)
    e_s = 0.6108 * math.exp((17.27 * T_mean) / (T_mean + 237.3))
    e_a = e_s * (RH / 100)
    
    # Langkah 3: Menghitung radiasi bersih (R_n)
    R_n = (1 - 0.23) * Rs  # Angka albedo (0.23 untuk permukaan tanaman)
    
    # Langkah 4: Menghitung konstanta psikrometrik (γ)
    P = 101.3 * ((293 - 0.0065 * elevation) / 293) ** 5.26  # Tekanan udara (kPa)
    γ = 0.665 * 10**-3 * P  # Konstanta psikrometrik (kPa/°C)
    
    # Langkah 5: Menghitung kemiringan kurva tekanan uap jenuh (Δ)
    Δ = (4098 * (0.6108 * math.exp((17.27 * T_mean) / (T_mean + 237.3)))) / (T_mean + 237.3) ** 2
    
    # Langkah 6: Menghitung ET₀
    ET0 = (0.408 * Δ * (R_n - G) + γ * (900 / (T_mean + 273)) * u2 * (e_s - e_a)) / (Δ + γ * (1 + cp * u2))
    
    return ET0

# Masukkan data
T_mean = 25.0  # Suhu rata-rata harian (°C)
RH = 60.0  # Kelembaban relatif rata-rata harian (%)
n = 8.0  # Durasi penyinaran matahari aktual (jam)
N = 12.0  # Durasi penyinaran matahari maksimum (jam)
u2 = 2.0  # Kecepatan angin pada ketinggian 2 meter (m/s)
latitude = -8.18  # Lintang lokasi (derajat)
day_of_year = 249  # Hari ke-200 dalam setahun
elevation = 96  # Ketinggian lokasi (meter di atas permukaan laut)

ET0 = calc_ET0(T_mean, RH, n, N, u2, latitude, day_of_year, elevation)

print(f"Nilai ET₀ harian: {ET0:.2f} mm/hari")
