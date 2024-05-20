import os
import sys
import commands
from conversation import Talk

class Prompts:
    def __init__(self, save):
        self.save = save
        self.new_save = False
        self.directory = f"saves/{save}"

        turnfile = "turn.txt"
        turn = os.path.join(self.directory, turnfile)
        if os.path.exists(turn):
            self.new_save = False
            self.turn = commands.read(turn)
        else:
            self.new_save = True
            commands.save_txt(turn, "1")

        self.check_prompts()

    def check_prompts(self):
        if self.new_save:
            self.prompts_file = "prompts.json"
            self.relay()
        else:
            self.prompts_file = os.path.join(self.directory, "prompts.json")
            if os.path.exists(self.prompts_file):
                self.relay()
            else:
                self.generate()

    def generate(self):
        # Implement logic to generate prompts
        self.relay()

    def relay(self):
        try:
            data = commands.load(self.prompts_file)
            if data is not None and isinstance(data, dict):
                self.prompts_list = data.get("prompts", [])
            else:
                commands.printpure("Error: No prompts retrieved.")
                sys.exit(1)
        except Exception as e:
            commands.printpure(f"Error in prompt retrieval: {e}")
            sys.exit(1)

        Talk_Instance = Talk(self.save, self.new_save, self.prompts_list)

if __name__ == "__main__":
    instance = Prompts(90)