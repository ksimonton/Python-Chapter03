#Katelyn Simonton - Python Chapter 3 Exercise 2 - 2/23/2018

#Exercise 2: Rewrite your pay program using try and except so that your program handles 
#non-numeric input gracefully by printing a message and exiting the program. The following 
#shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input
try:
	hours = int(input("Enter Hours: "))
	rate= float(input("Enter Rate: "))
	hourly = float(int(hours) *1.5)
	pay = float(int(hourly *rate))
	print ("Pay: " + str(pay))
except ValueError:
	print("Error, please enter numeric input.")
	exit()