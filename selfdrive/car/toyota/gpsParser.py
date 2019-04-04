# Created by Fayez Joseph Chedid

from gpsdpyx import connect, get_current
import time
from math import sin, cos, sqrt, atan2, radians

# IP of the OBU
device = "192.168.3.102"

def distanceCalc():

    print('Waiting for a connection')

    # Set parameters
    connect(host=device)

    print("Parsing GPS information...")

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

    print("Result:", abs(distance*mod), "m")

    # If the distance is less than X meters (in this example) then apply the brakes
    if distance <= 5:
        return True
    else:
        return False

def main():
    # Opens the modifier.txt
    f = open("modifier.txt")
    modx = f.read()
    mod = int(modx)

    # Get the current position
    gpsLocation = get_current()

    # Output for debugging
    print("This is my latitude", gpsLocation.lat)
    print("This is my longitude", gpsLocation.lon)

    # Calls distance calculation
    distanceCalc()

    # Update the time it refreshes (in seconds)
    time.sleep(1)
