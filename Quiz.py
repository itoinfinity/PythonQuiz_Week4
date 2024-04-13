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

def select_difficulty():
    while True:
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Define your questions here
easy_questions = [
    Question("What does CPU stand for?",
             ["Central Processing Unit", "Computer Personal Unit", "Central Personal Unit", "Central Processor Unit"],
             "a"),
    Question("What is the full form of RAM?",
             ["Random Access Memory", "Randomly Accessed Memory", "Random Accessed Memory", "Random Application Memory"],
             "a"),
    Question("What does HTML stand for?",
             ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyperlink Transfer Markup Language"],
             "a")
]

medium_questions = [
    Question("What is the purpose of a GPU?",
             ["Central Processing Unit", "Random Access Memory", "Graphics Processing Unit", "Hard Disk Drive"],
             "c"),
    Question("Which programming language is known for its simplicity and readability?",
             ["Java", "C++", "Python", "JavaScript"],
             "c"),
    Question("What is the name of the largest computer network in the world?",
             ["Internet", "Intranet", "LAN", "WAN"],
             "a")
]

hard_questions = [
    Question("Which company developed the Python programming language?",
             ["Google", "Microsoft", "Apple", "Dropbox"],
             "a"),
    Question("What is the function of an operating system?",
             ["Manage hardware resources", "Design websites", "Create documents", "Play games"],
             "a"),
    Question("What is the process of finding errors and fixing them within a program called?",
             ["Debugging", "Programming", "Compiling", "Running"],
             "a")
]

# Main program
def main():
    difficulty = select_difficulty()
    if difficulty == 1:
        questions = easy_questions
    elif difficulty == 2:
        questions = medium_questions
    else:
        questions = hard_questions

    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
