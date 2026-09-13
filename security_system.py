from gpiozero import Button

currentState = "DISARMED"


reed_switch = Button(17)

#function to tell the door has been opened
def doorOpened():
	global currentState

	
     #if we are in ARMED mode 
	if currentState == "ARMED":
		print("Door Opened")
		currentState = "ALARMING"
		print("ATTN ALARMING")

reed_switch.when_released = doorOpened


#security system is active
securitySystem = "RUNNING"
#---------------------BEGIN LOOP-------------------------
while securitySystem == "RUNNING":
	
	if currentState == "DISARMED": 
		print("DISARMED")
		#ask for arm code and store in variable
		arm_code = input("Please enter the arm code:")
		#if the code is correct 
		if arm_code == "999":
		#new state is armed
			currentState = "ARMED"
			print("ARMED")
		#if code is not correct prompt user for code again
		else: 
			print("Invalid arm code.") 	
	# if we are in alarm mode
	if currentState == "ALARMING":
			# prompt user to put in the disarm code
			disarm_code =input("Please enter the disarm code: ")
			# if the disarm code is correct
			if disarm_code == "999":
				# show we are disarmed
				print("DISARMED")
				currentState = "DISARMED"
	#---------------------------------END LOOP------------------------------

  


