# HW 8.1 Python Individual
#File: HW8_1_Task1_functions_Tillmaaa.py
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
#Calculates the Paralllel and Series resistance of two integers


listA = eval(input('Please enter vector A: '))
listB = eval(input('Please enter vector B: '))
if len(listA) == len(listB) : 
	x = listA[0] * listB[0]
	x = x + listA[1] * listB[1]
	x = x + listA[2] * listB[2]
	print("The dot product of vector A and vector B is",x)
else :
	print("both vectors should be a length of 3")
