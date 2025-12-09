import os

def file_manipulation_example(file_path, mode):
    """
    This function demonstrates basic file manipulation operations:
    creating a file, writing to it, reading from it, and deleting it.
    
    :param file_path: The path where the file will be created.
    """
    # Create and write to the file
    if(mode == "write"):
        with open(file_path, 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
    # Read from the file
    if(mode == "read"):
        if(os.path.exists(file_path)):
            with open(file_path, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        else:
            print(f"File: '{file_path}' does not exist. Please create it first by running this function again with mode='write'.")
    # Delete the file
    if(mode == "delete"):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
file_manipulation_example(os.getcwd() + "/test_file.txt", "read")
file_manipulation_example(os.getcwd() + "/test_file.txt", "write")