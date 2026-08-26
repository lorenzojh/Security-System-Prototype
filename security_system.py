from gpiozero import Button

currentState = "DISARMED"
button = Button(17)

securitySystem = "RUNNING"

while securitySystem == "RUNNING":


	if currentState == "DISARMED": 
		print("DISARMED")

		arm_code = input("Please enter the arm code:")

		if arm_code == "999":
			currentState = "ARMED"
		else: 
			print("Invalid arm code.") 
	if currentState == "ARMED":
		print("ARMED")
		if button.is_pressed: 
			currentState = "ALARMING"
			print("ATTN ALARMING!!")
	if currentState == "ALARMING":
		disarm_code =input("Please enter the arm code: ")
		if disarm_code == "999":
			print("DISARMED")
			currentState = "DISARMED"

  


