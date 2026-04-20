import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

def plot_position(tempaltaz,objname=None):
    """
    Plot the altitude and azimuth of the targets over time.

    Parameters
    ----------
    timetrack : list
        A list of tracking times for each target. Each element is a list of datetime objects corresponding to the tracking points.
    startrack : list
        A list of tracking points for each target. Each element is a list of tuples (altitude, azimuth) in degrees corresponding to the tracking points.

    Returns
    -------
    None
        This function does not return anything. It generates a plot of altitude and azimuth over time for each target.
    """

    if objname is None:
        objname = ['Target {}'.format(i+1) for i in range(len(tempaltaz))] 

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    xx = np.linspace(0, 2*np.pi, 360)
    plt.plot(xx,np.ones(360)*60,color='red')
    plt.plot(xx,np.ones(360)*5,color='red')
    for i in range(len(tempaltaz)):
        tempalt = tempaltaz[i][0]
        tempaz =  tempaltaz[i][1]
        az_rad = np.radians(tempaz)
        r = 90 - tempalt
        ax.scatter(az_rad, r, label=objname[i])
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1) 
    ax.set_xticks(np.radians([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(['N (0°)', 'NE', 'E (90°)', 'SE', 'S (180°)', 'SW', 'W (270°)', 'NW'],fontsize=14)
    ax.set_yticks([0, 30, 60, 90])
    ax.set_yticklabels(['90° (Zenith)', '60°', '30°', '0° (Horizon)'], color='grey',fontsize=14)
    ax.tick_params(labelsize=12)
    ax.legend(bbox_to_anchor=(1,-0.05),fontsize=14,ncol=4)

    ax.set_ylim(0, 90)

    plt.tight_layout()
    plt.show()

