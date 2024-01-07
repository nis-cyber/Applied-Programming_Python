def grade_exam() -> object:
    # Correct answers
    user_answer = []
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D',
                       'A']
    for i in range(20):
        answer = input(f" Answer for Q no {i + 1} ")
        user_answer.append(answer)
    with open("student_answers.txt", "w") as f:
        f.write(str(user_answer) + "\n")

    # Read student's answers from a file
    with open('student_answers.txt', 'r') as file:
        student_answers = [line.rstrip() for line in file]

    # Check the number of correct and incorrect answers
    num_correct = 0
    incorrect_questions = []
    for i in range(len(correct_answers)):
        print(i)
        if student_answers[i] == correct_answers[i]:
            num_correct += 1
        else:
            incorrect_questions.append(i + 1)

    # Check if the student passed or failed
    if num_correct >= 15:
        result = "Passed"
    else:
        result = "Failed"

    # Display results
    print("Result: " + result)
    print("Total correctly answered questions: " + str(num_correct))
    print("Total incorrectly answered questions: " + str(len(incorrect_questions)))
    print("Incorrectly answered questions: " + str(incorrect_questions))

# Call the function to grade the exam
grade_exam()
