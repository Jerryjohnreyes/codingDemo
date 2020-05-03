# Store the file path associated with the file (note the backslash may be OS specific)
file = '../Resources/input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()
    # it is stored in a string variable
    for letter in lines:
        print(letter)

    # Print the contents of the text file
    print(lines)
