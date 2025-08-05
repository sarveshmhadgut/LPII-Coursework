class Employee:
    def __init__(self, name, performance=0, feedback=""):
        self.name = name
        self.performance = performance
        self.feedback = feedback


employees = []

knowledge_base = {
    "poor": "Provide training and mentorship.",
    "average": "Set clear goals and expectations.",
    "good": "Recognize and reward achievements.",
    "excellent": "Promote and provide growth opportunities.",
}


def evaluate_performance():
    name = input("Enter the employee's name: ")

    try:
        performance = int(
            input(
                "Enter the employee's performance (1 - Poor, 2 - Average, 3 - Good, 4 - Excellent): "
            )
        )
        if performance < 1 or performance > 4:
            print("Invalid performance level.")
            return
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    feedback = input("Enter any additional feedback: ")

    employees.append(Employee(name, performance, feedback))
    print("Performance evaluation completed.\n")


def display_feedback():
    if not employees:
        print("No performance evaluations available.\n")
        return

    print("Employee Performance Feedback:\n")
    for employee in employees:
        print(f"Name: {employee.name}")
        print("Performance: ", end="")
        if employee.performance == 1:
            print("Poor")
            suggested_action = knowledge_base["poor"]
        elif employee.performance == 2:
            print("Average")
            suggested_action = knowledge_base["average"]
        elif employee.performance == 3:
            print("Good")
            suggested_action = knowledge_base["good"]
        elif employee.performance == 4:
            print("Excellent")
            suggested_action = knowledge_base["excellent"]
        else:
            suggested_action = "Unknown"

        print(f"Feedback: {employee.feedback}")
        print(f"Suggested Action: {suggested_action}\n")


def main():
    while True:
        print("Employee Performance Evaluation System")
        print("1. Evaluate Performance")
        print("2. Display Feedback")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            evaluate_performance()
        elif choice == 2:
            display_feedback()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
