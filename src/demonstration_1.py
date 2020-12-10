"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    #create empty string
    ans = ""
    #Loop through each Char if input string 
    for char in string:
        #for each char convert to ascii
        ascii_char = ord(char)
        #check if num is between 65 and 90
        if 65 <= ascii_char <= 90:
            #the letter is uppercase, then convert to lower 
            lower_char = ascii_char + 32
            # lower char = char + 32
            lower_char = chr(lower_char)
            # convert lower char to letter
            ans += lower_char
            # add lower char to answer string
        # else
        else:
            ans += char 
            # add the char to the answer string

    #return answer string
    return ans

print(to_lower_case('LAMA'))