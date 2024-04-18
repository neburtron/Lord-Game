import Call_LLM
import Commands
import sys
import Value_Evaluation


"""
    This is the main script for this project. I'm rewriting it now, and thought I would explain
    how it works. (if you're reading this I forgot to go back and write this...)



"""

class Talk:

    def __init__(self):
        
        # Values
        self.save = 0
        self.current_prompt_index = 0
        self.prompts = []
        self.array = []

        # If new game, current turn is 0
        if self.save == 0:
            self.turn = 0
        else:
            self.get_turn()
            # Implement get turn number later

        # Get LLM's conversation directions, add it to the array, and 
        LLM_start_prompt = Commands.read("Conversation_Start_Prompt.txt")
        self.array_input("system","",LLM_start_prompt)
        self.get_prompts()


    def get_turn(self):
        # Implement later
        return 0


    def get_prompts(self):
        try:
            self.prompts = Commands.prompts('Prompts.json', self.save)
            # Just opens start prompts, add stuff for other prompts later
            if not self.prompts:
                print("Error: No prompts retrieved.")
                sys.exit(1)  # Exit program if prompts are not retrieved successfully
        except Exception as e:
            print(f"Error in prompt retrieval: {e}")
            sys.exit(1)  # Exit program for any other unexpected errors
    
    def array_input(self,thing,character,msg):
            if thing:
                self.array.append({"role": thing, "content": character + ": " + msg})
            else:
                self.array.append({"role": thing, "content": msg})

            """
            Just for putting stuff in Array
            Checks to see if the name + message are seperate, and combines them if they are not.
            This is a thing because OpenAI API only accepts User, System, and Assistant... 
            for my setup at least.
            """

    def get_next_prompt(self):
        #check if there's more prompt
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index] # Continue to next prompt
            self.current_prompt_index += 1  # Move to the next prompt for the next call
            return next_prompt
        else:
            print()
            print("First turn over, second turn not implemented yet. THE END.")

            Value_Evaluation.main(self.array)
            # @ end of turn, run the prepare next turn script. 
            sys.exit() # Remove when continuing to turn 2 is possible 
            


    
            
    




if __name__ == "__main__":
    talk_instance = Talk()