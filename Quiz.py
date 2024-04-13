import random

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for i, option in enumerate(self.options):
            print(f"{chr(97 + i)}) {option}")
        print()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display_question()
            answer = input("Enter your answer (a, b, c, or d): ").lower()
            if answer == question.correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer is: {question.correct_answer.upper()}")
            print()
        print("Quiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")

# Define your questions here
questions = [
    Question("What does CPU stand for?",
             ["Central Processing Unit", "Computer Personal Unit", "Central Personal Unit", "Central Processor Unit"],
             "a"),
    Question("What is the full form of RAM?",
             ["Random Access Memory", "Randomly Accessed Memory", "Random Accessed Memory", "Random Application Memory"],
             "a"),
    Question("What does HTML stand for?",
             ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyperlink Transfer Markup Language"],
             "a"),
    Question("What is the purpose of a GPU?",
             ["Central Processing Unit", "Random Access Memory", "Graphics Processing Unit", "Hard Disk Drive"],
             "c"),
    Question("Which programming language is known for its simplicity and readability?",
             ["Java", "C++", "Python", "JavaScript"],
             "c"),
    Question("What is the name of the largest computer network in the world?",
             ["Internet", "Intranet", "LAN", "WAN"],
             "a"),
    Question("Which company developed the Python programming language?",
             ["Google", "Microsoft", "Apple", "Dropbox"],
             "a"),
    Question("What is the function of an operating system?",
             ["Manage hardware resources", "Design websites", "Create documents", "Play games"],
             "a")
]

# Create a quiz object
quiz = Quiz(questions)

# Run the quiz
quiz.run_quiz()
