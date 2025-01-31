#Task 1 - Define a function that returns the average of 3 numbers
def average(num1, num2, num3):
    """Take the average of three numbers"""
    return (num1 + num2 + num3) / 3

print (average(10, 20, 30))

#Task 2 - Move the function definition after the print statements
#This script will not work because the function has yet to be defined

#Task 3 - Print out the value of a parameter outside a function definition
#This script will not work because num1 is not defined

#Task 4 - Define a function that converts a dog's age into human years
def dog_to_human_age(dog_age):
    """This function takes the age of a dog and estimates its human age"""
    return dog_age * 7

dog1 = 10
dog2 = 3
print (f'{dog1} dog years is analogous to {dog_to_human_age(dog1)} human years')
print (f'{dog2} dog years is analogous to {dog_to_human_age(dog2)} human years')

#Task 5 - Define a function that will calculate the value of a car
def car_value(purchase_price, car_age):
    """Output a car's value depending on its type, age, and purchase price."""
    if car_type == "German":
        return purchase_price - .05*purchase_price*car_age
    elif car_type == "Japanese":
        return purchase_price - .07*purchase_price*car_age
    elif car_type == "Italian":
        return purchase_price + .05*purchase_price*car_age
    else:
        return "unknown"

purchase_price = int(input('Enter the purchase price of a car without the $ sign: '))
car_age = int(input('How old is the car in years?: '))
car_type = input('Is the car German, Japanese, or Italian?: ')

print(f'The value of the {car_type} car will be ${car_value(purchase_price, car_age)} after {car_age} years.')

#Task 6 - Define a function that converts a dog's age into human years and returns the result
def dog_to_human_years(dog_years):
    """This function takes the age of a dog from user input and estimates its human age"""
    return dog_years * 7

dog_name = input("Please enter your dog's name: ")
dog_years = int(input("Please enter your dog's age in years: "))
print(f'Your {dog_name} is {dog_to_human_years(dog_years)} human years old.')

#Task 7 - Calculate the price of an ice cream cone
def cone_price(scoops):
    """This function will calculate the price of an ice cream cone"""
    return scoops*1.15+2.25

scoops = int(input("How many scoops would you like: "))
print(f'A {scoops}-scoop cone will cost ${cone_price(scoops):.2f}')