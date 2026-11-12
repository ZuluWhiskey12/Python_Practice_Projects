from mosfet import MOSFET
from circuit_solver import solve_common_source, calculate_common_source_gain

mosfet = MOSFET("NMOS", 0.4, 0.05)

circuit = {
    "v_dd": 12.0,
    "r_d": 1000.0,
    "r_s": 250
}

gate_voltages = [0.5, 1.5, 3.0]

for v_g in gate_voltages:
    results =  solve_common_source(v_g, circuit, mosfet)
    
    g_m = mosfet.calculate_transconductance(v_g, results["v_s"])
    a_v = calculate_common_source_gain(g_m, circuit)
    
    print(f"\nGate voltage: {v_g} V")
    print(f"VS = {results['v_s']:.4f} V")
    print(f"VDS = {results['v_ds']:.4f} V")
    print(f"IDS = {results['i_ds'] * 1000:.4f} mA")
    print(f"gm = {g_m * 1000:.4f} mS")
    print(f"Av = {a_v:.4f} V/V")