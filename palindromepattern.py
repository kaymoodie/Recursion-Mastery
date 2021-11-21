word = "madam"

#Loop Version
print("Loop Version \n")

# Initialize start and end index 
start = 0
end = 1
# Get length of the word entered
length = len(word)

# Initialize list for storing patterns
palindrome_patterns = []

# Outer loop determines the size of the substring
for  increase in range(0, length):
    
    #print(f"Increased by {increase}")
    # Inner loop get the substring at a given start and end index
    while start <= length -1 and end <= length:
        # Stores the substring
        substring =  word[start: end]
        # Copy the substring
        reversed_substring =  word[start:end]
        # Reverse the copy of the substring
        reversed_substring = reversed_substring[::-1]
            
        #print(f"Substring {substring}, index start: {start} index end {end}")
        
        # Check if the substring and the reverse substring are same
        # If the same add the substring to list of patterns
        if substring == reversed_substring:
            palindrome_patterns.append(substring)
        
        # Move the start index by 1
        start += 1
        # Move the end index by 1
        end += 1
        
    # Increase the size of the substring by 1
    increase += 1
    # Set the end index to substring size + 1
    end = 1 + increase
    # Reset start index to 0
    start = 0
   
# Display the patterns stored in the list
for item in palindrome_patterns:
    print(item)
    


#Recurison Version 

print("\nRecursive Version\n")

# Initialize list for storing patterns
palindrome_patterns = []

def patterns(string):
    """Compares the value entered with a reversed of the value and checks if they are the same
    Args:
        string (str): characters stored together
    """
    # Reverse the string 
    reversed_substring = string[::-1]
    
    # Compare the two strings
    # If same add string to the list
    if string == reversed_substring:
        palindrome_patterns.append(string)

def palindromepattern(string, start, end, increaseby):
    """Takes a string (group of characters), get various combinations (substrings) and check if the substrings are palidrome patterns
    
    Args:
        string (str): Substrings/String to compare
        start (int): Start index for the substring/string
        end (int): Start index for the substring/string
        increaseby (int): Substring length to be increase by
    """
    
    #print(f"Moved index by {increaseby}")
    # Get the length of the string entered    
    length = len(string)
    #print(f"Substring {string[start:end]}, index start: {start} index end {end}")
    # Check the substring at the start and end index
    patterns(string[start:end])
    
    # Check if end index is last index value and there is no more to increase the substring by
    if(end == length and increaseby == length):
        pass
   
    # Check substrings between the start and end index
    # If the start index is between 0 to length and end index is between 1 and length -1 
    # Call palidromepattern with argument string, start index increased by 1, end index increase by 1 and increase value as same
    elif (start < length and end <= length-1):
        palindromepattern(string, start + 1, end + 1, increaseby)
        
    # If start index is more than length
    # Reset start index to 0, set end index to increasedby value plus 1
    # Call palindromepattern with string and newly initialized values for start, end and increaseby plus 1
    else:
        start = 0
        end = increaseby + 1
        palindromepattern(string, start, end , increaseby + 1 )

# Call the palindorome method
palindromepattern(word, 0, 1, 1)

# Display patterns found
for item in palindrome_patterns:
    print(item)