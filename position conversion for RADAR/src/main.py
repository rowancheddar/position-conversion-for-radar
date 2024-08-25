"""
This is an algorithm that converts position coordinates from geodetic to enu to radar

Input the geodetic information of reference and target points to convert it to range, azimuth and elevation

Parameters in your dataframe
----------
latr : (float)
    Reference Point (e.g. RADAR) latitude
lonr : (float)
    Reference Point (e.g. RADAR) longitude
altr : (float)
    Reference Point (e.g. RADAR) altitude, in metres
latt : (float)
    Target Point latitude
lont : (float)
    Target Point longitude
altt : (float)
    Target Point altitude, in metres
"""
import numpy as np
import pandas as pd
from PositionConversion import geo_to_enu, enu_to_rae

# Collecting user input for the reference point
latr = float(input("Enter the reference latitude: "))
lonr = float(input("Enter the reference longitude: "))
altr = float(input("Enter the reference altitude (in meters): "))

# Collecting user input for the target point
latt = float(input("Enter the target latitude: "))
lont = float(input("Enter the target longitude: "))
altt = float(input("Enter the target altitude (in meters): "))

data = {
    'Reference_Lat': [latr],
    'Reference_Lon': [lonr],
    'Reference_Alt': [altr],
    'Target_Lat': [latt],
    'Target_Lon': [lont],
    'Target_Alt': [altt]
}

df1 = pd.DataFrame(data)

df1["x"], df1["y"], df1["z"] = geo_to_enu(latr,lonr,altr,latt,lont,altt) 

df1["rng"], df1["azi"], df1["ele"] = enu_to_rae(df1["x"],df1["y"],df1["z"])
print(f"Range = {df1['rng'][0]} m")
print(f"Azimuth = {df1['azi'][0]} rad")
print(f"Elevation = {df1['ele'][0]} rad")
