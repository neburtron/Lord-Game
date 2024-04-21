import json

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

def prompts(filename, save=0):
    # Load prompts from a specific save file or default file.
    # This is nonsense, fix it later.
    # replace 0 with if it's a new saves file or not, new var, taken when called.
    if save == 0:
        filename = 'Prompts.json'
    else:
        save_filename = f'save{save}.txt'
        filename = f'save/{save_filename}'
    try:
        with open(filename) as f:
            return json.load(f).get("prompts", [])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
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
