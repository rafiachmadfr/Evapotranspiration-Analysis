def bc_model (hari_terang, t_avg):
    ET_BC = hari_terang * (0.46 * t_avg + 8) + 1
    return ET_BC
