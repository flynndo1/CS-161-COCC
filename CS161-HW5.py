#Task 1 - Write an if statement to determine if a number is divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")

#Task 2.1 - Use if and elifs to print the name of a state capital when given the name of the state (do for 5 or 6 states)
state = input("Enter a state in the USA: ")
if state == "Alaska":
    print("The capital of Alaska is Juneau")
elif state == "Alabama":
    print("The capital of Alabama is Montgomery")
elif state == "Arizona":
    print("The capital of Arizona is Phoenix")
elif state == "California":
    print("The capital of California is Sacramento")
elif state == "Colorado":
    print("The capital of Colorado is Denver")
else:
    print("I don't know the capital of that state")

#Task 2.2 - Create a dictionary of the states and capitals and use a get() to print the name of the capital
state_cap = {
    "Arkansas": "Little Rock",
    "Idaho": "Boise",
    "Mississippi": "Jackson",
    "Ohio": "Columbus",
    "Kansas": "Topeka",
    "Washington": "Olympia"
}

capital = state_cap.get(state, "Not found")
print(capital)

#Task 2.3 - Use the "match case" to do the same thing
match state:
    case "Illinois":
        print("The capital of Illinois is Springfield")
    case "Montana":
        print("The capital of Montana is Helena")
    case "Delaware":
        print("The capital of Delaware is Dover")
    case "Georgia":
        print("The capital of Georgia is Atlanta")
    case "Kentucky":
        print("The capital of Kentucky is Frankfort")
    case other:
        print("I don't know the capital of that state")

#Task 3 - Use elif in a function definition. Use docstrings to document your function
age = int(input("Enter your age in years: "))
def pool_admission(age):
    """The pool_admission function takes age as an input and returns the price of admission without a $ sign"""
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

print(f"The price of admission is {pool_admission(age)}")

#Task 4 - Determine how many times the string "160" appears in the HTML code for coccbobcat.com
import requests
from bs4 import BeautifulSoup
website = "http://coccbobcat.com"
keyword = "160"
response = requests.get(website)
soup = BeautifulSoup(response.text, "html.parser")
content = soup.get_text()
total_keyword_count = content.count(keyword)

print(f"The substring '{keyword}' appears {total_keyword_count} times in the HTML source of {website}")

#Task 5 - Write a Python program that will determine the number of processes running on your system
import psutil
active_processes = psutil.pids()
count_processes = len(active_processes)
print(f"Number of active processes: {count_processes}")