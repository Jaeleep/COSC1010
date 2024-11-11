#
# Jae Lee Park
# Nov 9, 2024
# Capital Quiz Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South       Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables
    correct_answers = 0
    incorrect_answers =0

    # Continue until user quits the game.
    while True:
        # Randomly select a state from the dictionary
        state = random.choice(list(capitals.keys()))
        correct_capital = capitals[state]

        # Ask the user to input the capital
        user_answer = input("What is the capital of " + state + "? (or type 'quit' to exit): ").strip()

        # Allow the user to quit the game
        if user_answer.lower() == 'quit':
            print("Thanks for playing!")
            break

        # Check if the user's answer is correct
        if user_answer.lower() == correct_capital.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect! The correct answer is " + correct_capital + ".")
            incorrect_answers += 1

        # Show the user their progress so far
        print("Correct answers: " + str(correct_answers) + ", Incorrect answers: " + str(incorrect_answers) + "\n")
# Call the main function.
main()
