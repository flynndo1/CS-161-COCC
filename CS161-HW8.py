# Task 1 - String operations create a new string based on the first
def phrase_check(phase1, phase2):
    """This function checks whether the 2nd phrase is the same phrase as the 1st, only in uppercase letters."""
    if phase1.upper() == phase2:
        print("Stop shouting please!")
    else:
        print("These phrases are not the same.")
phrase1 = input("Enter a phrase: ")
phrase2 = input("Enter the same phrase in all caps: ")
phrase_check(phrase1, phrase2)

# Task 2 - Counting the number of different vowels in a string and printing the total
def vowel_count(string):
    """This function returns the number of different vowels in a string."""
    vowels = {"a", "e", "i", "o", "u"}
    found_vowels = set() #Stores unique vowels found in the string
    for letter in string.lower(): #Converts the string to lowercase since the stored vowels are lowercase
        if letter in vowels:
            found_vowels.add(letter) #Add the vowel to found_vowels
    print(f"{string} has {len(found_vowels)} different vowels.")

string = input("Enter a string for vowel counting: ")
vowel_count(string)

# Task 3 - Store two different strings, then print them out in alphabetical order
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if string1 < string2:
  print(f"{string1} comes before {string2}")
else:
  print(f"{string2} comes before {string1}")

# Task 4 - Get a user to enter the same email address twice
def email_check():
    """email_check will verify the user's email address by ensuring both strings are matched"""
    em1 = input("Enter your email address: ")
    em2 = input("Enter your email address again: ")
    while em1 != em2:
        print("The two emails do not match")
        em1 = input("Enter your email address: ")
        em2 = input("Enter your email address again: ")

    print("Thank You!")

email_check()

# Task 5 - Write an iterative and recursive function and compare the time needed to print the factorial of a number
import time

def iterative_factorial(n):
    """Returns the factorial of n using iteration"""
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


def recursive_factorial(n):
    """Returns the factorial of n using recursion"""
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def factorial_eval(numbers):
    """Returns the factorial of a list of numbers and measures execution time for both methods"""
    for n in numbers:

        # Measure time for iterative factorial
        start_time = time.perf_counter_ns()
        iterative_result = iterative_factorial(n)
        end_time = time.perf_counter_ns()
        iterative_time = end_time - start_time

        # Measure time for recursive factorial
        start_time = time.perf_counter_ns()
        recursive_result = recursive_factorial(n)
        end_time = time.perf_counter_ns()
        recursive_time = end_time - start_time

        # Print results
        print(f"The factorial of {n} is:")
        print(f"  - Iteratively found to be {iterative_result} (Time: {iterative_time} nanoseconds)")
        print(f"  - Recursively found to be {recursive_result} (Time: {recursive_time} nanoseconds)")

# List of numbers to evaluate
numbers = [3, 10, 25]
factorial_eval(numbers)

# When this code is executed the recursion function is found to be faster for 3! and 10! but slower for 25!
# This is surprising as I was expecting recursion to be slower in all cases. Generally it will be slower than iterative functions
# Here's the results I found from one run:
# 3! - Iteration: 1000ns, Recursion: 791ns
# 10! - Iteration: 1000ns, Recursion: 875ns
# 25! - Iteration: 1250ns, Recursion: 1500ns