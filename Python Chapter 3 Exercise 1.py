#Katelyn Simonton - Python Chapter 3 Exercise 1 - 2/23/2018

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours 
#worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0


hours = int(input("Enter Hours: "))
rate= float(input("Enter Rate: "))
hourly = float(int(hours) *1.5)
pay = float(int(hourly *rate))
print ("Pay: " + str(pay))
