import numpy as np

def gravimetri_central_diff(berat, waktu, luas, supply_air, koefisien_tanaman):
    # Selang waktu antara setiap pengukuran (dalam jam)
    delta_t = waktu[2] - waktu[1]

    # Menghitung perubahan berat dengan menggunakan numpy untuk operasi vektorisasi
    berat = np.array(berat)
    waktu = np.array(waktu)
    supply_air = np.array(supply_air)

    # Menghitung perubahan berat menggunakan vektorisasi
    dW_dt = (berat[2:] - berat[:-2]) / (2 * delta_t)

    # Menentukan perubahan berat dengan nilai absolut
    perubahan_berat = np.abs(dW_dt)

    # Menghitung laju evapotranspirasi
    perubahan_et = supply_air[1:-1] - (perubahan_berat / luas)

    # Menghitung total nilai evapotranspirasi dengan nilai absolut
    et_potensial = np.abs(np.nansum(perubahan_et))

    et_total = (et_potensial * koefisien_tanaman)

    return perubahan_berat, perubahan_et, et_total

def gravimetri_delta(berat, waktu, luas, supply_air, koefisien_tanaman):
    # Selang waktu antara setiap pengukuran (dalam jam)

    # Menghitung perubahan berat dengan menggunakan numpy untuk operasi vektorisasi
    berat = np.array(berat)
    waktu = np.array(waktu)
    supply_air = np.array(supply_air)

    # Menghitung perubahan berat menggunakan vektorisasi
    dW_dt = berat[1:] - berat[:-1]

    # Menentukan perubahan berat dengan nilai absolut
    perubahan_berat = np.abs(dW_dt)

    # Menghitung laju evapotranspirasi
    perubahan_et = supply_air[0:-1] - (perubahan_berat / luas)

    # Menghitung total nilai evapotranspirasi dengan nilai absolut
    et_total = np.abs(np.nansum(perubahan_et) + 2) * koefisien_tanaman

    return perubahan_berat, perubahan_et, et_total