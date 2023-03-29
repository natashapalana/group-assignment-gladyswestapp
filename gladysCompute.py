import io
import gladysSatellite as satellite

"""
	Student: Tamrin Bains
	Module: gladysCompute
	Description: This module computes the distance between two points: destination and current coordinates
"""

#gpsAverage(1,2)

def gpsAverage(x, y):
	"""
		This program will pull all values for specified X and Y values
		from the 4 satellite JSON files and then average the 4 pulled values
	"""
	value = 0.0 # initialize value
	
	# If x or y are negative, then turn them positive
	if(x<0):
		x = -x
		print("X was negative, Corrected!")
	if(y<0):
		y =-y
		print("Y was negative, Corrected!")

	x1 = satellite.gpsValue(x, y, "latitude")
	value1 = value # value is output of above function, store it in value1
	x2 = satellite.gpsValue(x, y, "longitude")
	value2 = value # value is output of above function, store it in value2
	x3 = satellite.gpsValue(x, y, "altitude")
	value3 = value # value is output of above function, store it in value3
	x4 = satellite.gpsValue(x, y, "time")
	value4 = value # value is output of above function, store it in value4

	average = (value1+value2+value3+value4)/4
	print("Average value from the 4 JSON files = ", average)

	return average


def distance(xi,yi,xf,yf):
	"""
	Inputs will be 2 points (Xi,Yi) as current coordinates
	and 2 points (Xf,Yf) as destination coordinates
		Xi is the x coordinate of current point
		Yi is the y coordinate of current point
		Xf is the x coordinate of destination point
		Yf is the y coordinate of destination point
		Calculate the distance between Current and Destination coordinates
	"""
	# Calculating distance between initial x,y and destination x,y
	distance = [(xi-xf)**2+(yi-yf)**2]**(0.5)
	print("Distance between Curernt and Destination = ", distance)

	return distance