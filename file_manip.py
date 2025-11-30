# file_manip.py
# This script demonstrates file manipulation in Python including reading, writing, and appending to files.
# It also shows how to use the pathlib module to handle file paths.
# The script performs the following operations:
# 1. Reads a file line by line and prints each line in uppercase.
# 2. Writes multiple lines to a file, demonstrating the use of write mode.  
# 3. Reads the file again, sorts the lines, and prints the sorted list.
from pathlib import Path # Import Path from pathlib module
def demo_file_manipulation(): # Define the main function
    with open(Path(__file__).parent / "data.txt", "r") as file: # Open file in read mode
        for line in file: # Iterate through each line in the file
            print(line.strip().upper()) # Print each line in uppercase, stripping whitespace
    with open(Path(__file__).parent / "data.txt", "w") as file: # Open file in write mode
        file.write("Path(__file_).parent / 'data.txt' returns current file (This one)'s file path then appends the file we are wanting to open to it. \n Options have to be followed to avoid issues: \n w = write, this will overright all data with new data using the file.write command.\n a = append, this will add to the end of the file. Preserving all existing data.\n r = read, this will only allow reading of the file.\n") # Write multiple lines to the file
    with open(Path(__file__).parent / "data.txt", "r") as file: # Open file in read mode
        lines = file.readlines() # Read all lines into a list
        lines.sort() # Sort the list of lines
        print(lines) # Print the sorted list of lines
