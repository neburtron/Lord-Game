import Call_LLM
import json
# Seperate different bits @ "user: next" + "user: end", or thing to same effect.
# Then call LLM W Evaluate this prompt
# Then interpret that as a series of called commands + run those commands
# Similar script could be made for context, but I have no idea how I want to tackle that.

def main(conversation): #temp
    with open('conversation.json', 'w') as f:
        json.dump(conversation, f, indent=4)
    print("Conversation saved to conversation.json.")

# Save the list as file is just a placeholder, probably not nessisary in final doc.
# Needed something to do with array from TempTerminal.py