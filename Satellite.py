"""

    student: Brayan Cruz

    Module: gladysSatellite

    Description: Opens and reads any of the four data files from disk based on the satellite name given to readSat function.

    Reads latitude, longitude, altitude, and time information into data structures.

    Returns the data that was read to the gladysUserInterface module

"""

import json
pathToFile = "/Users/brayancruz/Documents/GitHub/class-python-test1/gladysSatellite/time-satellite.json"
pathToFile = "/Users/brayancruz/Documents/GitHub/class-python-test1/gladysSatellite/longitude-satellite.json"
pathToFile = "/Users/brayancruz/Documents/GitHub/class-python-test1/gladysSatellite/latitude-satellite.json"
pathToFile = "/Users/brayancruz/Documents/GitHub/class-python-test1/gladysSatellite/altitude-satellite.json"

try:
    jsonFile = open(pathToFile, 'r')
except OSError:
    print("ERROR: Unable to open the file %s" % pathToFile)
    exit(-1)

time = json.load(jsonToFile)
longtitude = json.load(jsonToFile)
latitude = json.load(jsonToFile)
altitude = json.load(jsonToFile)



