import Call_LLM
import json
# Seperate different bits @ user: next + user: end, or thing to same effect.
# Then do the evaluation...
# Similar script could be made for context, but I have no idea how I want to tackle that.

def main(conversation): #temp
    with open('conversation.json', 'w') as f:
        json.dump(conversation, f, indent=4)  # Use indentation for readability
    print("Conversation saved to conversation.json.")

# Took this from the TempTerminalRewrite script because it makes more sense to be here as a template
# For something to do W input before implementaiton of the seperating of prompts and eval + whatever else.





