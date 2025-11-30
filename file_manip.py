from pathlib import Path
with open(Path(__file__).parent / "data.txt", "r") as file:
    for line in file:
        print(line.strip().upper())
with open(Path(__file__).parent / "data.txt", "a") as file:
    file.write("Path(__file_).parent / 'data.txt' returns current file (This one)'s file path then appends the file we are wanting to open to it. \n Options have to be followed to avoid issues: \n w = write, this will overright all data with new data using the file.write command.\n a = append, this will add to the end of the file. Preserving all existing data.\n r = read, this will only allow reading of the file.\n")
with open(Path(__file__).parent / "data.txt", "r") as file:
    lines = file.readlines()
    lines.sort()
    print(lines)