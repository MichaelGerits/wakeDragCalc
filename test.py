import pandas as pd
import numpy as np

#tests the freestream velocity calculation
# Create a sample dynamic pressure matrix (angles of attack vs pressure taps)
angles_of_attack = [0, 5, 10, 15]  # Example angles of attack
pressure_taps = ["Tap1", "Tap2", "Tap3", "Tap4"]  # Example pressure taps

# Generate random dynamic pressure values for illustration
np.random.seed(42)
dynamic_pressure_data = np.random.uniform(100, 500, (len(angles_of_attack), len(pressure_taps)))

# Create the dynamic pressure DataFrame
dynamic_pressure_df = pd.DataFrame(dynamic_pressure_data, index=angles_of_attack, columns=pressure_taps)
dynamic_pressure_df.index.name = "Angle of Attack (deg)"
dynamic_pressure_df.columns.name = "Pressure Taps"

# Create a density DataFrame (assumes uniform density across pressure taps for each angle of attack)
density_data = np.random.uniform(1.0, 1.5, len(angles_of_attack))  # Random densities
density_df = pd.DataFrame(density_data, index=angles_of_attack, columns=["Density (kg/m^3)"])
density_df.index.name = "Angle of Attack (deg)"

# Convert dynamic pressure to velocity
# Velocity formula: v = sqrt(2 * q / rho)
velocity_data = dynamic_pressure_df.div(density_df["Density (kg/m^3)"], axis=0)  # Divide pressures by densities
velocity_data = (2 * velocity_data).apply(np.sqrt)  # Compute velocities

# Create the velocity DataFrame
velocity_df = pd.DataFrame(velocity_data, index=angles_of_attack, columns=pressure_taps)
velocity_df.index.name = "Angle of Attack (deg)"
velocity_df.columns.name = "Pressure Taps"

# Print the dataframes
print("Dynamic Pressure DataFrame:")
print(dynamic_pressure_df, "\n")
print("Density DataFrame:")
print(density_df, "\n")
print("Velocity DataFrame:")
print(velocity_df)


print("\n___________________________________________________________________________________\n")
#test the wake velocity calculation-------------------------------------------------------------------------------

# Create sample DataFrames for static pressure, total pressure, and density
angles_of_attack = [0, 5, 10, 15]  # Example angles of attack
pressure_taps = ["Tap1", "Tap2", "Tap3", "Tap4"]  # Example pressure taps

# Generate random static and total pressure values
np.random.seed(42)
static_pressure_data = np.random.uniform(2, 20, (len(angles_of_attack), len(pressure_taps)))  # Pa
total_pressure_data = np.random.uniform(300, 500, (len(angles_of_attack), len(pressure_taps)))  # Pa

# Create DataFrames for static and total pressure
static_pressure_df = pd.DataFrame(static_pressure_data, index=angles_of_attack, columns=pressure_taps)
static_pressure_df.index.name = "Angle of Attack (deg)"
static_pressure_df.columns.name = "Pressure Taps"

total_pressure_df = pd.DataFrame(total_pressure_data, index=angles_of_attack, columns=pressure_taps)
total_pressure_df.index.name = "Angle of Attack (deg)"
total_pressure_df.columns.name = "Pressure Taps"

# Create a density DataFrame (same as before)
density_data = np.random.uniform(1.0, 1.5, len(angles_of_attack))  # Random densities (kg/m^3)
density_df = pd.DataFrame(density_data, index=angles_of_attack, columns=["Density (kg/m^3)"])
density_df.index.name = "Angle of Attack (deg)"

# Calculate wake velocity using the Bernoulli equation
# Velocity formula: v = sqrt(2 * (p_t - p_s) / rho)
wake_velocity_data = (total_pressure_df - static_pressure_df).div(density_df["Density (kg/m^3)"], axis=0)  # Pressure difference divided by density
wake_velocity_data = (2 * wake_velocity_data).apply(np.sqrt)  # Compute velocities

# Create the wake velocity DataFrame
wake_velocity_df = pd.DataFrame(wake_velocity_data, index=angles_of_attack, columns=pressure_taps)
wake_velocity_df.index.name = "Angle of Attack (deg)"
wake_velocity_df.columns.name = "Pressure Taps"

# Print the DataFrames
print("Static Pressure DataFrame:")
print(static_pressure_df, "\n")
print("Total Pressure DataFrame:")
print(total_pressure_df, "\n")
print("Density DataFrame:")
print(density_df, "\n")
print("Wake Velocity DataFrame:")
print(wake_velocity_df)