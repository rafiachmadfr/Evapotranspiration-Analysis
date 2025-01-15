import numpy as np
from .koef_empiris import koefisien_empiris
from .extraterrestrial_radiation import extraterrestrial_radiation

# Definisikan konstanta
kons_stefan_boltzmann = 4.903e-9  # (MJ K^(-4) m^(-2) day^(-1))
panas_laten_uap = 2.45  # (MJ/kg)
albedo_tanaman = 0.23  # Albedo tanaman

# Fungsi untuk menghitung tekanan uap jenuh (e°) pada suhu T (°C)
def saturation_vapor_pressure(T):
    return 0.6108 * np.exp((17.27 * T) / (T + 273.3))

# Fungsi untuk menghitung tekanan uap aktual (e_a) berdasarkan RH dan T_min
def actual_vapor_pressure(T_min, RH):
    e_s = saturation_vapor_pressure(T_min)
    return e_s * (RH / 100)

# Fungsi untuk menghitung kemiringan kurva tekanan uap (Δ)
def slope_of_vapor_pressure_curve(T):
    e_s = saturation_vapor_pressure(T)
    return (4098 * e_s) / (T + 273.3)**2

# Fungsi untuk menghitung konstanta psikometrik (γ)
def psychrometric_constant(P):
    return (1.013 * P) / (0.622 * panas_laten_uap)

# Fungsi untuk menghitung radiasi gelombang pendek bersih (R_ns)
def net_shortwave_radiation(R_s):
    return (1 - albedo_tanaman) * R_s

# Fungsi untuk menghitung radiasi gelombang panjang bersih (R_nl)
def net_longwave_radiation(T_avg, e_a, R_s, R_s0):
    return kons_stefan_boltzmann * T_avg * (0.34 - 0.14 * np.sqrt(e_a)) * (1.35 * R_s / R_s0 - 0.35)

# Fungsi untuk menghitung tekanan atmosfer (P) berdasarkan ketinggian
def atmospheric_pressure(altitude):
    return 101.3 * ((293 - 0.0065 * altitude) / 293)**5.26

# Fungsi untuk menghitung radiasi matahari aktual (R_s) dan R_s0 (radiasi saat cerah)
def solar_radiation(T_max, T_min, altitude, latitude, input_date):
    KRS = koefisien_empiris(T_max - T_min)
    R_a = extraterrestrial_radiation(latitude, input_date)
    
    R_s = KRS * np.sqrt(T_max - T_min) * R_a
    R_s0 = (0.75 + 2 * 10**-5 * altitude) * R_a
    
    return R_s, R_s0

# Fungsi untuk menghitung radiasi bersih (R_n)
def calculate_net_radiation(T_max, T_min, T_avg, RH, altitude, latitude, input_date):
    R_s, R_s0 = solar_radiation(T_max, T_min, altitude, latitude, input_date)
    
    e_a = actual_vapor_pressure(T_min, RH)  # Tekanan uap aktual
    
    R_ns = net_shortwave_radiation(R_s)  # Radiasi gelombang pendek bersih
    R_nl = net_longwave_radiation(T_avg, e_a, R_s, R_s0)  # Radiasi gelombang panjang bersih
    
    # Radiasi bersih (R_n)
    R_n = R_ns - R_nl
    return R_n

# Fungsi utama untuk menghitung ET Penman-Monteith
def pm_model(T_hr, RH, u_2, T_min, T_max, T_avg, altitude, latitude, input_date):

    R_a = extraterrestrial_radiation(latitude, input_date)
    
    # Menghitung tekanan uap aktual (e_a)
    e_a = actual_vapor_pressure(T_min, RH)

    # Menghitung kemiringan kurva tekanan uap (Δ)
    delta = slope_of_vapor_pressure_curve(T_hr)

    # Menghitung tekanan atmosfer (P)
    P = atmospheric_pressure(altitude)

    # Menghitung konstanta psikometrik (γ)
    gamma = psychrometric_constant(P)

    # Menghitung radiasi bersih (R_n)
    R_n = calculate_net_radiation(T_max, T_min, T_avg, RH, altitude, latitude, input_date)

    # Menghitung evapotranspirasi potensial (ET_PM) dengan persamaan Penman-Monteith
    ET_PM = (0.408 * delta * R_n + gamma * (37 / (T_hr + 237)) * u_2 * (saturation_vapor_pressure(T_hr) - e_a)) / \
            (delta + gamma * (1 + 0.34 * u_2))
    
    ET_PM_total = np.array(ET_PM)
    ET_PM_total = np.sum(ET_PM_total, axis=0)

    return R_a, ET_PM, ET_PM_total