import sys
import os

import llm_interface
import find_commands
import commands


"""
Still needs to be done:

LLM interaction + commands
- I still need to figure out formatting + rework for HuggingFace or whatever

All the scripts that the original conversation.py interacts with + whatever 
new ones need to be written / rewritten

Rewrite prompts

I need to figure out save template + how that's gonna be organized + set all 
that stuff up

I'd like to make a flowchart that goes over how this thing works. Might decide 
against it, but might not at the same time.

Commands
"""


class Talk:

    def __init__(self, save, prompts, prompts_num):
        
        # Make all input vars accessible by whole class
        self.save = save
        self.prompts = prompts
        self.prompts_num = prompts_num

        # Setup non-input vars
        self.current_prompt_index = 0
        self.array = []
        self.turn = 0
        self.isturn1 = False

        # Get data from files
        self.instruct = commands.load_json("conversation_start_prompt.txt")
        self.get_turn()

    def get_turn(self):
        try:
            with open(os.path.join('saves', self.save, 'turn.txt'), 'r') as file:
                self.turn = int(file.read().strip()) 
        except FileNotFoundError:
            print(f"\nError: turn.txt for save '{self.save}' not found\n") 
            sys.exit(1)
        except ValueError:
            print(f"\nError: turn.txt contains invalid data for save '{self.save}'\n")
            sys.exit(1)

        if self.turn == 0:
            self.isturn1 = True
        else:
            self.isturn1 = False

    def run(self):
        while self.current_prompt_index < len(self.prompts):
            self.reset_turn()
            self.run_turn()
        self.reset_turn()
        # If not called by parent after this script is done, call next script here. 
  
    def reset_turn(self):
        file_path = os.path.join('saves', self.save, f'turn{self.turn}', 'conversation', f'{self.current_prompt_index}.txt')
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Save the array to a JSON file
            commands.save_json("file_path", self.array)
            
            # Clear the array
            self.array.clear()
            
            # Add starting instruction to array
            self.array.append(self.instruct)
            self.prompt = self.get_next_prompt()
            self.array.append(self.prompt)
            commands.printpure(self.prompt) # change this later. 

        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)
            sys.exit(1)        
        
    def run_turn(self):
        """
        Whole bunch of stuff here, use nested functions
        """
        return

    def get_next_prompt(self):
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index]
            self.current_prompt_index += 1
            return next_prompt
        return None

if __name__ == "__main__":
    Instance = Talk("", "", "")
    Instance.run()