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
elif gpa < 4 and gpa >=3.5 :
	print("Highest honors for semester")
elif gpa >4 :
	print("Error: Invalid GPA")
else :
	print("Error: Invalid GPA")
