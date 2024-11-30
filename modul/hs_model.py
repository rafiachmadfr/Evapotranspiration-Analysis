from .koef_empiris import koefisien_empiris

def hs_model (t_max, t_min, t_avg, Ra):

    t_rentang = t_max - t_min
    
    KRS = koefisien_empiris(t_rentang)

    ET_HS = 0.0135 * KRS * (t_max-t_min)**0.5 * (t_avg + 17.8) * Ra
    
    ETo = 0.0023 * (t_avg + 17.8) * ((t_max - t_min) ** 0.5) * Ra
    
    return ET_HS