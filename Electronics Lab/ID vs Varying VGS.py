import matplotlib.pyplot as plt
import csv

def parse_CSV(filename):
    x = []
    y = []
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter= ',')

        for row in lines:
            try:
                voltage = float(row[0])
                drain_Current = float(row[1])
                
                x.append(voltage)
                y.append(drain_Current * (10**3))
                
            except(ValueError, IndexError):
                continue
    return x,y

VGS, ID = parse_CSV("1a Fixed.csv")
VOV = []
for voltage in VGS:
    VOV.append(voltage - 1.5)
    
VDS_17, ID_17 = parse_CSV("1.7V VGS vs ID.csv")
VDS_19, ID_19 = parse_CSV("1.9V VGS vs ID.csv")
VDS_205, ID_205 = parse_CSV("2.05V VGS vs ID.csv")

plt.plot(VOV, ID, color = 'purple', linestyle = 'solid', label = "$I_{D}$ vs $V_{GS}$ - $V_{T}$")
plt.plot(VDS_17, ID_17, color = 'r', label = '$V_{GS}$ = 1.7 V')
plt.plot(VDS_19, ID_19, color = 'b', label = '$V_{GS}$ = 1.9 V')
plt.plot(VDS_205, ID_205, color = 'g', label = '$V_{GS}$ = 2.05 V')

plt.xlabel("$V_{DS}$ [V]")
plt.ylabel("$I_{D}$ [mA]")
plt.title("NMOS I-V Characteristics at Varying Gate Biases")
plt.xlim(-0.1,5)
plt.grid()
plt.legend()

plt.show()