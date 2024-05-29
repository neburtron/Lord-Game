import json
import os

def save_txt(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"Error occurred: {e}")

def save_json(filename, contents):
    try:
        with open(filename, 'w') as f:
            json.dump(contents, f, indent=4)
    except (IOError, PermissionError) as e:
        print(f"Error saving to {filename}: {e}")

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
        return None

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ''

def append(filename, contents):
    # Append contents to a file. Supports appending dictionaries in JSON format.
    try:
        with open(filename, 'a') as f:
            if isinstance(contents, dict):
                json.dump(contents, f)
                f.write('\n')
            else:
                f.write(str(contents) + '\n')
    except (IOError, PermissionError) as e:
        print(f"Error appending to {filename}: {e}")

def load_last_tab_index(Settings_Folder):
    try:
        with open(os.path.join(Settings_Folder, "last_tab_index.txt"), "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


def printspace(thing):
    print()
    print(thing)
    print()

def printpure(thing):
    print(thing)

def input1():
    print()
    input2 = input("you: ").strip().lower()
    print()
    return input2

def list_saves():
    folder_names = []
    directory_path = "saves"
    
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return folder_names
    
    try:
        # Get a list of all items (files and directories) in the specified directory
        items = os.listdir(directory_path)
        
        # Iterate over each item
        for item in items:
            item_path = os.path.join(directory_path, item)

            # Check if the item is a directory
            if os.path.isdir(item_path):
                folder_names.append(item)  # Add the directory name to the list
    
    except OSError as e:
        print(f"Error: Unable to list contents of directory '{directory_path}'.")
        print(e)
    
    return folder_names