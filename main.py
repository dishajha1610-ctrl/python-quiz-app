def main():
    print("Welcome to the Python Quiz App!")
    name = input("Enter your name: ").strip() or "Student"

    questions = [
        {
            "question": "What does this code print? x = [1, 2]; y = x; y.append(3); print(x)",
            "choices": ["A) [1, 2]", "B) [1, 2, 3]", "C) [3]", "D) Error"],
            "answer": "B",
        },
        {
            "question": "What is the result of [x * 2 for x in range(3)]?",
            "choices": ["A) [0, 1, 2]", "B) [0, 2, 4]", "C) [2, 4, 6]", "D) [1, 2, 3]"],
            "answer": "B",
        },
        {
            "question": "What does the expression 10 // 3 return?",
            "choices": ["A) 3.33", "B) 3", "C) 1", "D) 4"],
            "answer": "B",
        },
        {
            "question": "What is printed by print('Python'[1:4])?",
            "choices": ["A) Pyt", "B) yth", "C) tho", "D) ytho"],
            "answer": "B",
        },
        {
            "question": "Which statement about a Python dictionary is correct?",
            "choices": [
                "A) Keys must be unique",
                "B) Values must be unique",
                "C) Keys can only be strings",
                "D) Dictionaries cannot be changed",
            ],
            "answer": "A",
        },
        {
            "question": "What does this function return? def f(a, b=2): return a * b; f(3)",
            "choices": ["A) 5", "B) 6", "C) 3", "D) Error"],
            "answer": "B",
        },
        {
            "question": "What is the purpose of finally in a try/except statement?",
            "choices": [
                "A) It runs only if an exception occurs",
                "B) It runs only if no exception occurs",
                "C) It normally runs whether an exception occurs or not",
                "D) It defines a new exception",
            ],
            "answer": "C",
        },
        {
            "question": "What does enumerate(['a', 'b']) provide in a loop?",
            "choices": [
                "A) Each item only",
                "B) Each item's index and value",
                "C) The list in reverse",
                "D) The number of items only",
            ],
            "answer": "B",
        },
        {
            "question": "What is printed by print(bool([]))?",
            "choices": ["A) True", "B) False", "C) []", "D) Error"],
            "answer": "B",
        },
        {
            "question": "Which statement creates a shallow copy of list items?",
            "choices": [
                "A) copy = items",
                "B) copy = items.copy()",
                "C) copy = items.clear()",
                "D) copy = list",
            ],
            "answer": "B",
        },
    ]

    score = 0

    for number, item in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {item['question']}")

        for choice in item["choices"]:
            print(choice)

        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            answer = input("Please enter A, B, C, or D: ").strip().upper()

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {item['answer']}.")

    total = len(questions)
    percentage = score / total * 100

    print("\n" + "=" * 40)
    print(f"Quiz complete, {name}!")
    print(f"Score: {score} out of {total} ({percentage:.0f}%)")

    if percentage == 100:
        print("Remark: Excellent! You got a perfect score!")
    elif percentage >= 80:
        print("Remark: Great work! You understand these Python topics well.")
    elif percentage >= 60:
        print("Remark: Good effort! Review a few topics and try again.")
    elif percentage >= 40:
        print("Remark: Keep practising the topics you missed.")
    else:
        print("Remark: Keep learning Python basics—you can try again!")

    print("=" * 40)


if __name__ == "__main__":
    main()