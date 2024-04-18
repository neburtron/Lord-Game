import Call_LLM
import Commands
# Seperate different bits @ "user: next" + "user: end", or thing to same effect.
# Then call LLM W Evaluate this prompt
# Then interpret that as a series of called commands + run those commands
# Similar script could be made for context, but I have no idea how I want to tackle that.


def main(conversation): # Placeholder script that just writes array to json
    Commands.save("conversation.json", conversation)
    print("conversation saved to conversation.json.")

