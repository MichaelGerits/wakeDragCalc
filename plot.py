import DataRead as DR
import DragCalc as calc
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(DR.attackAngles, calc.CD1, marker="o", linestyle="-", color="red", label="velocity CD")
plt.plot(DR.attackAngles, calc.CD2, marker="o", linestyle="-", color="green", label="pressure CD")
plt.plot(DR.attackAngles, calc.CD, marker="o", linestyle="-", color="blue", label="Total CD")
plt.title("CD Vs apha", fontsize=16)
plt.xlabel("Angle of Attack (deg)", fontsize=14)
plt.ylabel("Drag Coeficcient (-)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()