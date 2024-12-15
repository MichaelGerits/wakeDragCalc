import DataRead as DR
import numpy as np
import pandas as pd

c = 0.160 #chord length
#values are tabulated (rows = alpha, collumns = y position) [1 collumn = over entire tunnel]
print("Rake properties\n")
print(DR.totRake.head()) #total pressure at the rake 
print(DR.statRake.head()) #static pressure at the rake (expanded)
print(DR.dynRake.head()) #dynamic pressure at the rake
print(DR.velRake) #local velocity at the rake

print("\n Rake positions \n")
print(DR.totRakeLoc) #locations of the rake measurements

print("\ntunnel properties\n")
print(DR.tunnelData.head()) #tunnel density, temperature, rpm etc
print(DR.tunnelP.head()) #freestream static and total pressure
print(DR.frstrVelocities.head()) #freestreeam veloities

keys = list(DR.totRake.columns) #tube names(to itterate positions)


dy = np.diff(DR.totRakeLoc)  * 1e-3 #(m)
print(dy[:5])
#integrate the first term of the drag
D1 = 0
for j in range(len(dy)): #integrate with the discrete "bars" taking the leftmost value of the interval
    D1 += DR.tunnelData['rho'] * (DR.frstrVelocities - DR.velRake[keys[j]])  * DR.velRake[keys[j]] * dy[j]
print(D1.head())

print("\n\n")
##integrate the second term of the drag
D2 = 0
for j in range(len(dy)):
    D2 += DR.pStat - DR.statRake[keys[j]] * dy[j]
print(D2.head())
#calculate total drag


D = D1 + D2 #calculate the total drag

CD1 = D1.div(DR.frStrDynP, axis=0) / (c)
CD2 = D2.div(DR.frStrDynP, axis=0) / (c)
CD = D.div(DR.frStrDynP, axis=0) / (c)


