from astropy.coordinates import AltAz

def cal_altaz(coord, obs_time, obs_loc):
    """
    Calculate the altitude and azimuth of a celestial object at a given time and location.

    Parameters
    ----------
    coord : SkyCoord
        The celestial coordinates of the object (RA and Dec).
    
    obs_time : Time
        The time of observation. This should be an astropy Time object.
    
    obs_loc : EarthLocation
        The location of the observer. This should be an astropy EarthLocation object.

    Returns
    -------
    tuple
        A tuple containing the altitude and azimuth in degrees.
    """
    altaz_frame = AltAz(obstime=obs_time, location=obs_loc)
    target_altaz = coord.transform_to(altaz_frame)
    return target_altaz.alt.degree, target_altaz.az.degree