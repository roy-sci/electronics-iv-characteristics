# I–V Characteristics of Semiconductor Devices


import numpy as np
import matplotlib.pyplot as plt





# Voltage sweep (V)
voltage = np.linspace(-5, 1, 300)


# PN diode I–V characteristics


# Parameters 
Is = 1e-12        # saturation current (A)
Vt = 0.026        # thermal voltage (V)

current_diode = []

# Explicit loop (no vectorised)
for V in voltage:
    if V > 0:
        I = Is * (np.exp(V / Vt) - 1)
    else:
        I = -Is
    current_diode.append(I)

current_diode = np.array(current_diode)


# Zener diode I–V char


zener_voltage = -3.3  # breakdown voltage (V)
zener_resistance = 50  # ohms (approx slope)

current_zener = []

for V in voltage:
    if V > 0.7:
        I = Is * (np.exp(V / Vt) - 1)
    elif V < zener_voltage:
        I = (V - zener_voltage) / zener_resistance
    else:
        I = -Is
    current_zener.append(I)

current_zener = np.array(current_zener)


# Plotting


plt.figure(figsize=(8, 5))

plt.plot(voltage, current_diode,
         label="PN Diode",
         linewidth=1.5)

plt.plot(voltage, current_zener,
         label="Zener Diode",
         linewidth=1.5)

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("I–V Characteristics of Semiconductor Devices")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# analysis output


print("Semiconductor I–V Analysis")
print("--------------------------")
print("PN Diode:")
print("• Nonlinear increase in current for forward bias")
print("• Very small reverse current")

print("\nZener Diode:")
print("• Forward bias similar to PN diode")
print("• Breakdown observed near -3.3 V")
