import json

def Save(filename, contents): #temp
    with open(filename, 'w') as f:
        if isinstance(contents, dict):
            json.dump(contents, f, indent=4)
        else:
            f.write(contents)

def Load(filename): #temp
    with open(filename, 'r') as f:
        contents = json.load(f)
    return contents

def Append(filename, contents):
    with open(filename, 'a') as f:
        if isinstance(contents, dict):
            # Serialize the dictionary to JSON and append to file
            json.dump(contents, f)
            f.write('\n')  # Add a newline to separate JSON objects
        else:
            # Write other types directly to the file
            f.write(str(contents) + '\n')

def Read(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

