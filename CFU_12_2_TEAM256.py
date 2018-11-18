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

def cfu(n):
	sum = 0
	if n < 0:
		for num in range(0-n,0,-1):
			sum = (num*-1) + sum
			print(num*-1)
		print("The sum of the sequence is", sum)
	else:
		for num in range(0-n,0+1):
			sum = (num*-1) + sum
			print(num*-1)
		print("The sum of the sequence is", sum)
