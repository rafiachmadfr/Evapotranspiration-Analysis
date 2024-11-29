import numpy as np

def gravimetri(berat, waktu, luas, supply_air):
    
    # Selang waktu antara setiap pengukuran (dalam jam)
    delta_t = waktu[2] - waktu[1]

    perubahan_berat = []
    perubahan_volume = []
    perubahan_et = []

    # Menghitung turunan tengah dari jam ke-2 hingga jam ke-9
    for i in range(1, len(berat)-1):
        dW_dt = (berat[i+1] - berat[i-1]) / (2 * delta_t)
        perubahan_berat.append(dW_dt)

    # # Menghitung turunan biasa dari jam ke-2 hingga jam ke-9
    # for i in range(1, len(volume)-1):
    #     dW_dt = (volume[i] - volume[i+1])
    #     perubahan_volume.append(dW_dt)

    # Konversi berat ke volume
    for i in range(len(perubahan_berat)):
        berat_to_volume = perubahan_berat[i] * 1e6
        perubahan_volume.append(berat_to_volume)

    # Menghitung nilai laju evapotranspirasi
    for i in range(len(perubahan_volume)):
        perubahan_et.append(supply_air[i] - (perubahan_volume[i] / luas))

    # Menghitung total nilai evapotranspirasi
    et_total = np.nansum(perubahan_et)
    # print(f"ET Total Tanaman {sheet_name}: {et_total} mm/day")

    return(perubahan_volume, perubahan_et, et_total)

