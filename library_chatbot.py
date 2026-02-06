print("Welcome to the Library Chatbot")
print("Ask me about library services")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Thank you for visiting the library")
        break

    if "timing" in user_input or "hours" in user_input:
        print("Bot: Library is open from 9 AM to 5 PM")

    elif "issue" in user_input or "borrow" in user_input:
        print("Bot: You can issue books for 14 days")

    elif "return" in user_input:
        print("Bot: Please return books before the due date")

    elif "fine" in user_input or "late" in user_input:
        print("Bot: Late fine is 2 rupees per day")

    elif "membership" in user_input:
        print("Bot: Student ID card is required for membership")

    elif "contact" in user_input:
        print("Bot: Contact librarian at library@college.edu")

    else:
        print("Bot: I can help with library timing, issue, return, fine, membership.")
