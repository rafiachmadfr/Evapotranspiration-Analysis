def bc_model (hari_terang, t_avg):
    ET_BC = 0 + hari_terang * (0.46 * t_avg + 8)
    return ET_BC
