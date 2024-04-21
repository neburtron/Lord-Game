import llm_interface
import Commands
import sys
import Value_Evaluation

class Talk:

    def __init__(self):
        
        # Values
        self.save = 0 
        # Temp static value, replace with get_save or something.
        # get save should ask for input, re ask if bad name, check if save file exists + asks for
        # confirmation if so, asks to create new save if not, else for both cases - ask to 
        # make new game / fresh save file W given name
        self.current_prompt_index = 0
        self.prompts = []
        self.array = []

        # If new game, current turn is 0
        if self.save == 0:
            self.turn = 0
            self.isturn1 = True
        else:
            self.get_turn()
            # Implement get turn number later

        # Get LLM's conversation directions, add it to the array, and 
        LLM_start_prompt = Commands.read("Conversation_Start_Prompt.txt")
        self.array_input("system","",LLM_start_prompt)
        self.get_prompts()

        first_prompt = self.get_next_prompt()
        self.relayprompt(first_prompt)

    def get_turn(self):
        # Implement later
        return 0

    def get_prompts(self):
        try:
            self.prompts = Commands.prompts('Prompts.json', self.save)
            # Just opens start prompts, add stuff for other prompts later
            if not self.prompts:
                Commands.printpure("Error: No prompts retrieved.")
                sys.exit(1)  # Exit program if prompts are not retrieved successfully
        except Exception as e:
            Commands.printpure(f"Error in prompt retrieval: {e}")
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
            Commands.printspace("First turn over, second turn not implemented yet. THE END.")

            Value_Evaluation.main(self.array)
            # @ end of turn, run the prepare next turn script. 
            sys.exit() # Remove when continuing to turn 2 is possible 

    def relayprompt(self, prompt):
       # Temp notation of current prompt
        Commands.printpure(self.current_prompt_index)

        # Check and print enter description if available
        if "EnterDesc" in prompt and prompt["EnterDesc"].strip():
            self.array_input("assistant", "Scene", prompt["EnterDesc"].strip())
            Commands.printpure(f"Scene: {prompt['EnterDesc'].strip()}")

        # Check and print text1 if available
        if "character" in prompt and "text1" in prompt and prompt["text1"].strip():
            self.array_input("assistant", prompt["character"], prompt["text1"].strip())
            Commands.printpure(f"{prompt['character']}: {prompt['text1'].strip()}")

        # Check and print text2 if available
        if "character" in prompt and "text2" in prompt and prompt["text2"].strip():
            self.array_input("assistant", prompt["character"], prompt["text2"].strip())
            Commands.printpure(f"{prompt['character']}: {prompt['text2'].strip()}")
        
        # Check and give LLM Notes if available
        if "notes" in prompt and prompt["notes"].strip():
            self.array_input("system", "notes", prompt["notes"].strip())
            # For LLM only

        self.user_input(self.isturn1)



    def user_input(self, first):
        # For the first prompt it's better if it skips the LLM alltogether.
        user_input = Commands.input1()
            
        if first == True:
            self.isturn1 = False
            self.array_input("user", "player", user_input)
            prompt = self.get_next_prompt()
            self.relayprompt(prompt)
        else:

            if user_input == "exit":  # Exit the program
                Commands.printspace("Are you sure you want to exit? Type yes to confirm.")
                confirm = Commands.input1()  # Get user confirmation
                if confirm == "yes":
                    sys.exit()
            elif user_input == "next":
                # Move on to next prompt
                self.array_input("user", "player", "next")
                prompt = self.get_next_prompt()
                self.relayprompt(prompt)
            else:
                # Send message to Array and send Array to LLM for response
                self.array_input("user", "player", user_input)
                self.llmresponse()

    def llmresponse(self):
        
        # Call LLM and get response
        llmresponse = llm_interface.main(self.array)
        if llmresponse:
            # Get role and content from llmresponse
            role = llmresponse.role
            content = llmresponse.content
                
            # Save what they said to conversation array, easy
            self.array_input(role, "", content)
                
            # Print the message for player
            Commands.printspace(f":{content}")

        self.user_input(0)

if __name__ == "__main__":
    talk_instance = Talk()