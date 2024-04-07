
# What ChatGPT said to do to import a script 2 layers up, I don't know if this is the best way to do it.
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
two_levels_up = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(two_levels_up)

import Next_Turn
import json

turn_number = 5 # Temp
Turn_Json = "Every_Turn.json"

# Temp 
values = [
    {"Treasury": 10},
    {"Population": 10},
    {"Stability": 10},
    {"Authority": 10},
    {"Civilian_wellbeing": 10},
    {"Public_Opinion": 10},
]

def get_values():
    return values # replace with proper data storage / whatever.


def change_values():
    # Write file thing used to save values for turn / whatever
    with open ('turns/turn' + str(turn_number) + '.txt', 'w') as f:
        f.write(str(values))

    # Read values from Every_turn.json
    try:
        with open(Turn_Json) as f:
            changes = json.load(f).get("Effects",[]) # Get the effects
    except FileNotFoundError:
        print("Error: Every_Turn.json file not found.")
        changes = []

    # Send to Next_Turn.py # Does the actual next turning
    # I don't know why I was thinking to have this as it's own script
    # I'm going to leave it for now. 
    Next_Turn.main(values, changes)


if __name__ == "__main__":
    # Call the get_values() function and capture its result
    retrieved_values = get_values()
    print("Treasury:", retrieved_values[0]["Treasury"])