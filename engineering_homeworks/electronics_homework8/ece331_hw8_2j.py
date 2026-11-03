import matplotlib.pyplot as plt
import numpy as np

# Circuit parameters
thevenin_voltage = 2.0                      # Volts
peak_input_voltage = 0.0575                 # Volts
r_th = 600.0                                # Ohms
c_1 = 10e-6                                 # Farads
angular_frequency = 6283.0                  # rad/s

# Calculate the transfer function
tau = r_th * c_1
transfer_function = ((1j * angular_frequency * tau) /
                     (1 + 1j * angular_frequency *tau))

magnitude = np.abs(transfer_function)
phase_rad = np.angle(transfer_function)

# Calculate gate voltage over time
time_s = np.linspace(0, 0.002, 1000)

total_gate_voltage = (
    thevenin_voltage 
    + peak_input_voltage
    * magnitude
    * np.cos(angular_frequency * time_s + phase_rad))

# Plot the MOSFET Gate Voltage vs Time
plt.plot((time_s * 1000), total_gate_voltage)
plt.grid()
plt.xlabel("Time [ms]")
plt.ylabel("Gate Voltage [V]")
plt.title("MOSFET Gate Voltage vs Time")

plt.show()