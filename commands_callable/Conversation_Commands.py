#from Conversation import Talk
import random
import llm_interface


"""

Commands to be implemented:

Next

Hidden Note available to LLM, but not player

run instance of LLM to evaluate cost of thing W factors added ()

Run instance of LLM again 
    - For cases like where LLM needs dice roll / thing's cost evaluated before responding
    - LLM should either say a bit of preamble or just have commands in their message if they're
        using this command. It shouldn't monologue, at least that often. 

        
Insight check - check if thing player says is a lie from looking at prevous turn's stored data.

"""

# Empty
def Next():
    return 
    # call next command from Conversation.py 

# Done
def Roll_Dice(sides):
    X = random.randrange(1, sides)
    return (X)

# Empty
def Hidden_Note(text):
    return
    # Change Conversation.py's relay prompt thing so that it handles all stuff printed
    # besides user input, streamline process, and have this have the same behavior as notes
    # section from prompts.

# Empty
def Evaluate_Cost(prompt):
    valuesdoc = ("values.txt") # Doesn't exist
    return
    # Run instance of LLM who's job is just to look at rates for buying power of different core values
    # and return a reasonable rate for this or that thing.

# Empty
def Wait_for_Commands():
    return 
