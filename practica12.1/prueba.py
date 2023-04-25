# Function to Validate the Roman numeral
def ValidationOfRomanNumerals(string):
     
    # Importing regular expression
    import re
     
    # Searching the input string in expression and
    # returning the boolean value
    print(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string)))
 
# Driver code
 
# Given string
string="VX"
 
# Function call
ValidationOfRomanNumerals(string)