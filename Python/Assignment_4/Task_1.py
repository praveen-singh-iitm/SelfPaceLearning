
file_name="Sample.txt"
try:
    with open(file_name,"r") as file:
        print(f"Line 1: {file.readline().strip()}")
        print(f"Line 2: {file.readline().strip()}")
        print(f"Line 3: {file.readline().strip()}")
except FileNotFoundError:
    print(f"Error: The File {file_name} was not found")