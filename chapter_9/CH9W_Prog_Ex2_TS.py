
import random

def main():
    # Dictionary of US states and their capitals, kept it at 10 for better testing
    capitals = {
        'Illinois': 'Springfield',
        'California': 'Sacramento',
        'Texas': 'Austin',
        'Florida': 'Tallahassee',
        'New York': 'Albany',
        'Georgia': 'Atlanta',
        'Ohio': 'Columbus',
        'Michigan': 'Lansing',
        'Nevada': 'Carson City',
        'Arizona': 'Phoenix'
    }

    # Convert dictionary keys to a list for shuffling
    states = list(capitals.keys())
    random.shuffle(states)

    # Initialize counters for correct and incorrect answers
    correct = 0
    incorrect = 0

    # Quiz the user
    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == capitals[state].lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {capitals[state]}.\n")
            incorrect += 1

    # Show results
    print("Quiz Complete!")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

main()