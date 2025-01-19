#Task 1 - Print out the value of a variable in binary and decimal form
x = 31
print (x, bin(x), hex(x))

#Task 2 - Identify the error when giving an incorrect input type
x = 18
print (x, bin(x), hex(x))
#When x = 1.825, the error returned is "float object cannot be interpreted as an integer"
#The binary and hexadecimal functions are designed to work with integers, not decimals

#Task 3 - Assigning a binary or hex value to a variable
y = 0b1011
z = 0xA3
print (y,z)

w = x + y + z
print ("the sum is",w)

#Compression
#Task 1 - Choose meaningful variable names for a program to calculate the % of compression
orig_size = 240
dictionary_size = 25
compressed_size = 148
compression = 1 - ((compressed_size + dictionary_size) / orig_size)

#Task 2 - Assign values to your variables. Calculate the result
print("Calculated compression: " + str(compression))

#Task 4 - Print out your result and make the output similar to what's shown
total_characters = compressed_size + dictionary_size
percent_compression = compression*100
print(f"Compressed text size: {compressed_size} characters \n     Dictionary size: {dictionary_size} characters \n               Total: {total_characters} characters\n  Original text size: {orig_size} characters\n         Compression: {percent_compression:.2f}"+"%")

#Extra credit - Write a script to find the two's complement of a decimal number (min -128, max 127) input by a user
num = int(input("Enter an integer between [-128,127]: "))
#Check for valid input
if not -128 <= int(num) <= 127:
    raise ValueError ("The number must be between -128 and 127")
#Define the number of bits
num_bits = 8
#Convert number input to binary and convert to two's complement
#Use zfill to include the appropriate number of bits for 8-bit representation
#Use [2:] to remove prefix
def twos_comp_from_decimal(num, num_bits):
    if num >= 0:
        binary = bin(num)[2:].zfill(num_bits)
    else:
        binary = bin(2**num_bits + num)[2:]
    return binary
print(twos_comp_from_decimal(num, num_bits))