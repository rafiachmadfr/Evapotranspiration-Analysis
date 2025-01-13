import math
import numpy as np
from datetime import datetime

def extraterrestrial_radiation(latitude, input_date):
    
    # Konstanta
    k1 = (24 * 60) / np.pi
    solar_constant = 0.0820

    # Mengonversi input_date dari string ke objek datetime
    data_waktu = datetime.strptime(input_date, "%Y-%m-%d")

    # Hari dalam setahun
    day_of_year = data_waktu.timetuple().tm_yday

    # Perhitungan inverse distance Earth-Sun
    inverse_distance = 1 + 0.033 * np.cos((2 * np.pi / 365) * day_of_year)

    # Solar declination
    solar_declination = 0.409 * np.sin(((2 * np.pi / 365) * day_of_year) - 1.39)

    # Konversi latitude ke radian
    latitude_radians = np.radians(latitude)

    # Sunset hour angle
    sunset_hour_angle = np.arccos(np.clip(-np.tan(latitude_radians) * np.tan(solar_declination), -1, 1))

    # Menghitung Ra (extraterrestrial irradiance)
    Ra = (k1 * solar_constant * inverse_distance) * (
        sunset_hour_angle * np.sin(latitude_radians) * np.sin(solar_declination) +
        np.cos(latitude_radians) * np.cos(solar_declination) * np.sin(sunset_hour_angle)
    )

    # Ekspresi Ra dalam equivalent evaporation
    Ra_mm = Ra * 0.408

    return Ra_mm
