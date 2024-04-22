import llm_interface
import Commands
import Find_Commands
# Seperate different bits @ "user: next" + "user: end", or thing to same effect.
# Then call LLM W Evaluate this prompt
# Then interpret that as a series of called commands + run those commands
# Similar script could be made for context, but I have no idea how I want to tackle that.


def main(conversation, save): 
    # Placeholder script that just writes array to json
    # Made it put it in selected save W turn number because why not
    Commands.save("{save}/conversation_Turn{turn}.json", conversation)
    print("conversation saved to conversation.json.")

