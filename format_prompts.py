import commands
from conversation import Talk
import os
import sys

"""

- Figure out what goes into prompts.json in final thing
- Edit start prompts.json 
- Fix commands.prompts
- finish this script
- Implement into working build (change main.py and conversation.py)

That's about all that's needed for implementing this into the working build.
When I'm ready to write things to get the working build past turn 1, I'll expand this script.
Setting things up to make things easier later.

"""

class Prompts:

    def __init__(self, save, new_save):
        
        self.save = save
        self.new_save = new_save
        self.directory = f"saves/{save}"
        self.turn = 0

        self.check_prompts()

    def check_prompts(self):
        if self.new_save == True:
            self.relay(True)
        else:
            prompts_file = os.path.join(self.directory, "prompts.json")
            if os.path.exists(prompts_file):
                self.relay(False)
            else:
                self.generate()

    def generate(self):
        # Get data + send to write prompts script
        # Then run relay
        self.relay(False)


    def relay(self, newsave):
        try:
            self.prompts = commands.prompts(self.save, self.turn)
            # Run the get prompts command from commands.py. Rewrite at some point
            if not self.prompts:
                commands.printpure("Error: No prompts retrieved.")
                sys.exit(1)  # Exit program if prompts are not retrieved successfully
        except Exception as e:
            commands.printpure(f"Error in prompt retrieval: {e}")
            sys.exit(1)  # Exit program for any other unexpected errors

        Talk_Instance = Talk(self.save, self.new_save, self.prompts)



if __name__ == "__main__":
    instance = Prompts(0, True)