#
# Jae Lee Park
# Sep 15, 2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

#Local variables
numAttending = 0 # The number of people attending
numPerperson = 0 # The number of hot dogs and buns per person
total = 0 # The total number of hot dogs and buns needed
minDogs = 0 # The minimum number of packages of hot dogs 
minBuns = 0 # The minimum number of packages of hot dog buns
dogsLeft = 0 # The numberof hot dogs left over from a package
bunsLeft = 0 # The number of hot dog buns left over from a package

# Get the number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs per person from the user.
numPerperson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs and buns needed.
total = numAttending * numPerperson

# Calculate the minimum number of packages of hot dogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is larege enough to require more than one package of hot dogs.
if minDogs > 0 :
    #Calculate the number of hot dogs left over from a package if any.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    #If there will be left overs, add an additional package of hot dogs
    if dogsLeft != 0:
        minDogs += 1

# Set the minimum number of packages of hot dogs to one becuase the numberof people attending is small enough to requrie only one package of hot dogs.
else: 
    minDogs = 1
 
# Determine the number of lefover hot dogs, if any.
dogsLeft = (HOT_DOGS_PER_PACKAGE * minDogs) - total 

# Calculate the minimum number of packages of buns needed.
minBuns = (total + BUNS_PER_PACKAGE - 1) //BUNS_PER_PACKAGE

#Determine the number of lefover buns.
bunsLeft = (BUNS_PER_PACKAGE * minBuns) - total 

# Display the minimum packages of hot dogs needed.
print('Minimum packages of hot dogs nedded: ', minDogs)
 
# Display the minimum packages of hot dog buns needed.
print('Minimum packages of hot dog buns nedded: ', minBuns)

# Display the number of hot dogs left over.
print('Hot dogs left over: ', dogsLeft)

# Display the number of hot dog buns left over.
print('Hot dog buns left over: ', bunsLeft)