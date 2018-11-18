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
#Calculates a persons age in years and age in minutes 

def main():
	lastName = (input("Enter your last name: "))
	firstName = (input("Enter your first name: "))
	age = int(input("Enter your age in whole years: "))
	days = int(input("Enter the days since your last birthday: "))
	year = 365.242199
	day = 24
	minutes = 60
	ageInYears = age + days/year
	ageInMinutes = ageInYears *year *day *minutes
	print (firstName,lastName)
	print("you are", ageInYears, "years old")
	print("you are", int(ageInMinutes), "minutes old")
