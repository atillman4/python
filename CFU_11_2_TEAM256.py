# HW 8.1 Python Individual
#File: HW8_1_Task1_functions_Tillmaaa.py
#Date:		28 Oct 2018
#By: 		Alex Tillman
#			Justin Kohler
#			Ryan Steffen
#			David McCoy
#Section:	021
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
#Calculates a persons age in years and age in minutes 

dList = eval(input("What are the values for A, B and C: "))
Det = dList[1]**2 - (4*dList[0]*dList[2])
if Det < 0 :
	print ("There are no real roots")
elif Det == 0:
	print("There is one real root")
elif Det >0 :
	print("There are two real roots")
