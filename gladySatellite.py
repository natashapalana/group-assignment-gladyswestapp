 

"""

    Student: Nof Mohammed

    Module: gladysSatellite

    Description: This module does Opens and reads any of the four data files from disk based on the satellite name given to readSat function.

•   Reads latitude, longitude, altitude, and time information into data structures.

•   Returns the data that was read to the gladysUserInterface module

 …

 """

 

import json

import os

 

def readSat(sat, pathToJSONDataFiles):

    fileName = sat + "-satellite.json"

    filePath = os.path.join(pathToJSONDataFiles, fileName)

 

    try:

        with open(filePath, 'r') as fileHandle:

            data = json.load(fileHandle)

    except IOError:

        print("ERROR: Unable to open the file " + filePath)

        raise IOError

 

    satellite_data = {}

 

    for entry in data:

        lat, long = entry['latitude'], entry['longitude']

        satellite_data[(lat, long)] = {

        'altitude': entry['altitude'],

        'time': entry['time']

    }

 

    return satellite_data

 

def gpsValue(x, y, sat):

    pathToJSONDataFiles = "C:/Users/sjccuser/OneDrive/Documents/GitHub/gladysSatellite"

 

    satellite_data = readSat(sat, pathToJSONDataFiles)

 

    for coordinates, data in satellite_data.items():

        if coordinates == (x, y):

            return data

 

    return None
