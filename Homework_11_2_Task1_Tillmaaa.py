# HW 11.2 Python Individual
#File: Homework_11_2_Task1_Tillmaaa.py
#Date:		28 Oct 2018
#By: 		Alex Tillman
#Team 		256
#
#Electronic Signature
#	Alex Tillman
#
#
#
#This electronic signature above indiccates the script
#submitted for evaluation is my individual work, and i 
#ahve a general understanding of all aspects of its 
#development and execution
#
#A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
#Calculates the refraction distance of a single light through two mediums

import math
#input
refraction = eval(input("Enter indices of refraction for bottom two media: "))
angle = float(input("Enter angle of incidence (in degrees): "))
distance = eval(input("Enter d1 and d2 (units):"))
#calculate angles
sinAngle =  math.sin(math.radians(angle))
sinAngle2 = (refraction[0]*sinAngle)/refraction[1]
if sinAngle > 1 or sinAngle2 > 1 :
        print("Error, no refraction in the second media")
else : 
        angle2 = math.degrees(math.asin(sinAngle2))
        critAngle = math.degrees(math.asin(refraction[0]/refraction[1]))
        #calculate distances                      
        x = math.tan(math.radians(angle)) * distance[0]
        y = math.tan(math.radians(angle2)) * distance[1]
        d4 = x + y 
        print("Ending distance is: ")
        print(round(d4,4))
