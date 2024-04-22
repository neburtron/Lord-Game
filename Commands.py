import json
import os


def save(filename, contents):
    # Save contents to a file. Supports dictionaries, other types are written directly.
    try:
        with open(filename, 'w') as f:
            if isinstance(contents, dict):
                json.dump(contents, f, indent=4)
            else:
                f.write(str(contents))
    except (IOError, PermissionError) as e:
        print(f"Error saving to {filename}: {e}")

def load(filename):
    # Load contents from a file.
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
        return None

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

def read(filename):
    # Read contents from a file.
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ''
    




def prompts(save, turn=0):
    filename = "Prompts.json"
    if turn == 0:
        # Use the provided filename directly
        file = filename
    else:
        file = filename
        # If there's a file named prompts.json in saves/{save}/prompts, save that path as file var
        # If not call the make prompts script before saving same path as file var

    # Use the load function to load JSON data
    data = load(file)
    if data is not None and isinstance(data, dict):
        return data.get("prompts", [])
    else:
        return []

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


