import numpy as np

def gravimetri(berat, waktu, luas, supply_air):
    
    # Selang waktu antara setiap pengukuran (dalam jam)
    delta_t = waktu[2] - waktu[1]

    perubahan_berat = []
    perubahan_et = []

    for i in range(1, len(berat)-1):
        dW_dt = (berat[i+1] - berat[i-1]) / (2 * delta_t)
        
        # Memasukkan perubahan berat sebagai nilai plus atau minus
        if dW_dt >= 0:
            perubahan_berat.append(dW_dt)  # air bertambah (positif)
        else:
            perubahan_berat.append(-dW_dt)  # air berkurang (negatif)

    # Menghitung nilai laju evapotranspirasi
    for i in range(len(perubahan_berat)):
        perubahan_et.append(supply_air[i+1] - (perubahan_berat[i] / luas))

    # Menghitung total nilai evapotranspirasi
    et_total = np.abs(np.nansum(perubahan_et))
    # print(f"ET Total Tanaman {sheet_name}: {et_total} mm/day")

    return(perubahan_berat, perubahan_et, et_total)

