# Given an integer, write a function that returns true if the given number is palindrome, else false.


number = input("Enter number: ")

# Loop Version

print("\nPython Shortcut Version")
if(number.isnumeric):
    print(number == number[::-1])

print("\nLoop Version")

# Get the length of the number enter
length = len(number)
# Determine the number of pairs to compare
pairs = rounds = int(length /2)
# Initialise the first index of the character to be compared 
first_index = 0
# Initialise the last index of the character to be compared 
last_index = length - 1
# Varible for storing a count of if the first and last characters are equal
equal = 0


while True:
    # Check how many more pairs to compare 
    if rounds > 0:
        # Compare the pairs
        if number [first_index] == number[last_index]:
            # If pairs are equal increase to 1
            equal += 1
    # If there is no more pairs to compare to loop
    else:
        break

    # Increase the next indices to compare 
    first_index += 1
    last_index -= 1
    # Decrease how many more pairs to compare
    rounds -= 1

# Check if the number of pairs compared are equal to the number of same pairs
if pairs == equal:
    print("True")
else:
    print("False")

    
# Recursive Version

print("\nRecursive Version")

# Initialise variables that would be used in throughout the code
length = len(number)
pairs = int(len(number)/2)
COUNT = 0


def compare_pairs(digit1, digit2):
    """
    Takes a pair of number and compare them, if they are the same add 1 to count
    
    Args:
        digit1 (int): Number at the first half
        digit2 (int): Number at the second half
    """

    # Assign the COUNT as a global variable
    global COUNT
    
    if digit1 == digit2:  
        COUNT += 1

def numbers_palindrome(number, first_index, last_index, rounds):
    """
    Takes a number, start and end index, and how many pairs of digits there are in the number
    
    Args:
        number (string): Number to check
        first_index (int): Index of the digits at the first half
        last_index (int): Index of the digits at the last half
        rounds (int): Number of pairs
    """
    # Check if there are no more pairs to check
    if rounds == 0:
        pass
    else:
    # If there are pairs to check
    # Change location for the first and last index 
    # Decrease the number of pairs to check
        first_index += 1
        last_index -= 1
        rounds -= 1
        # Compare pairs of digit
        compare_pairs(number[first_index], number[last_index])
        # Call the numbers_palindrome 
        numbers_palindrome(number, first_index, last_index, rounds)

    # Check if all the digits in the pairs are equal
    return pairs == COUNT

print(numbers_palindrome(number, 0, length-1, pairs))
