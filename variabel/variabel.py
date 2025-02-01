# koordinat
latitude = -8.188
altitude = 98

# Massa jenis air dalam kg/m^3
rho_air = 1000

Koefisien_tanaman_alpukat = 0.5

# BC Metode berdasarkan tabel persentase hari terang
persentase_hari_terang = 0.27

kode_groups = ("A", "B", "C", "D", "E", "F")

sisi_media_tanaman = {
    'A1' : (12.5,), 'A2' : (12.5,), 'A3' : (12.5,), 'A4' : (12.5,),
    'B1' : (15.0,), 'B2' : (15.0,), 'B3' : (15.0,), 'B4' : (15.0,),
    'C1' : (17.5,), 'C2' : (17.5,), 'C3' : (17.5,), 'C4' : (17.5,),
    'D1' : (20.0,), 'D2' : (20.0,), 'D3' : (20.0,), 'D4' : (20.0,),
    'E1' : (22.5,), 'E2' : (22.5,), 'E3' : (22.5,), 'E4' : (22.5,),
    'F1' : (25.0,), 'F2' : (25.0,), 'F3' : (25.0,), 'F4' : (25.0,), }  # Satuan cm

tinggi_tanaman = {
    'A1' : (25,), 'A2' : (40,), 'A3' : (45,), 'A4' : (60,),
    'B1' : (25,), 'B2' : (40,), 'B3' : (45,), 'B4' : (60,),
    'C1' : (25,), 'C2' : (40,), 'C3' : (45,), 'C4' : (60,),
    'D1' : (25,), 'D2' : (40,), 'D3' : (45,), 'D4' : (60,),
    'E1' : (25,), 'E2' : (40,), 'E3' : (45,), 'E4' : (60,),
    'F1' : (25,), 'F2' : (40,), 'F3' : (45,), 'F4' : (60,), }   # Satuan cm

# Define the pot groups based on their sizes
pot_groups = {
    "A": ["A1", "A2", "A3", "A4"],
    "B": ["B1", "B2", "B3", "B4"],
    "C": ["C1", "C2", "C3", "C4"],
    "D": ["D1", "D2", "D3", "D4"],
    "E": ["E1", "E2", "E3", "E4"],
    "F": ["F1", "F2", "F3", "F4"],
}