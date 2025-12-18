global_attempts = 3 # Global variable to track attempts

import time # Import time module for delays
def main(): # Main function to get user input and handle logic
    name = input("Enter your name: ") # Get user input
    if name == "": # Check for empty input
        print("Name cannot be empty. Please try again.") # Prompt user again
        global global_attempts # Access global variable
        global_attempts -= 1 # Decrement attempts
        if global_attempts == 0: # Check if attempts are exhausted
            print("No attempts left. Exiting.") # Notify user and exit
            return # Exit the function
        else: # If attempts remain
            print(f"You have {global_attempts} attempts left.") # Notify user of remaining attempts
            main() # Call main function again
    elif name == "Butthead" or name == "butthead": # Check for inappropriate name
        print("Inappropriate name entered. Please try again.") # Notify user
        global_attempts -= 1 # Decrement attempts
        if global_attempts == 0: # Check if attempts are exhausted
            print(f"Nice try! {name} Exiting.") # Notify user and exit
            return # Exit the function
        else: # If attempts remain
            print(f"You have {global_attempts} attempts left.") # Notify user of remaining attempts
            main() # Call main function again
    elif name == "Beavis" or name == "beavis": # Check for specific name
        print("That's not your name!") # Notify user
        global_attempts -= 1 # Decrement attempts
        if global_attempts == 0: # Check if attempts are exhausted
            print(f"Nice try! {name} Exiting.") # Notify user and exit
            return # Exit the function
        else: # If attempts remain
            print(f"You have {global_attempts} attempts left.") # Notify user of remaining attempts
            main() # Call main function again
    elif name == "BUTTHEAD" or name == "BEAVIS" or name.isupper(): # Check for uppercase inappropriate names
        if(global_attempts == 3):
            print("DON'T SCREAM AT ME!") # Notify user
        if(global_attempts == 2):
            print("STOP SCREAMING AT ME!") # Notify user
        if(global_attempts == 1):
            print("SCREAM AT ME ONE. MORE. TIME. I DARE YOU!") # Notify user
        global_attempts -= 1 # Decrement attempts
        if global_attempts == 0: # Check if attempts are exhausted
            print(f"SINCE YOU WON'T STOP... I'M...") # Notify user
            time.sleep(1) # Pause for dramatic effect
            print("C:\\format c: /fs:NULL") # Simulate command
            time.sleep(3) # Pause for dramatic effect
            print("The type of the file system is NTFS.") # Simulate command output
            time.sleep(1) # Pause for dramatic effect
            print("WARNING ALL DATA ON NON-REMOVABLE DISK DRIVE C: WILL BE LOST!") # Simulate warning
            time.sleep(2) # Pause for dramatic effect
            print("Proceed with Format <Y/N>? Y") # Simulate user confirmation
            time.sleep(1) # Pause for dramatic effect
            print("Formatting...") # Simulate formatting
            time.sleep(10) # Simulate time taken to format
            print("Just kidding!") # Notify user
            time.sleep(1) # Pause for dramatic effect
            print("Have a nice day!") # Notify user
            time.sleep(1) # Pause for dramatic effect
            print("Exiting!") # Notify user and exit
            return # Exit the function
        else: # If attempts remain
            if(global_attempts > 1):
                print(f"You have {global_attempts} attempts left.") # Notify user of remaining attempts 
            else:
                print(f"You have {global_attempts} attempt left.") # Notify user of remaining attempts
            main() # Call main function again
            return # Exit the function
    else: # If valid name is entered
        print("That's NOT your name!") # Notify user
        global_attempts -= 1 # Decrement attempts
        if global_attempts == 0: # Check if attempts are exhausted
            print(f"Nice try {name.capitalize()}! Exiting.") # Notify user and exit
            return # Exit the function
        else: # If attempts remain
            print(f"You have {global_attempts} attempts left.") # Notify user of remaining attempts
            main() # Call main function again
main()