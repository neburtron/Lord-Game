import llm_interface
import commands
import find_commands

"""
Before anything, it's probably a good idea to format it so it's just one message W unified format W/O weird stuff


This script handles the array given to it by conversation.py


Step 1 - break down

1 - Seperate into prompts

2 - Break down what happened + remove fluff
 


It looks through the info and interprets it in two senses: 
1, immediate value changes + value changes per turn
2, story / lore / described changes / things that happened.

The first is shown to the player at an end screen
The second is used all over the place
The core of this game is the memory / lore system and I haven't even started it yet.

Break up log by the prompts

Give LLM job to interpret for values + the commands to do so
Interpret that
Pass along


Story Stuff
Go through each prompt and seperate each effect into it's own thing. Remove fluff and just do stuff that will have an effect
later down the line.
Additionally, make a list of newly established stuff. This might need to be handled as a different instance run before the
first depending on how taxing looking thorugh memory system is. Might be part of next step.

Report (next step)
Look through data logs and find what each change references / what that change is being done to. If it can't, assume it's new
and write a new txt file.

Get from last turn's data logs. Make new copy W new stuff ammended by LLM to keep them somewhat short. Have additional files
saved that tell you what happened that turn.

Story stuff is sent to distantsimulated.py too. Get the names of the txt files the impacted data logs corispond to and put
them in {}'s or something

Send a bunch of that stuff to the prompt generator section. I've been thinking about that one too, and I want it to interact
with things a lot more + for there to be representations of storylines / some percentage of new stuff, continuations, and 
unrelated / insignificant stuff.

Might have missed some stuff.

"""

def main(conversation, save, current_prompt_index, turn=0):
    commands.save(f"{save}/conversation_turn{turn}_prompt{current_prompt_index}.json", conversation)
    commands.printspace("saved text to json.")
    pass
    
    # Placeholder script that just writes array to json
    # Made it put it in selected save W turn number because why not
    
    # If there's not a folder that fits naming format W turn number, make it + change next bit to put new files in current folder
    # and also remove the turn part from the name...
