#Task 1 - Print your pet's type and name using an f-string
pet_type = "cat"
pet_name = "Matilda"
print(f"I have a {pet_type} and her name is {pet_name}.\n")

#Task 2 - Use input statements to take input and an f-string to print the results as shown
name = input("Enter your first name: ")
age = input("Enter your current age: ")
savings = input("Enter your yearly savings: ")
print(f"Hello {name}! You are currently {age} years old.\n\nIn 10 years, you will be 30 years old.\n\nIf you save ${savings} each year, in 5 years you will have saved $6000.\n\nYour average monthly savings is $100.00.\n")

#Task 3 - Use an f-string to print out the number of seconds in the current month. Have Python do the multiplication
days_in_Jan = 31
hrs_in_1day = 24
sec_in_1hour = 3600
sec_in_Jan = (days_in_Jan * hrs_in_1day * sec_in_1hour)
print(f"The number of seconds in January is {sec_in_Jan}\n")

#Task 4 - Use the // operator for integer division and % for the integer remainder. Use an f-string to print the result
eggs = input("Enter the number of eggs: ")
num_dozen = int(eggs) // 12
residual = int(eggs) % 12
print(f"This makes {num_dozen} dozen eggs with {residual} left over")