# HW 8.1 Python Individual
#File: HW8_1_Task1_Tillmaaa.py
#Date:		28 Oct 2018
#By: 		Alex Tillman
#
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
#This is the main program from task 1 of the python homework


def main():
	from HW8_1_Task1_functions_Tillmaaa import pResistance,sResistance
	a = float(input("input first resistance value: "))
	b=  float(input("input second resistance value: "))
	pResistance(a,b)
	sResistance(a,b)