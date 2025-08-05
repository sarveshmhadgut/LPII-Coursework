class Ticket:
    def __init__(self, issue, solution=""):
        self.issue = issue
        self.status = "Open"
        self.solution = solution


tickets = []
knowledge_base = {
    "internet down": "Check if the router is plugged in and restart it.",
    "cannot print": "Ensure the printer is connected and has enough paper.",
    "slow computer": "Restart your computer and close unnecessary applications.",
}

faqs = [
    "How to reset my password?",
    "How do I set up my email?",
    "What to do if I can't access the company portal?",
]


def create_ticket():
    issue = input("Enter the issue: ")
    if issue in knowledge_base:
        solution = knowledge_base[issue]
        print(f"Solution based on common issues: {solution}")
        tickets.append(Ticket(issue, solution))
        print("Ticket created with a suggested solution.")
    else:
        tickets.append(Ticket(issue))
        print("Ticket created. Our team will get back to you with a solution.")


def view_tickets():
    if not tickets:
        print("No tickets found.")
        return
    for i, ticket in enumerate(tickets, start=1):
        print(f"Ticket {i}: Issue - {ticket.issue}, Status - {ticket.status}", end="")
        if ticket.solution:
            print(f", Suggested Solution - {ticket.solution}")
        else:
            print()


def display_faqs():
    print("Frequently Asked Questions:")
    for faq in faqs:
        print(f"- {faq}")


def main():
    while True:
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. View FAQs")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_ticket()
            elif choice == 2:
                view_tickets()
            elif choice == 3:
                display_faqs()
            elif choice == 4:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
