import math
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.constants import gravitational_constant as Gravity
import time

print("For this script to function, you have to put exoplanet_orbital_data3.xlsx in the SAME directory as this Python script!!")

BASE_DIR = Path(__file__).resolve().parent

data = pd.read_excel(BASE_DIR / "exoplanet_orbital_data3.xlsx")
data = data.dropna()

names = data["Exoplanet Name"].astype(str).to_numpy()
centralbodymass = data["Central Body Mass (kg)"].astype(float).to_numpy()
periapsis = data["Periapsis (m)"].astype(float).to_numpy()
apoapsis = data["Apoapsis (m)"].astype(float).to_numpy()
meandistance = data["Mean Distance (m)"].astype(float).to_numpy()

print("-" * 50)
print("Available Exoplanets in the Dataset:")
print(", ".join(names))
print("-" * 50)

while 1==1 :
    whichplanet = input("Please enter the name of the exoplanet you'd like to calculate the orbital velocity of : ").strip()
    planet_row = data[data["Exoplanet Name"].str.strip() == whichplanet]
    
    M = planet_row["Central Body Mass (kg)"].iloc[0]
    periapsis = planet_row["Periapsis (m)"].iloc[0]
    apoapsis = planet_row["Apoapsis (m)"].iloc[0]
    meandistance = planet_row["Mean Distance (m)"].iloc[0]
    
    semimajoraxis = (periapsis + apoapsis) / 2
    v = math.sqrt(Gravity * M * ((2 / meandistance) - (1 / semimajoraxis)))
    vrounded = round(v, 2)

    print("-" * 50)
    print("The orbital velocity of " + str(whichplanet) + " is: " + str(vrounded) + "m/s")
    print("-" * 50)
    stopornot = input("Would you like to stop the code or restart it? (stop/restart) : ").strip().lower()

    if stopornot == "stop":
        print("Thanks for your time!")
        break
    elif stopornot == "restart":
        continue
    else :
        print("Invalid input. Restarting.")
        continue
