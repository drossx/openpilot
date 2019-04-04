# Created by Fayez Joseph Chedid

from gpsdpyx import connect, get_current
import time, sys
from math import sin, cos, sqrt, atan2, radians
import signal

# IP of the OBU
device = "192.168.3.102"

def parserInit():

    global gpsLocation

    def signal_handler(signum, frame):
        raise Exception('Timed out')

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(1) #3 seconds to connect

    #log
    log = open("initlog.txt", "a")
    sys.stdout = log

    # Set parameters
    try:
        connect(host=device)
        gpsLocation = get_current()
        print('Connected')
    except Exception, msg:
        print('Timed out')
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def distanceCalc():

    global gpsLocation

    #log
    log = open("mainlog.txt", "a")
    sys.stdout = log

    # Get the current position
    try:
        gpsLocation = get_current()
    except AttributeError:
        print("No signal found")
        return False

    print('made it in')

    # Opens the modifier.txt
    #f = open("modifier.txt")
    #modx = f.read()
    #mod = int(modx)

    # Output for debugging
    #print("This is my latitude", gpsLocation.lat)
    #print("This is my longitude", gpsLocation.lon)

    # Approximate radius of Earth in km
    R = 6378.1

    # Setting the two latitudes and longitudes
    lat1 = radians(abs(gpsLocation.lat))
    lon1 = radians(abs(gpsLocation.lon))

    # Stop sign coordinates go here
    lat2 = radians(abs(45.37878))
    lon2 = radians(abs(-75.65460))

    # Calculating the difference
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Using Haversine formula to calculates the distance between the two points and prints in km
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance in meters and round to 4 decimals
    d = (R * c)*1000
    distance = round(d, 4)

    print("Result:", abs(distance), "m")

    # If the distance is less than X meters (in this example) then apply the brakes
    if distance <= 5:
        return True
    else:
        return False

