# Raspberry Pi Security System

This is a Raspberry Pi security system prototype I’m building as a hands-on way to learn more about Python, GPIO, Linux, and how hardware and software interact.

The project started out very simple with a button connected to the Raspberry Pi, mainly so I could understand how GPIO inputs work and how the Pi reads HIGH and LOW signals. From there I moved to using a reed switch module so the system can detect when a door opens or closes.

## Current Features

Right now the system can:

- Start in a `DISARMED` state
- Arm the system using a code
- Detect when the door opens using a reed switch
- Change from `ARMED` to `ALARMING` when the door opens
- Turn on an active buzzer when the alarm is triggered
- Disarm the system using the correct code
- Turn off the buzzer when the system is disarmed

The main system states are:

- `DISARMED`
- `ARMED`
- `ALARMING`

The reed switch is connected to GPIO17 and is used to simulate a basic door sensor. When the magnet is close to the reed switch, the door is treated as closed. When the magnet moves away, the program detects that event and can trigger the alarm if the system is armed.

## What I’m Learning

A big goal of this project is just getting more comfortable with how software actually controls and responds to physical hardware.

So far I’ve worked with:

- Raspberry Pi GPIO
- GPIO numbering
- HIGH and LOW signals
- Pull-up resistors
- Ground and 3.3V connections
- Python conditionals and loops
- Functions
- State machines
- Event handling
- Variable scope
- SSH
- Linux terminal commands
- Git and GitHub
- Debugging hardware and software together

## Hardware

Right now I’m using:

- Raspberry Pi
- SunFounder starter kit
- Reed switch and magnet
- Breadboard
- Active Buzzer
- 5850 Transistor
- 1kΩ Reisistor
- Jumper wires

Current reed switch wiring:

- `VCC` → Raspberry Pi `3.3V`
- `GND` → Raspberry Pi `GND`
- `DO` → Raspberry Pi `GPIO17`

The GPIO Input uses a pull-up resistor, allowing the Pi to detect the reed swith state changes as the door opens and closes.

## Buzzer

The active buzzer is controlled using "GPIO27". A transistor is used so the GPIO pin controls the buzzer without directly powering it. 

The transistor switches power to the buzzer when the system enter the 'ALARMING' state. 
## Future Plans

I want to keep building this out slowly and eventually make it feel more like a real security system.

Some things I want to add are:

- Motion sensor
- LEDs for system status
- Physical keypad for arming and disarming
- Web dashboard
- Door and sensor status
- Event history
- Notifications
- Camera integration

This is still an early prototype, but the main goal is to keep adding features while understanding how each part works.
