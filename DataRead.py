import pandas as pd
import numpy as np
data = pd.read_csv('raw_testG82D.txt', skipinitialspace=True, skiprows=[1], sep=r'\t') #import the data


"""
Process the data into organised chunks
"""
data.columns = data.columns.str.strip()
columns_to_drop = range(8,57)  # drop the airfoil taps
data = data.drop(data.columns[columns_to_drop], axis=1)


totRake = data.iloc[:, 8:55] #total pressure at the rake
totRakeLoc = np.array([
0, 12, 21, 27, 33, 39, 45, 51, 57, 63, 69, 72, 75, 78, 81, 84, 87, 90,
93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135,
138, 141, 144, 147, 150, 156, 162, 168, 174, 180, 186, 195, 207, 219
]) #locations of the pressure measurements (mm)


statRake = data.iloc[:, 56:68] #static pressure at the rake (not expanded)
statRakeLoc = np.array([
43.5, 55.5, 67.5, 79.5, 91.5, 103.5, 115.5, 127.5, 139.5, 151.5, 163.5, 175.5
]) #locations of the pressure taps (not expanded) (mm)

attackAngles = data[['Alpha']] #angles of attack
tunnelData = data.iloc[:, 3:8] #tunnel data: rho, T, rpm etc
tunnelP =data[['P097', 'P110']] #freestream static and total pressure

"""
process the data into usefull metrics
"""
#given equation fro freestream dynamic pressure
frStrDynP = 0.211804 + 1.928442 * tunnelData['Delta_Pb'] + 1.879374e-4 * (tunnelData['Delta_Pb']**2)

#getting free stream vel with bernouilli
frstrVelocities = frStrDynP.div(tunnelData["rho"], axis=0)  # Divide pressures by densities
frstrVelocities = (2 * frstrVelocities).apply(np.sqrt) #apply sqrt


'''
this part expands the static rake values to correspond with the total values

It looks at the positios and any positions  that fall in between the defined values get copied

temp will take the tap names of the total pressure too, to make it easier to itterate once integrating
'''
tkeys = totRake.columns #collumn keys to itterate
skeys = statRake.columns #collumn keys to itterate
temp = pd.DataFrame(columns=tkeys, index = range(len(data))) #temporary dataframe with same size and keys as totRake


tcol = 0 #placed here as to not itterate over already looked at positions
#itterate over the static rake locations
for scol in range(len(statRakeLoc)):
    #while the position falls in between copy static pressure
    while totRakeLoc[tcol] <= statRakeLoc[scol]:
        temp[list(tkeys)[tcol]] = statRake[list(skeys)[scol]]
        tcol+=1

#fill in the remaining collumn (the end, where static doesn't go)
for i in range(tcol,len(totRakeLoc)):
    temp[list(tkeys)[i]] = statRake[list(skeys)[-1]]

statRake = temp

#Gets the dynamic prssure along the rakes
dynRake = totRake-statRake

#gets the local velocity

velRake = (dynRake).div(tunnelData["rho"], axis=0)  # Pressure difference divided by density
velRake = (2 * velRake).apply(np.sqrt)  # Compute velocities

"""
Test prints
"""
#print(frStrDynP.head())
#print(frstrVelocities.head())
#print(totRake.head())
#print(totRakeLoc[:5])
#print(statRake.head())
#print(attackAngles.head())
#print(tunnelData.head())
#print(tunnelP.head())
