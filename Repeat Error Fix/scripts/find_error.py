#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    # Using 'with' handles file closing automatically
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file:
            # Create a simple list of lowercase words to find
            search_words = error.lower().split()
            search_words.append("error") 
            
            # Check if every search word exists in the current log line
            if all(word in log.lower() for word in search_words):
                returned_errors.append(log)
    return returned_errors
  
def file_output(returned_errors):
    output_path = os.path.expanduser('~') + '/data'
    # Ensure the directory exists before writing
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    with open(output_path + '/errors_found.log', 'w', encoding='UTF-8') as file:
        for error in returned_errors:
            file.write(error)

if __name__ == "__main__":
    # 1. Get the absolute path to THIS script (find_error.py)
    script_path = os.path.abspath(__file__)
    
    # 2. Go up one level to the 'scripts' folder
    script_dir = os.path.dirname(script_path)
    
    # 3. Go up one more level to the project root
    project_root = os.path.dirname(script_dir)
    
    # 4. Construct the path to the 'data' sibling folder
    data_dir = os.path.join(project_root, 'data')

    # 5. Get the filename from the user (e.g., 'fishy.log')
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        # Combine the data directory with the specific filename
        log_file = os.path.join(data_dir, target_file)
        
        # Safety Check: Does the file actually exist?
        if os.path.exists(log_file):
            returned_errors = error_search(log_file)
            file_output(returned_errors)
        else:
            print(f"Error: Could not find {target_file} in {data_dir}")
    else:
        print("Usage: ./find_error.py <filename>")

    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)