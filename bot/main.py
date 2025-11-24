
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please provide name and phone."

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please provide name and phone."

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    if not args:
        return "Please provide a name."

    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    return f"Contact list: {contacts}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can l help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()