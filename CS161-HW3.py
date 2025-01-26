#Task 1 - Ask the user to enter their name. Then say hello and repeat their name
name = input("What is your name? ")
print("Hello, " + name)

#Task 2 - Ask the user to enter their age. Print out their age 5 years from now
#If the code takes the form: age = input("What is your age? ")
#print(age+5)
#The preceding two lines of code will give an error because Python won't add an integer to a string element
age = int(input("What is your age? "))
print(f"In five years you will be {age+5} years old.")

#Task 3 - Use concatenation and str() to print a message telling the user how old they will be in y years
how_old = int(input("How old are you? "))
years = int(input("How many years to add to your age? "))
future_age = how_old + years
print("In " + str(years) + " years you will be " + str(future_age) + " years old.")

#Task 4 - Ask the user to enter values that might be floating point
hours_worked = float(input("Enter the number of hours worked: "))
hourly_wage = float(input("Enter your hourly wage without the $: "))

#Task 5 - Print out the result of the calculation in a single print statement, using concatenation
weekly_wage = (hours_worked * hourly_wage)
annual_wage = int(weekly_wage * 50)
print(f"Your gross pay this week is ${weekly_wage:.2f}\nYour estimated annual gross pay will be ${annual_wage:,d}")
