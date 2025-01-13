def bc_model (hari_terang, t_avg):
    ET_BC = hari_terang * (0.46 * t_avg + 8) + 0.5
    return ET_BC
