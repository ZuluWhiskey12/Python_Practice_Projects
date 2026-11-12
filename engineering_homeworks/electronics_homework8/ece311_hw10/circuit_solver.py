from mosfet import MOSFET
import numpy as np

def solve_common_source(v_g, circuit, mosfet):
    v_dd = circuit["v_dd"]
    r_d = circuit["r_d"]
    r_s = circuit["r_s"]
    
    k = mosfet.k
    v_threshold = mosfet.v_threshold
    
    a = 1
    b = -(1 / (k * r_s) + 2 * (v_g - v_threshold))
    c = (v_g - v_threshold) ** 2
    
    roots = np.roots([a, b, c])
    
    for v_s in roots:
        i_ds = v_s / r_s
        v_d = v_dd - i_ds * r_d
        
        region = mosfet.check_region(v_g, v_d, v_s)
        
        if region == "Saturation":
            v_ds = v_d - v_s
            return {
                "a": a,
                "b": b,
                "c": c,
                "v_s": v_s,
                "v_d": v_d,
                "v_ds": v_ds,
                "i_ds": i_ds,
                "region": region
            }
            
    raise ValueError("No valid saturation solution found")

def calculate_common_source_gain(g_m, circuit):
    r_d = circuit["r_d"]
    r_s = circuit["r_s"]
    
    return -(g_m * r_d) / (1 + g_m * r_s)