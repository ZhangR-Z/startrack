from astropy.time import Time
import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from cal_degrees import HMStoDeg
from cal_degrees import DMStoDeg
from cal_altaz import cal_altaz
import numpy as np

def track_all(starttime=None,timezone=0,target=None,loc=None,exptime=None,readouttime=60,rotatespeed=None,ntrack=50,savetime='LT'):
    """
    track all targets with given parameters.

    Parameters
    ----------
    startime : str
        The start time of the observation in the format 'YYYY-MM-DD HH:MM:SS'
    timezone : float
        The timezone offset in hours. e.g., for UTC-1, timezone should be -1; default is 0 (UTC).
    target : list
        A list of targets, where each target is a list containing right ascension and declination coordinates.
        The right ascension should be in the format [h, m, s], and the declination should be in the format [pm, d, m, s], where pm is '+' or '-'.
    loc : EarthLocation
        The location of the observer.
    exptime : list
        A list of exposure times in seconds for each target.
    readouttime : float
        The readout time in seconds. Default is 60 seconds.
    rotatespeed : float
        The rotation speed in degrees per minutes.
    ntrack : int
        The number of tracking points. Default is 50.
    savetime : str
        The time format for saving the tracking times. 'LT' for local time, 'UTC' for Coordinated Universal Time. Default is 'LT'.

    Returns
    -------
    timetrack : list
        A list of tracking times for each target. Each element is a list of datetime objects corresponding to the tracking points.
    startrack : list
        A list of tracking points for each target. The tracking points are tuples of (altitude, azimuth) in degrees.
    """
    UTCtime = Time(starttime) + timezone * u.hour
    startrack = []
    timetrack = []
    for i in range(len(target)):
        tempra = HMStoDeg(target[i][0][0], target[i][0][1], target[i][0][2])
        tempdec = DMStoDeg(target[i][1][0], target[i][1][1], target[i][1][2], target[i][1][3])
        coord = SkyCoord(ra=tempra * u.deg, dec=tempdec * u.deg, frame='icrs')
        if (i>0) & (rotatespeed is not None):
            tempalt, tempaz = cal_altaz(coord, UTCtime, loc)
            rotatetime = (np.abs(tempalt - startrack[i-1][-1][0]) / rotatespeed) * u.minute
            UTCtime += rotatetime
        tempaltaz=[]
        temptime = []
        tempaltaz.append(cal_altaz(coord, UTCtime, loc))
        if savetime == 'LT':
            temptime.append((UTCtime-timezone*u.hour).datetime)
        elif savetime == 'UTC':
            temptime.append(UTCtime.datetime)
        for j in range(ntrack):
            timestep = exptime[i]/ntrack
            UTCtime += timestep * u.second
            tempaltaz.append(cal_altaz(coord, UTCtime, loc))
            if savetime == 'LT':
                temptime.append((UTCtime-timezone*u.hour).datetime)
            elif savetime == 'UTC':
                temptime.append(UTCtime.datetime)

        UTCtime += readouttime * u.second

        startrack.append(tempaltaz)
        timetrack.append(temptime)
    return timetrack, startrack