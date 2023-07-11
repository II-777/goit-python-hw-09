import re

def input_error(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "[-] Input Error. Use 'help' for assistance."
        except Exception as e:
            return "[-] Exception: " + str(e)
    return wrap

class ContactData:
    def __init__(self):
        self.data = {}

    @input_error
    def add(self, contactname, phone):
        self.data[contactname] = phone
        return "[+] Contact added successfully."

    @input_error
    def change(self, contactname, phone):
        if contactname in self.data:
            self.data[contactname] = phone
            return "[+] Phone number changed successfully."
        return "[-] No matching records found."

    @input_error
    def phone(self, contactname):
        if contactname in self.data:
            return self.data[contactname]
        return "[-] Record not found."

    def show_all(self):
        if self.data:
            return "\n".join([f"Contact: {contact}, Phone: {phone}" for contact, phone in self.data.items()])
        return "[-] No records found. The Database is empty"

class Bot:
    def __init__(self):
        self.contact_data = ContactData()
        self.commands = {
            "hello": self.handle_hello,
            "add": self.handle_add,
            "change": self.handle_change,
            "phone": self.handle_phone,
            "show all": self.handle_show_all,
            "help": self.handle_help
        }
        self.exit_commands = ["x", "close", "exit", "good bye"]

    def parse_input(self, input_str):
        for cmd in self.commands:
            pattern = rf"\b{cmd}\b"
            if re.match(pattern, input_str, re.IGNORECASE):
                args = re.split(r"\s+", input_str.lstrip(cmd).strip(), maxsplit=1)
                args = [s.strip() for s in args]
                return cmd, args
        return input_str.lower(), []

    def handle_hello(self, *args):
        return "[+] What's up?"

    @input_error
    def handle_add(self, *args):
        contactname, phone = args
        return self.contact_data.add(contactname, phone)

    @input_error
    def handle_change(self, *args):
        contactname, phone = args
        return self.contact_data.change(contactname, phone)

    @input_error
    def handle_phone(self, *args):
        contactname = args[0]
        return self.contact_data.phone(contactname)

    def handle_show_all(self, *args):
        return self.contact_data.show_all()

    def handle_help(self, *args):
        HELP = {
            "help     ": "Show help message.",
            "add      ": "Add new record (ex.: 'add John 40054').",
            "change   ": "Change existing record (ex.: 'change John 30045')",
            "phone    ": "Show contact phone (ex.: 'phone John').",
            "show all ": "Show all records.",
            "hello    ": "Print a greeting",
            "x        ": "Exit",
            "close    ": "Exit",
            "exit     ": "Exit",
            "good bye ": "Exit"
        }
        print('\n')
        for key, value in HELP.items():
            print(f"{key} - {value}")
        print('\n')

    def run(self):
        while True:
            try:
                contact_input = input("Enter your command:")
            except KeyboardInterrupt:
                break

            if contact_input.lower() in self.exit_commands:
                break

            command, args = self.parse_input(contact_input)
            handler = self.commands.get(command)
            if handler:
                result = handler(*args)
                if result:
                    print(result)
            else:
                print("[-] Command not recognized. Please try a different command or use 'help' for assistance.")

        print("\n[+] See you later, pal!")

def main():
    print("Hi, I am Cortana and I am here to help! A touch of sign in here and a WiFi there... Just kidding! I am Based Assistant :)\nType in 'help' if you feel lost or press 'CTRL+C' to exit. Enough intro let's dig in...\n")
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
