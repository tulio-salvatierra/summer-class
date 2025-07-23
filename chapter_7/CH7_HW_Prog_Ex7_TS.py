# Driver's License Exam Grader

# a second list of incorrect answers is provided as a comment for testing purposes.

def main():
    # List of correct answers
    answers = [
        'A', 'C', 'A', 'A', 'D',
        'B', 'C', 'A', 'C', 'B',
        'A', 'D', 'C', 'A', 'D',
        'C', 'B', 'B', 'D', 'A'
    ]
    
     # List of incorrect answers
    #answers = [
    #    'A', 'B', 'A', 'A', 'B',
    #    'B', 'A', 'A', 'C', 'A',
    #    'A', 'C', 'C', 'A', 'B',
    #    'C', 'D', 'B', 'D', 'C'
    #]


    # Read student answers from file
    try:
        infile = open("student_answers.txt", "r")
        student_answers = []

        for line in infile:
            answer = line.strip().upper()
            student_answers.append(answer)

        infile.close()

        # Compare answers
        total_correct = 0
        incorrect_questions = []

        for i in range(20):
            if student_answers[i] == answers[i]:
                total_correct += 1
            else:
                incorrect_questions.append(i + 1)  # Question numbers are 1-based

        # Display results
        print("Result:")
        if total_correct >= 15:
            print("You passed the exam!")
        else:
            print("You failed the exam.")

        print("Total correct answers:", total_correct)
        print("Total incorrect answers:", 20 - total_correct)
        print("Questions answered incorrectly:", incorrect_questions)

    except FileNotFoundError:
        print("Error: student_answers.txt not found.")
    except IndexError:
        print("Error: Not enough answers in the file (should be 20).")

main()