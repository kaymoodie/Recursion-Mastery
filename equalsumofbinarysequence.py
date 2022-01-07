# Given a number n, find all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
# Loop Version

print("Loop Version")
# Convert a decimal to binary
n = int(input("Enter a number: "))
no_of_bin_nums = pow((2 * n),2)
binary_sequence = []
bin_with_matching_halves = []

for number in range(no_of_bin_nums):
    bit = n * 2 - 1
    binary_number = ""
   
    while bit >= 0:
        if  number % pow(2,bit) < number:
            binary_number += "1"
            number -= pow(2,bit)
        else:
            binary_number += "0"
        bit -=1
 
    binary_sequence.append(binary_number)

# Split and Convert strings
for item in binary_sequence:
    length = len(item)
    first_half = item[0:int(length/2)]
    second_half = item[int(length/2):length]
    index = len(first_half) -1
    sums1 = sums2 = 0
    exponent = 0
    
    while index >= 0:
        sums1 += int(first_half[index]) 
        sums2 += int(second_half[index]) 
        exponent += 1
        index -= 1
        
    if sums1 == sums2:
        bin_with_matching_halves.append(item)
            
    sums1 = sums2 = 0
    
print(binary_sequence)
print(bin_with_matching_halves)

# Recursive Version
BINARY_SEQUENCE =[]
SUM_SAME = []
# Get number of bits
def get_number(num_input):

    no_of_bin_nums = pow((2 * num_input),2)-1
    bits = (2 * num_input) - 1

    return no_of_bin_nums, bits

# Get binary number for each number 
def get_binary_number(number,bit):
    global BINARY_SEQUENCE
    binary_number = ""
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
    #print(binary_number[0:int(length/2)])
    sum2 =  sums(binary_number[int(length/2):length],0,0)
    #print(binary_number[int(length/2):length-1])
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
