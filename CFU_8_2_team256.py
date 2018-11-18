# Activity 8.2.1: CFU
#File: CFU_8_2_team256.py
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
#This program outputs the surface area of a cylinder given the diameter and height

def surAreaCyl(d,h):
	import math
	surfaceArea = ((2*math.pi*((d/2)**2)) + (2*math.pi*(d/2)*h))
	print ("The surface area of a cylinder is", surfaceArea, "cm^2 for a given diameter of ", d, "cm and height of", h, "cm")
	
def main():
	d = int(input("Insert diameter (in cm): "))
	h = int(input("Insert height (in cm): "))
	surAreaCyl(d,h)
	