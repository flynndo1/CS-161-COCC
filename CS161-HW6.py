#Task 1 - Ask the user to enter an integer, store the value and count it down
#Task 2 - Modify the loop to print out whether a number is even or odd
#Task 3 - Ask the user to enter the amount of decrease and use this value in the loop
x = int(input("Enter an integer: "))
decrease = int(input("Enter a decrease value: "))
while (x > 0):
    if (x % 2 == 0):
        print(f"{x} is even")
        x = x - decrease
    else:
        print(f"{x} is odd")
        x = x - decrease
print ('blastoff!!')

#Task 4.1 - Write a loop to print out words until the word has a length less than 5 letters
#Task 4.2 - Rewrite the loop so it stops if the word has < 5 letters, or they have entered more than 5 words
word_count = 0
while True:
    word = input("Enter a word: ")
    word_count += 1
    if len(word) < 5:
        print("goodbye")
        break
    elif word_count > 5:
        print("loser")
        break
    else:
        print(f"{word} has {len(word)} letters")

#Task 5 - Write a while loop that counts from 10 to 100 in decimal, binary, and hex
x = 10
while x<101:
    y = bin(x)
    z = hex(x)
    print(x, y,z)
    x += 1

#Task 6 - Write two functions that will print a number of stars == to the input and decrements one fewer each time until x==0
#Iteration:
k = int(input("Enter the number of stars: "))
while k > 0:
    print ("*" * k)
    k = k - 1

#Recursion
def stars(n):
    """This function will print the number of stars input by the user and then print one fewer star until there are none left"""
    if n==0:
        return
    else:
        print("*" * n)
        stars(n-1)

t = int(input("Enter the number of asterisks: "))
stars(t)




