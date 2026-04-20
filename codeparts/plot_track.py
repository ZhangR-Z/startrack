import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

def plot_track(timetrack, startrack,objname=None):
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
        objname = ['Target {}'.format(i+1) for i in range(len(startrack))] 

    for i in range(len(startrack)):
        tempalt = np.array(startrack[i]).T[0]
        tempaz =  np.array(startrack[i]).T[1]
        plt.figure(figsize=(12,6))
        plt.subplot(121)
        plt.plot(timetrack[i],tempalt,label=objname[i])
        plt.xlabel('Time',fontsize=14)
        plt.ylabel('Altitude (Degrees)',fontsize=14)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.tick_params(labelsize=12)
        plt.legend(fontsize=12)
        plt.subplot(122)
        plt.plot(timetrack[i],tempaz)
        plt.xlabel('Time',fontsize=14)
        plt.ylabel('Azimuth (Degrees)',fontsize=14)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.tick_params(labelsize=12)
        plt.show()

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    xx = np.linspace(0, 2*np.pi, 360)
    plt.plot(xx,np.ones(360)*60,color='red')
    plt.plot(xx,np.ones(360)*5,color='red')
    for i in range(len(startrack)):
        tempalt = np.array(startrack[i]).T[0]
        tempaz =  np.array(startrack[i]).T[1]
        az_rad = np.radians(tempaz)
        r = 90 - tempalt
        ax.plot(az_rad, r, linewidth=2, label='Star Trajectory')
        if i==0:
            ax.scatter(az_rad[0], r[0], color='green', marker='<', s=100, label='Start', zorder=5)
        elif i!=0:
            ax.plot([finalaz,az_rad[0]], [finalr, r[0]],color='grey',linestyle='--', linewidth=1,alpha=0.5)
        if i==len(startrack)-1:
            ax.scatter(az_rad[-1], r[-1], color='red', marker='x', s=100, label='End', zorder=5)
        finalaz = az_rad[-1]
        finalr = r[-1]

    ax.set_theta_zero_location('N')
        
    ax.set_theta_direction(-1) 

    ax.set_xticks(np.radians([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(['N (0°)', 'NE', 'E (90°)', 'SE', 'S (180°)', 'SW', 'W (270°)', 'NW'])

    ax.set_yticks([0, 30, 60, 90])
    ax.set_yticklabels(['90° (Zenith)', '60°', '30°', '0° (Horizon)'], color='grey')

    ax.set_ylim(0, 90)

    plt.tight_layout()
    plt.show()

