# HW 11.2 Python Individual
#File: Homework_11_2_Task2_Tillmaaa.py
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
#Calculates the Paralllel and Series resistance of two resistors, then
# it calculates the votlage and current based on either type of resistance
from HW8_1_Task1_functions_Tillmaaa import pResistance,sResistance
resistor = eval(input("Enter two resistor values seperated by comma: "))
voltageSource = float(input("Enter the power of the volage source driving the circuit :"))
type = input("Is this a series or a parallel? :")
pTotal = float(pResistance(resistor[0],resistor[1]))
sTotal = float(sResistance(resistor[0],resistor[1]))
volt1 = (resistor[0]/(resistor[0] + resistor[1]))*voltageSource
volt2 = (resistor[1]/(resistor[0] + resistor[1]))*voltageSource
s_current = voltageSource/sTotal
p_currentTotal = voltageSource/pTotal
p_current1 = (resistor[1]/(resistor[0] + resistor[1]))*p_currentTotal
p_current2 = (resistor[0]/(resistor[0] + resistor[1]))*p_currentTotal
pVolt = voltageSource
if	resistor[0] < 0  or resistor[1] <0 :
	print("Error resistor values must be non negative")
	sys.exit()
elif type == "series":
	print("Total combined resistance : ", sTotal)
	print("Voltage: ")
	print("		Resistor 1: ", round(volt1,4), "volts")
	print("		Resistor 2: ", round(volt2,4), "volts")
	print("Current: ")
	print("		Resistor 1: ", round(s_current,4))
	print("		Resistor 2: ", round(s_current,4))
elif type == "parallel":
	print("Total combined resistance : ", pTotal)
	print("Voltage: ")
	print("		Resistor 1: ", voltageSource, "volts")
	print("		Resistor 2: ", voltageSource, "volts")
	print("Current: ")
	print("		Resistor 1: ", round(p_current1,4))
	print("		Resistor 2: ", round(p_current2,4))
else:
	print("unexpected error. Please try again ")
	sys.exit()
	
