from .koef_empiris import koefisien_empiris
from .extraterrestrial_radiation import extraterrestrial_radiation

def hs_model (t_max, t_min, t_avg, latitude, input_date):

    t_rentang = t_max - t_min
    
    KRS = koefisien_empiris(t_rentang)
    Ra = extraterrestrial_radiation(latitude, input_date)

    ET_HS = 0.0135 * KRS * (t_max-t_min)**0.5 * (t_avg + 17.8) * Ra
    
    ETo = 0.0023 * (t_avg + 17.8) * ((t_max - t_min) ** 0.5) * Ra
    
    return Ra, ET_HS