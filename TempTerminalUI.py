# This is a working demo of the most basic and underdeveloped form of my idea. 
# You get the prompt, then the LLM responds.


# Next steps would be:
# Taking the raw output and making it not raw + adding to conversation array
# Adding the context stuff hidden from the user + writing that out
# A start to the rigid structure that is the main bit of this idea
# User + LLM callable commands
# End of conversation + moving on to next (includes starting with the first + second prompts and going through rest one by one)
# Interpreting the converstaion stuff, list of commands, storing values, and all that stuff
# Moving on to the next turn + writing new scripts + continuing storylines along + memory
# Saves system + store all the prevous turn data
# GUI
# Eat Caviar with elon musk and Carniegie


import json
import Call_LLM
import random

# Load prompts from JSON file
with open('prompts.json') as f:
    data = json.load(f)

# Choose a random prompt
prompt = random.choice(data["prompts"])

conversation = []

# Print initial prompt
print(prompt["character"])
print(prompt["EnterDesc"])
print(prompt["text1"])
print(prompt["text2"])
print()


if prompt["character"]:
    conversation.append({"role":"system", "content": prompt["character"] + ": " + prompt["EnterDesc"]})

# Add system prompt
if prompt["character"]:
    conversation.append({"role": "system", "content": prompt["character"] + ": " + prompt["text1"]})

# Add second system prompt if text2 exists
if prompt["text2"]:
    conversation.append({"role": "system", "content": prompt["character"] + ": " + prompt["text2"]})

# Get user input
user_input = input()

# Add user input to conversation
conversation.append({"role": "user", "content": "player: " + user_input})

# Convert conversation to JSON format
conversation_json = json.dumps(conversation)

#Call the LLM main function with the conversation
LLM = Call_LLM.main(conversation_json)

print(LLM)

