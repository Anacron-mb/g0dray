#!/usr/bin/python

import os
import subprocess
import sys
import argparse
import time

MAX_BRIGHTNESS = 100    # Highest brightness (there is no cap with xrandr)
MIN_BRIGHTNESS = 0      # Lowest brightness (0 means pitch black)
DEFAULT_TIME = 0.2      # Default -time value, don't change if you want a true clone of xbacklight
DEFAULT_STEPS = 20      # Default steps, leave 20 if you want a true clone of xbacklight 

# Parser for command line options
parser = argparse.ArgumentParser()
actiongroup = parser.add_mutually_exclusive_group() 

actiongroup.add_argument('-set', metavar='percent', help='Sets brightness to the specified level.')
actiongroup.add_argument('-inc', metavar='percent', help='Increases brightness by the specified amount.')
actiongroup.add_argument('-dec', metavar='percent', help='Decreases brightness by the specified amount.')
actiongroup.add_argument('-get',action='store_true',help='Print out the current backlight brightness of each output with such a control. The brightness is represented as a percentage of the maximum brightness supported. ')

parser.add_argument('-steps', metavar='number', help='Number of steps to take while fading. Default is 20')
parser.add_argument('-time', metavar='milliseconds', help='Length of time to spend fading the backlight between old and new value. Default is 200.')
parser.add_argument('-help',help='Print out a summary of the usage and exit.',action='help')
parser.add_argument('--version', action='version', version='%(prog)s 0.7.1')

args = parser.parse_args()

# Get screen identifier
commandToGetScreen = "xrandr --listmonitors | grep \"^ \" | cut -f 6 -d' '"
screen = subprocess.check_output(commandToGetScreen, shell=True)
screen = screen.rstrip() # strips away /n at the end of the line

# Get current brightness 
commandToGetCurrentBrightness = "xrandr --verbose | grep Brightness | cut -f 2 -d' '"
brightness = subprocess.check_output(commandToGetCurrentBrightness, shell=True)
brightness = float(brightness.rstrip())

# Check first if no arguments are supplied
if len(sys.argv) == 1:
    print "No arguments supplied. Use -h or --help or -help to get more information."

timeBetweenChanges = DEFAULT_TIME
stepsToTake = DEFAULT_STEPS

if args.steps:
    try:
        stepsToTake = int(args.steps)
    except ValueError:
        print args.steps + " is not a valid number. Aborting."
        sys.exit(2)

    if stepsToTake > 35:
        print "A lot of steps can slow down the application, thus making -time unpredictable even if it set.." 

if args.time:
    try:
        timeBetweenChanges = float(args.time)/1000.000  # Convert to milliseconds
    except ValueError:
        print args.time + " is not a valid type of time (milliseconds). Aborting"
        sys.exit(2)

# Function used to change brightness in every case
def set_brightness(newbrightness):

    if newbrightness < (MIN_BRIGHTNESS/100.00):
        print "Cannot set brightness to " + str(newbrightness*100) + ",the value is too low."
        print "Setting brightness to " + str(MIN_BRIGHTNESS) + ". "
        newbrightness = MIN_BRIGHTNESS/100.00

    if newbrightness > (MAX_BRIGHTNESS/100.00):
        print "Cannot set brightness to " + str(newbrightness*100) + ",the value is too high."
        print "Setting brightness to " + str(MAX_BRIGHTNESS) + ". "
        newbrightness = MAX_BRIGHTNESS/100.00

    if newbrightness == brightness:
        sys.exit(0)
    elif newbrightness < brightness:
        brightdifference = brightness - newbrightness
        for step in range(1,stepsToTake+1):
            time.sleep(timeBetweenChanges/stepsToTake)
            os.system("xrandr --output " + screen + " --brightness " + str(brightness - ((brightdifference/stepsToTake)*step)))

    else:
        brightdifference = newbrightness - brightness
        for step in range(1,stepsToTake+1):
            time.sleep(timeBetweenChanges/stepsToTake)
            os.system("xrandr --output " + screen + " --brightness " + str(brightness + ((brightdifference/stepsToTake)*step)))
            
    sys.exit(0)

if args.set:
    
    try:
        brightnessToSet = float(args.set)/100.00
    except ValueError:
        print args.set + " is not a valid percent. Aborting."
        sys.exit(2)
        
    set_brightness(brightnessToSet)
    

if args.inc:
    try:
        brightnessToSet = float(brightness) + float(args.inc)/100.00
    except ValueError:
        print args.inc + " is not a valid percent. Aborting."
        sys.exit(2)

    set_brightness(brightnessToSet)
    
if args.dec:
    try:
        brightnessToSet = float(brightness) - float(args.dec)/100.00
    except ValueError:
        print args.dec + " is not a valid percent. Aborting."
        sys.exit(2)

    set_brightness(brightnessToSet)    

if args.get:
    
    percentbrightness = float(brightness)*100.00
    print "Current brightness is set at: " + str(percentbrightness)

    sys.exit(0)

sys.exit(0)     # Exits the right way
