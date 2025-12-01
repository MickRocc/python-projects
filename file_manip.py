# file_manip.py
# This script demonstrates file manipulation in Python including reading, writing, and appending to files.
# It also shows how to use the pathlib module to handle file paths.
# The script performs the following operations:
# 1. Reads a file line by line and prints each line in uppercase.
# 2. Writes multiple lines to a file, demonstrating the use of write mode.  
# 3. Reads the file again, sorts the lines, and prints the sorted list.
from pathlib import Path # Import Path from pathlib module
import os # Import os module for operating system dependent functionality
def demo_file_manipulation(mode): # Define a function to demonstrate file manipulation
    if os.path.exists(Path(__file__).parent / "data.txt") == True: # Check if the file does not exist
        if mode == "read": # Read and print each line in uppercase
            with open(Path(__file__).parent / "data.txt", "r") as file: # Open file in read mode
                for line in file: # Iterate through each line in the file
                    print(line.strip().upper()) # Print each line in uppercase, stripping whitespace
    elif os.path.exists(Path(__file__).parent / "data.txt") == False: # If the file does not exist
        demo_file_manipulation("write") # Call the function to write to the file if it doesn't exist
    elif mode == "write": # Write multiple lines to the file
        with open(Path(__file__).parent / "data.txt", "x") as file: # Open file in write mode
            file.write("Path(__file_).parent / 'data.txt' returns current file (This one)'s file path then appends the file we are wanting to open to it. \n Options have to be followed to avoid issues: \n w = write, this will overright all data with new data using the file.write command.\n a = append, this will add to the end of the file. Preserving all existing data.\n r = read, this will only allow reading of the file.\n x = open for exclusive creation, failing if the file already exists.\n + = open a file for updating (reading and writing)") # Write multiple lines to the file
    elif mode == "overwrite": # Write multiple lines to the file
        with open(Path(__file__).parent / "data.txt", "w") as file: # Open file in write mode
            file.write("Path(__file_).parent / 'data.txt' returns current file (This one)'s file path then appends the file we are wanting to open to it. \n Options have to be followed to avoid issues: \n w = write, this will overright all data with new data using the file.write command.\n a = append, this will add to the end of the file. Preserving all existing data.\n r = read, this will only allow reading of the file.\n x = open for exclusive creation, failing if the file already exists.\n + = open a file for updating (reading and writing)") # Write multiple lines to the file
    elif mode == "append": # Append a line to the file
        with open(Path(__file__).parent / "data.txt", "a") as file: # Open file in append mode
            file.write("\nThis line is appended to the file.") # Append a line to the file
    elif mode == "sort": # Sort and print the file contents
        with open(Path(__file__).parent / "data.txt", "r") as file: # Open file in read mode
            lines = file.readlines() # Read all lines into a list
            lines.sort() # Sort the list of lines
            print(lines) # Print the sorted list of lines

demo_file_manipulation("read") # Call the function to read the file
demo_file_manipulation("overwrite") # Call the function to overwrite the file
demo_file_manipulation("append") # Call the function to append to the file