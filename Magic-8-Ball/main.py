#
# Jae Lee Park
# OCt 24, 2024
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
import random

# Load responses from the file into a list
try:
    with open("8_ball_responses.txt", "r") as file:
        responses = file.read().splitlines()
except IOError as e:
    print("Error reading responses file:", e)
    exit()

# Welcome message
print("Welcome to the Magic 8 Ball!")

# Main loop to ask questions and display random responses
while True:
    question = input("Ask a yes or no question (or type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    # Display a random response
    print("Magic 8 Ball says:", random.choice(responses))

# Goodbye message
print("Goodbye!")