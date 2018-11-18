# Activity 12.2: Task 2
#File: ACT_12_Fibbonacci.py
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

def myFib(n):
	initial = 0
	if n < 0 or n%1 !=0 :
		print("Invalid entry- number must be non-negative integer")
	else	:
		fibList = [0]
		digit1 = initial # 0
		digit2 = 1
		for num in range(initial,n-1): #0 to 13
			digit1,digit2 = digit2,digit1+digit2
			fibList.append(digit1)  # 0 + 1 
			print (fibList)
