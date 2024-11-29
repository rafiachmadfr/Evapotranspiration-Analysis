def hs_model (t_max, t_min, t_avg, Ra):

    t_rentang = t_max - t_min
    
    def koefisien_empiris(t_rentang):
        Krs = (0.00185 * (t_rentang) ** 2 ) - 0.0433
        return Krs

    ET_HS = 0.0135 * koefisien_empiris(t_rentang) * (t_max-t_min)**0.5 * (t_avg + 17.8) * Ra
    
    ETo = 0.0023 * (t_avg + 17.8) * ((t_max - t_min) ** 0.5) * Ra
    
    return ET_HS