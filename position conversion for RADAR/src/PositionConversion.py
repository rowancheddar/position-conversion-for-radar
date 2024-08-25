import numpy as np 

######################### Geodectic to ENU Converter #########################

def N(lat):
    """
    Finds the prime vertical radius, N(phi), that is used for many position conversion
    Using WGD-84 model
    
    Parameters
    ----------
    lat : (float)
        Latitude value
    
    Returns
    -------
    (float)
        the prime vertical radius
    """
    ba = ((6356752.314)**2) / ((6378137)**2)
    x = 1-ba
    x1 = (np.sin(lat))**2
    x2 = x*x1
    
    val = (6378137)/ np.sqrt(1-x2)
    return val

def geo_to_enu (latr,lonr,altr,latt,lont,altt):
    """
    Geodectic (GEO) to East North Up (ENU) conversion.

    Parameters
    ----------
    latr : (float)
        Reference Point (e.g. RADAR) latitude
    lonr : (float)
        Reference Point (e.g. RADAR) longitude
    altr : (float)
        Reference Point (e.g. RADAR) altitude, in metres
    latt : (float)
        Target Point (e.g. ADSB) latitude
    lont : (float)
        Target Point (e.g. ADSB) longitude
    altt : (float)
        Target Point (e.g. ADSB) altitude, in metres
    
    Returns
    -------
    (float)
        The ENU X value of the target from the reference point, in metres.
    """
    radlatr = latr/180 * np.pi
    radlatt = latt/180 *np.pi
    radlonr = lonr/180 *np.pi
    radlont = lont/180 * np.pi

    #elements:
    cosLatR = np.cos(radlatr)
    sinLatR = np.sin(radlatr)
    cosLonR = np.cos(radlonr)
    sinLonR = np.sin(radlonr)
    
    ba = ((6356752.314)**2) / ((6378137)**2)
    
    ####### Geo to ECEF conversion #######
    # Convert geodetic to ECEF coordinates for RADAR
    xr = (N(radlatr)+altr) * np.cos(radlatr) *np.cos(radlonr)
    yr = (N(radlatr)+altr) * np.cos(radlatr) *np.sin(radlonr)
    zr = (ba * N(radlatr) + altr) * np.sin(radlatr)
    
    # Convert geodetic to ECEF coordinates for TARGET
    xt = (N(radlatt)+altt) * np.cos(radlatt) *np.cos(radlont)
    yt = (N(radlatt)+altt) * np.cos(radlatt) *np.sin(radlont)
    zt = (ba * N(radlatt) + altt) * np.sin(radlatt)
    # end of geo to ecef conversion
    
    x1 = xt-xr
    y1 = yt-yr
    z1 = zt- zr
    
    # Matrix Multiplication
    x = (-sinLatR*cosLonR*x1) + (-sinLatR*sinLonR*y1) + (cosLatR*z1)
    y = (-sinLonR*x1)+ (cosLonR*y1)+ (0*z1)
    z = (cosLatR*cosLonR*x1) + (cosLatR*sinLonR*y1)+ (sinLatR*z1)
    
    x = np.float64(x) # Up
    y = np.float64(y) # East
    z = np.float64(z) # Up
    
    return x, y, z

####################### Position Converter: ENU to RAE ########################

def enu_to_rae (x,y,z):
    """
    East North Up (ENU) to Range, Azimuth & Elevation conversion.

    Parameters
    ----------
    x : (float) 
        The cartesian X value for the target. 
        Northing
        
    y : (float)
        The cartesian Y value for the target.
        Easting
        
    z : (float)
        The cartesian Z value for the target.
        Up
    
    Returns
    -------
    (float)
        Range of the target in meters

    (float)
        Azimuth of the target in miliradians

    (float)
        Elevation of the target in miliradians
    """
    
    # Range Calculation
    rng = np.sqrt((x**2) + (y**2) + (z**2))
    
    # Azimuth Calculation
    azi = np.mod(np.arctan2(y,x),2 * np.pi)

    # Elevation Calculation
    ele = np.arctan(z / (np.sqrt(x**2 + y**2)))
    
    return rng,azi,ele