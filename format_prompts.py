import commands
from conversation import Talk
import os
import sys

"""


- Figure out what goes into prompts.json in final thing
- Edit starting prompts.json 
- other stuff

"""

class Prompts:

    def __init__(self, save, new_save):
        
        self.save = save
        self.new_save = new_save
        self.directory = f"saves/{save}"
        self.turn = 0 # temp

        self.check_prompts()

    def check_prompts(self):
        if self.new_save == True:
            self.relay()
        else:
            prompts_file = os.path.join(self.directory, "prompts.json")
            if os.path.exists(prompts_file):
                self.relay()
            else:
                self.generate()

    def generate(self):
        # Get data + send to write prompts script
        # Then run relay
        self.relay()

    
    def prompts(self,filename="prompts.json"):
        folder = "saves"

        if self.turn == 0:
            # Use the provided filename directly
            file = filename
        else:
            file = os.path.join(folder, filename)

            # Change this later so that:
            # If there's a file named prompts.json in saves/{save}/prompts, save that path as file var
            # If not call the make prompts script before saving same path as file var
        
        # Use the load function to load JSON data
        data = commands.load(file)
        
        if data is not None and isinstance(data, dict):
            return data.get("prompts", [])
        else:
            return []


    def relay(self):
        try:
            self.prompts_list = self.prompts()
            if not self.prompts_list:
                commands.printpure("Error: No prompts retrieved.")
                sys.exit(1)  # Exit program if prompts are not retrieved successfully
        except Exception as e:
            commands.printpure(f"Error in prompt retrieval: {e}")
            sys.exit(1)  # Exit program for any other unexpected errors

        Talk_Instance = Talk(self.save, self.new_save, self.prompts_list)

if __name__ == "__main__":
    instance = Prompts(90, True)
