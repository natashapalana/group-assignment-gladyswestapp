
import io
import gladysWestLogin 
import gladysCompute 
import gladysSatellite 


# This UserInterface present a text-based menu for users to interact with the app by Natasha Palana

def runTests():
	"""
	Tests some module functions
	"""

	print("running a few tests")

# When type "t" --- test gladysUserLogin.login()

	userName = gladysWestLogin.login()
	print("Your userName: ", userName)

# When type "t" --- test gladysSatellite.readSat()

	satData = gladysSatellite.readSat()
	print("Satellite Data: ", satData)

# When type "t" --- test gladysUserLogin.login()

a = 10
b = 20 
sat = "GPS"
average = gladysCompute.gpsValue(a, b, sat)
print("GPS value for " + str(a) + ", " + str(b) + " is " + str(average))

print("Module tests complete!")

#runApp(userName, sat, result)


def start():
	"""
		logs the user in, and runs the app

	"""
# Login the user

	userName = gladysWestLogin.login()
	print("Your userName: ", userName)
	runApp(userName)

# read the satellite data

	satData = gladysSatellite.readSat()
	print("Satellite Data: ", satData)



def runApp(userName, satData):
	"""
		runs the app
	"""
	current_position = None
	destination_position = None

	# loop until user types q
	userQuit = False
	while (not userQuit):

		# menu choices
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("Hi user!")
		print(">> Welcome to the Gladys West Map App <<")
		print("Type 'c' to set your current position")
		print("Type 'd' to set your destination position")
		print("Type 'm' to navigate that tells the distance")
		print("Type 't' to run module tests")
		print("Type 'q' to quit the app")
		print()

		# get first character of input
		userInput = input("Please a command to run the app:")
		lowerInput = userInput.lower()
		letter_choice = lowerInput[0:1]

		#  if-elif control structure when the user type the command

		# quit --- 'q'
		if letter_choice == 'q':
			userQuit = True

		# run module tests --- 't' 
		elif letter_choice == 't':
			runTests()
		
		# navigate that tells the distance --- 'm'
		elif letter_choice == 'm':
			if current_position is None or destination_position is None:
				print("Please type your current and position destination first.")
			else:
				distance = compute_distance(current_position, destination_position)
				print("The distance between current position", current_position, "and destination position", destination_position, "is", round(distance, 2), "units.")
		
		# destination position --- 'd
		elif letter_choice == 'd':
			current_position = get_position("current")
		
		#current position  --- 'c'
		elif letter_choice == 'c':
			destination_position = get_position("destination")
		
		else:
			print("ERROR: " + letter_choice + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")

# At the end, user can put their inputs and it will generate well by Natasha Palana

#Angelline's code here below:
userQuit = False

while (not userQuit):

    #menu

    print("\n")
    print("-------------------------------")

    print("Welcome to Gladys West Map App")

    print("-------------------------------")

    print("Current position     : x = 56 , y = 13")

    print("Destination position : x = 98 , y = 2")

    print("Distance             : 607.87")
    print("\n")

    print("[c] to set current position")

    print("[d] to set destination position")

    print("[m] to map - which tells the distance")

    print("[t] to run module tests")

    print("[q] to quit")

    print()

        # get first character of input

    userInput = input("Enter a command:")

    lowerInput = userInput.lower()

    firstChar = lowerInput[0:1]

        # menu choices, use a switch-like if-elif control structure

    if firstChar == 'c' or firstChar == 'd':

        xCurrent = int(input("Enter a x position: "))

        yCurrent = int(input("Enter a y position: "))

        xDestination = int(input("Enter a x position: "))

        yDestination = int(input("Enter a y position: "))
        distance=((((xDestination - xCurrent )**2)+((yDestination-yCurrent)**2))**0.5)
        print(distance)
        break

    elif firstChar == 'm':

        print(distance)
        break

        # quit

    if firstChar == 'q':

        userQuit = True

        # run some tests (this is part 1 of 2)

    elif firstChar == 't':

        runTests()

    else:

        print("ERROR: " + firstChar + " is not a valid command")

print("\n")

print("Thank you for using the Gladys West Map App!")

print("\n")

def compute_distance(current_position, destination_position):

	"""
	computes the distance between two positions
	"""
	# TODO: implement this function
	pass


def get_position(position_type):

	"""
	gets the position from the user
	"""
	# TODO: implement this function
	pass
