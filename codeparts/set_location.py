from astropy.coordinates import EarthLocation
from astropy import units as u

def set_location(telescope=None, location=None):
    """
    Set the location of the telescope.

    Parameters
    ----------

    telescope : str
        The name of the telescope. This is used to identify the location.
        The supported telescopes include all sites recognized by astropy.
        The GTC, TNG, NOT, INT, WHT, and Mercator telescopes are supported by default.
        More telesocpes will be supported in the future.

    location : tuple
        The geographic coordinates of the location. Must be a tuple of (longitude, latitude, height).
        The longitude and latitude should be in degrees, and the height should be in meters.

    Returns
    -------
    EarthLocation
        An EarthLocation object representing the specified location.

    Raises
    ------
    ValueError
        If the specified location is not recognized by astropy.
    """
    if telescope is not None and location is not None:
        raise ValueError("Both telescope and location cannot be specified at the same time. Please specify only one of them.")

    if telescope is not None and location is None:
        if telescope == "GTC":
            return EarthLocation.from_geodetic(lon= -(17+53/60+31/3600) * u.deg, lat= (28+45/60+24/3600) * u.deg, height=2300 * u.m)
            
        elif telescope == "TNG":
            return EarthLocation.from_geodetic(lon= -17.8891 * u.deg, lat= 28.7553 * u.deg, height=2387 * u.m)

        elif telescope == "NOT":
            return EarthLocation.from_geodetic(lon=  -(17+53/60+6.3/3600) * u.deg, lat= (28+45/60+26.2/3600) * u.deg, height=2382 * u.m)
        
        elif telescope == "WHT":
            return EarthLocation.from_geodetic(lon=  -(17+52/60+53.9/3600) * u.deg, lat= (28+45/60+38.3/3600) * u.deg, height=2382 * u.m)

        elif telescope == "INT":
            return EarthLocation.from_geodetic(lon=  -(17+52/60+39.5/3600) * u.deg, lat= (28+45/60+43.4/3600) * u.deg, height=2382 * u.m)

        elif telescope == "Mercator":
            return EarthLocation.from_geodetic(lon=  -17.8786 * u.deg, lat= 28.7635 * u.deg, height=2333 * u.m)

        else:
            try:
                loc = EarthLocation.of_site(telescope)
                return loc
            
            except Exception as e:
                raise ValueError(f"Could not set location: {e}")
        
    if location is not None and telescope is None:
        if len(location) != 3:
            raise ValueError("Location must be a tuple of (longitude, latitude, height).")
        try:
            lon, lat, height = location
            loc = EarthLocation.from_geodetic(lon=lon * u.deg, lat=lat * u.deg, height=height * u.m)
            return loc
        except Exception as e:
            raise ValueError(f"Could not set location: {e}")