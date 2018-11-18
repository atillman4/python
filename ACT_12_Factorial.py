# Activity 12.2: Task 1
#File: ACT_12_Factorial.py
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
#
#
#
#This electronic signature above indiccates the script
#submitted for evaluation is my individual work, and i 
#ahve a general understanding of all aspects of its 
#development and execution
#
#A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
#This take the factorial of a number n 


print("Use myFactorial(integer) function") 
def myFactorial(n) : 
	factorial = 1
	if n < 0 or n%1 !=0 :
		print("Invalid entry- number must be non-negative integer")
	else	:
		for num in range(0,n):
			factorial = (n-num) * factorial
		print('%d ! = %d'%(n,factorial))
		

		
		
