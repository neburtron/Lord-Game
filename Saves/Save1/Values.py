
# What ChatGPT said to do to import a script 2 layers up, I don't know if this is the best way to do it.
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
two_levels_up = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(two_levels_up)

import Next_Turn
import json

turn_number = 5
Turn_Json = "Every_Turn.json"

# Current values temporarally set here static. 
values = [
    {"Treasury": 10},
    {"Population": 10},
    {"Stability": 10},
    {"Authority": 10},
    {"Civilian_wellbeing": 10},
    {"Public_Opinion": 10},
]

def get_values():
    return values


def main(conversation): #temp
    with open('conversation.json', 'w') as f:
        json.dump(conversation, f, indent=4)  # Use indentation for readability
    print("Conversation saved to conversation.json.")


def change_values():
    # Run command to save current values in turns folder, turn number, new txt file

    with open ('turns/turn' + str(turn_number) + '.txt', 'w') as f:
        f.write(str(values))
    


    # Read values from Every_turn.json
    try:
        with open(Turn_Json) as f:
            changes = json.load(f).get("Effects",[])
    except FileNotFoundError:
        print("Error: Every_Turn.json file not found.")
        changes = []

    # Send to Next_Turn.py # Does the actual next turning
    Next_Turn.main(values, changes)


if __name__ == "__main__":
    # Call the get_values() function and capture its result
    retrieved_values = get_values()
    print("Treasury:", retrieved_values[0]["Treasury"])



change_values()