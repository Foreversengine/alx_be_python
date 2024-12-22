# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")  # Print asterisk without advancing to a new line
    print()  # Print a newline character to move to the next row
    row += 1