## Introduction
This repository provides a simple Python implementation of coordinate transformations for radar tracking systems, including:
Conversion from Geodetic Coordinates (Latitude, Longitude, Altitude) to ENU (East-North-Up) local tangent plane.
Conversion from ENU to Radar coordinates (Range, Azimuth, Elevation).

## How it works
PositionConversion.py contains the core mathematical functions used for coordinate transformations:
1. Geodetic to ENU: Converts global latitude, longitude, and altitude into a local East-North-Up coordinate system relative to a reference point.
2. ENU to RADAR: Converts ENU coordinates into radar-based coordinates: Range, Azimuth, and Elevation, which are typically used for target detection and tracking.

main.py serves as the entry point for the program:
1. Prompts the user to input the reference point and target point in geodetic coordinates.
2. Calls the appropriate functions from PositionConversion.py to:
3. Convert geodetic coordinates to ENU
4. Then convert ENU to radar coordinates
5. Displays the final output in a readable format (range, azimuth, and elevation).

## Setup
1. run main.py 
2. Input the geodetic coordinates of your reference and target points

1. Clone the repository:
2. Install dependencies under requirements.txt
3. Run main.py
4. Follow the prompt and input the geodetic coordinates when prompted:
Reference point: Latitude, Longitude, Altitude
Target point: Latitude, Longitude, Altitude
