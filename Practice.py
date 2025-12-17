global_attempts = 5

def main():
    name = input("Enter your name: ")
    if name == "":
        print("Name cannot be empty. Please try again.")
        global global_attempts
        global_attempts -= 1
        if global_attempts == 0:
            print("No attempts left. Exiting.")
            return
        else:
            print(f"You have {global_attempts} attempts left.")
            main()
    elif name == "butthead":
        print("Inappropriate name entered. Please try again.")
        global_attempts -= 1
        if global_attempts == 0:
            print("No attempts left. Exiting.")
            return
        else:
            print(f"You have {global_attempts} attempts left.")
            main()
main()