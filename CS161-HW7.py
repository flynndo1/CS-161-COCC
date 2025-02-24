#Task 1 - Write a for or while loop that prints out all the even numbers between two numbers that the user inputs
def even_nums(l, h):
    """This function prints the even numbers between low and high (inclusive) specified by the user"""
    for num in range(low, high+1):
        if num % 2 == 0:
            print(num)

low = int(input("Enter low number: "))
high = int(input("Enter high number: "))
even_nums(low, high)

#Task 2 - Write a while loop that prints out all the factors of a given positive integer
def calc_factors(num):
    """This will determine the factors of a positive integer"""
    factors = [] #This array will be used to store the factors so it can be printed after the loop finishes
    i = 1
    while i <= num:
        if num % i == 0: #Checks if "i" is a factor
            factors.append(i)
        i += 1
    return factors

number = int(input("Enter a positive integer: "))
factors = calc_factors(number)
print(f"The factors of {number} are {factors} ")

#Task 3 - Write a program that uses iteration to calculate the sum of the numeric position of the letters of your last name
def sum_name(name):
    """This function will use the indexes from the alphabet list to provide a total sum for a given name"""
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    sum = 0 #Initializing the sum to start with 0
    for letter in name.lower(): #Convert the name to lowercase
        sum += alphabet.index(letter) #Add the letter's index to the sum
    return sum

name = input("Enter your surname: ")
print(f"The sum of the numeric positions in the name {name} is: {sum_name(name)}")

#Task 4 - Write a recursive function to print the squares of integers up to an input number
def squares(input_num):
    """This will print the squares of integers up to and including input_num"""
    if input_num < 1:
        return
    squares(input_num - 1)
    print(input_num * input_num)

input_num = int(input("Enter a number for the squares function: "))
squares(input_num)

#Task 5 - Write a sort that will create a teepee of the numbers from an unsorted list
#The largest # will be centered with odd #s in ascending order to the left of center, even #s in descending order to the right
def teepee_create(unsorted_list):
    """This function will sort a list so that the largest # will be in the middle, odd #s in ascending order to its left, and even #s in descending order to its right."""
    #This first step will find the max value and remove it temporarily
    max_num = max(unsorted_list)
    unsorted_list.remove(max_num)

    #Next the odd and even numbers are separated and sorted
    odds = sorted([num for num in unsorted_list if num % 2 != 0])
    evens = sorted([num for num in unsorted_list if num % 2 == 0], reverse=True)

    #The numbers can now be combined into the final sorted list
    teepee = odds + [max_num] + evens
    return teepee

unsorted_list = [12,43,22,34,2,21,3,33,81]
sorted_list = teepee_create(unsorted_list)
print(sorted_list)

#Task 6 - Not clear to me what is being asked