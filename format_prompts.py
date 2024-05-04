import commands
from conversation import Talk
import os

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
        self.check_prompts()

    def check_prompts(self):
        if self.new_save == True:
            self.relay(True)
        else:
            prompts_file = os.path.join(self.directory, self.save, "prompts.json")
            if os.path.exists(prompts_file):
                self.relay(False)
            else:
                self.generate()

    def generate(self):
        # Get data + send to write prompts script
        # Then run relay

        self.relay(False)
 
    def relay(self, newsave):
        prompt = commands.prompts() # Prompts command should be rewritten 
        Talk_Instance = Talk(prompt) # remove the old get prompt stuff from this script + save var from here.
        pass

