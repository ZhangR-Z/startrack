import numpy as np

def HMStoDeg(h,m,s):
    """
    Convert hours, minutes, and seconds to degrees.

    Parameters
    ----------
    h : float
        Hours.
    m : float
        Minutes.
    s : float
        Seconds.

    Returns
    -------
    float
        The equivalent angle in degrees.
    """
    if h<0 or h>24 or m<0 or m>60 or s<0 or s>60:
        raise ValueError("Invalid input: hours must be between 0 and 24, minutes and seconds must be between 0 and 60.")

    return 15 * (h + m/60 + s/3600)

def DMStoDeg(pm,d,m,s):
    """
    Convert degrees, minutes, and seconds to degrees.

    Parameters
    ----------
    d : float
        Degrees.
    m : float
        Minutes.
    s : float
        Seconds.

    Returns
    -------
    float
        The equivalent angle in degrees.
    """
    if d<-90 or d>90 or m<0 or m>60 or s<0 or s>60:
        raise ValueError("Invalid input: degrees must be between -90 and 90, minutes and seconds must be between 0 and 60.")
    if pm == '-':
        return d - m/60 - s/3600
    elif pm == '+':
        return d + m/60 + s/3600