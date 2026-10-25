from gpiozero import OutputDevice
from time import sleep

buzzer = OutputDevice(27)

print("Buzzer ON")
buzzer.on()
sleep(1)

print("Buzzer OFF")
buzzer.off()

buzzer.close()
