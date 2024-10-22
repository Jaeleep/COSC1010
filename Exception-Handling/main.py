#
# Jae Lee Park
# Oct 22, 2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Declare local variables
myfile = None
line = ""
number = 0
total = 0 
count = 0
average = 0


try:
    # Try to open the file. 'numbers.txt' in read mode
    myfile = open('numbers.txt', 'r')
    
    # Iterate over each line in the file
    for line in myfile:
        try:
            #Convert the line to an integer and add it to the total
            number = int(line.strip())
            total += number
            count += 1
        except ValueError:
            print("Value Error occured")
    if count > 0:
        average = total / count
        # Display the average
        print("The average of the number is : ", average)
    else:
        print("Error: The file did not contain any valid numbers.")

except IOError:
    # Handle errors in opening/reading the file
    print("IOError occured")

finally:
    # Close the file if it was successfully opened
    if myfile is not None:
        myfile.close
