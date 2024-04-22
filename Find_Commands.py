import Commands

# Import all scripts in Commands folder either manually or automatically detect them. 

"""

How each should work:
0 - open whatever commands file + get list of functions in it
1 - go through list + search for {}'s, adding to array (or other formatting used to indicate command)
2 - save copy of text without commands
3 - go through list of commands, if it's in the list issue commands
4 - when it gets to the end + command not recognized, print it,
    or return all failed seperately + have parent script deal with it.
    If parent script handles it, there is the potential to call LLM again + have it try something else.
    easier if done in parent script because here you'd need to hand over more variables than
    would otherwise be nessisary.

"""


def main(LLM_Output, scriptname="Conversation_Commands"):

    #commands = ("Commands/{scriptname}.py")

    # I don't have internet right now, change this so that instead of being the file location
    # commands = the list of function names for scriptname 


    # Go through LLM_Output, find all the commands issued
    # for all the commands, check which command they are
    # Then run that coresponding function
    # Then save input + whatever else needed

    # Save all to array or something W command name + variables for script, and return that to parent script
    # Then have a bit in parent script interpeting all of that.


    return
