# Activity 8.2.1: Task 3
#File: ACT8_2_Task3_Team256.py
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
#This program outputs the remainder of dividing two integers 

def modulus(a,b):
	c = a//b 
	d = c*b
	e = a-d
	print("the remainder is", e)
	
def main():
	a = int(input("Enter a value:"))
	b = int(input("Enter b value:"))
	modulus(a,b)