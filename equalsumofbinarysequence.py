# Given a number n, find all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
# Loop Version

print("Loop Version")
# Convert a decimal to binary
# Get a number from the user
n = int(input("Enter a number: "))
# Find all the number of binary sequence from 0 to the number entered
no_of_bin_nums = pow((2 * n),2)
# Initialize a list to store all the binary sequence
binary_sequence = []
# Initialize a list to store all the matching half
bin_with_matching_halves = []

 # The length of the number of bits to represent the binary number
bit = n * 2 - 1

# Get each number in number of binary sequence
for number in range(no_of_bin_nums):
   
    # Initialize the place holder for the binary number
    binary_number = ""
   
   # Get each bit
    while bit >= 0:
        # Find the binary number by finding the remainder of number divided by 2 to the power of the current bit
        if  number % pow(2,bit) < number:
            # If the remainder is less than the number then store one to the binary sequence
            binary_number += "1"
            # Decrease the number by 2 to the power of the current bit
            number -= pow(2,bit)
        # If the remainder is 0 then add 0 to the binary sequence
        else:
            binary_number += "0"
        # Go to the next bit
        bit -=1
    # Add the binary number created to the sequence
    binary_sequence.append(binary_number)

# Split and Convert strings
# Get the lenght of the binar
length = bit + 1
# Get each binary number in the sequence
for item in binary_sequence:
    
    # Get the first half of bits in the binary number
    first_half = item[0:int(length/2)]
    # Get the second half of bits in the binary number
    second_half = item[int(length/2):length]
    # Get a starting index 
    index = len(first_half) -1
    # Initialize variables for placing the sum results
    sums1 = sums2 = 0
    
    # Get each bit in both half of the binary sequence
    while index >= 0:
        # Add each bit to sum
        sums1 += int(first_half[index]) 
        sums2 += int(second_half[index]) 
        # Go to the next index
        index -= 1
        
    # Check if the two sums are equal
    if sums1 == sums2:
        # Add the corresponding item to the list
        bin_with_matching_halves.append(item)
    
    # Reset the sums to -   
    sums1 = sums2 = 0
 
 # Display the binary sequence   
print(binary_sequence)
# Display the binary with matching halves
print(bin_with_matching_halves)

# Recursive Version

# Declare Global Variables
BINARY_SEQUENCE =[]
SUM_SAME = []

# Get number of bits
def get_number(num_input):

    # Get the number binary numbers between 0 to the number entered
    no_of_bin_nums = pow((2 * num_input),2)-1
    # Find the number of bits used to represent a binary number
    bits = (2 * num_input) - 1

    return no_of_bin_nums, bits

# Get binary number for each number 
def get_binary_number(number,bit):
    
    # Initialize the global variable to store the binary numbers
    global BINARY_SEQUENCE
    # Initialize the variable to store the binary number
    binary_number = ""
    
    # 
    if number < 0:
        pass
    else:   
        binary_number = convert_binary_number(number,bit)
        BINARY_SEQUENCE.append(binary_number)
        sum_of_half(binary_number, len(binary_number))
        get_binary_number(number-1,bit)

# Convert number into binary number
def convert_binary_number(number,bit):
    if bit < 0 :
        return ""
    elif number % pow(2,bit) < number:
        return "1" + convert_binary_number(number - pow(2,bit), bit-1)
    else:
        return "0" + convert_binary_number(number,bit-1)

# Compare the sum of the two halves 
def sum_of_half(binary_number, length):
    
    global SUM_SAME

    sum1 =  sums(binary_number[0:int(length/2)], 0,0)
    sum2 =  sums(binary_number[int(length/2):length],0,0)
    if sum1 == sum2:
        SUM_SAME.append(binary_number)
    


# Calculate the sum of the binary numbers
def sums(values, index, sum):
    
    if index == len(values)-1:
        return int(values[index]) + sum
    
    sum = int(values[index]) + sum
    
    return sums(values,index+1, sum)

# Get Input from User
print("\nRecursive Version")
n = int(input("Enter a number: "))
no_of_bin_nums, bits = get_number(n)

get_binary_number(no_of_bin_nums, bits)
print(BINARY_SEQUENCE)
print(SUM_SAME)
