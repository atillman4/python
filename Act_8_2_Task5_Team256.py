# Activity 8.2.5: Task 5
#File: ACT_8_2_Task5_Team256.py
#Date:		18 Oct 2018
#By: 		Alex Tillman
#			Justin Kohler
#			Ryan Steffan 
#			David McCoy
#
#Section:	021
#Team 		256
#
#Electronic Signature
#	Alex Tillman
#	Justin Kohler
#	Ryan Steffan 
#	David McCoy
#This electronic signature above indiccates the script
#submitted for evaluation is my individual work, and i 
#ahve a general understanding of all aspects of its 
#development and execution
#
#A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
#This program outputs the area of a circle given two inputs

def areaOfCircle(r):
	import math
	area = math.pi*r**2
	print("Area of circle:",area)
def main():
	x = int(input("enter radius:"))
	areaOfCircle(x)
	
