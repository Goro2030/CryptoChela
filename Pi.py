
# Pi.py: Pi and connected devices Hardware API
# This Python script interfaces with hardware connected to a Raspberry Pi. 
# The hardware includes a flow sensor and a valve, and the script provides functionality to 
# open/close the valve and keep track of the number of flow events detected by the flow sensor.
# If the script is run on a device that isn't a Raspberry Pi, it won't crash but rather bypass the hardware control functionalities.

__author__ = "Mariano Silva"
__credits__ = ["Alexis Lanado", "Eduardo Schoenknecht", "Felipe Borges Alves", "Paulo Eduardo Alves"]

# Flag to determine if the code is being run on a Raspberry Pi
use_rPi = False

# Attempt to import the Raspberry Pi GPIO library
try:
    import RPi.GPIO as GPIO
    use_rPi = True  # if the import is successful, set use_rPi to True
except ImportError:  # if the import fails, print an error message
    print("This is not a raspberry Pi")

# Define the pin numbers for the valve and flow sensor
valve = 40
FlowSensor = 11

# Initialize flow counter and valve state
flow_counter = 0
valve_opened = False

# Function to set up the GPIO pins
def init_hardware():
    if use_rPi:  # if this is a Raspberry Pi
        GPIO.setmode(GPIO.BOARD)  # use board pin numbering
        GPIO.setup(valve, GPIO.OUT, initial=GPIO.LOW)  # initialize the valve pin as an output, initially low
        GPIO.setup(FlowSensor, GPIO.IN)  # initialize the flow sensor pin as an input
        GPIO.add_event_detect(FlowSensor, GPIO.BOTH, handleFlow)  # set up an event handler for the flow sensor

# Event handler for the flow sensor
def handleFlow(pin):
    global flow_counter
    if pin == FlowSensor:  # if the pin that triggered the event is the flow sensor
        flow_counter += 1  # increment the flow counter

# Function to open the valve
def open_valve():
    global valve_opened
    if use_rPi:  # if this is a Raspberry Pi
        GPIO.output(valve, GPIO.HIGH)  # set the valve pin high
    valve_opened = True  # update the valve state

# Function to close the valve
def close_valve():
    global valve_opened
    if use_rPi:  # if this is a Raspberry Pi
        GPIO.output(valve, GPIO.LOW)  # set the valve pin low
    valve_opened = False  # update the valve state

# Function to clean up the GPIO pins
def cleanIO():
    if use_rPi:  # if this is a Raspberry Pi
        GPIO.cleanup()  # clean up the GPIO pins
