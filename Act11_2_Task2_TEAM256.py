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
gpa = float(input("Enter your gpa up to one decimal point: "))

if	gpa < 0:
	print("Error: Invalid GPA")
elif gpa < 1 and gpa >0 :
	print("Faile semester- registration")
elif gpa < 2 and gpa >=1 :
	print("On probation for next semester")
elif gpa < 3 and gpa >=2 :
	print("Pass")
elif gpa < 3.5 and gpa >=3 :
	print("Dean's list for semester")
elif gpa <= 4 and gpa >=3.5 :
	print("Highest honors for semester")
elif gpa >4 :
	print("Error: Invalid GPA")
else :
	print("Error: Invalid GPA")
