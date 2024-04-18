import llm_interface
import Commands
import sys
import Value_Evaluation

"""
    This is the main script for this project. I'm rewriting it now, and thought I would explain
    how it works.

    __init__ is the starting script. It sets / resets some stats, and will
    start whatever needs to be started, when I get around to that.'

    Get turn has not been implemented yet. When implemented it'll look for the save with the highest number
    in the format "save" + number + ".txt", then from there whatever I decide to do for turns after turn 1
    should fire.

    Next is get prompts. I haven't implemented making save files or getting prompts from variable sources,
    right now it just gets them from Prompts.json.
    Error cases and whatnot, actual json stuff in Commands.py or whatever I renamed it to. 
    Exits if it can't open it because for now that just makes more sense.

    Array template copied from previous version. Just a callable thing that has the template for how data
    should be input into the array.

    Next prompt also copied from previous version. Called to print + add to array the next prompt if there
    is a next prompt, if not, shut things down. Should change at some point. 

    ...

    Notes:
    
    make save file script / add to Commands.py, import if it's own script.
        Script should copy from template

    Double check relay command, I don't think I added the notes section, I think I got everything else but I'm not sure.
    
    I should seperate the terminal stuff from the actual conversation stuff here, either in a script that 
    calls this / a script that this calls so that it's easier to add a GUI



"""

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

    def relayprompt(self, prompt):
       # Temp notation of current prompt
        print(self.current_prompt_index)

        # Check and print enter description if available
        if "EnterDesc" in prompt and prompt["EnterDesc"].strip():
            self.array_input("assistant", "Scene", prompt["EnterDesc"].strip())
            print(f"Scene: {prompt['EnterDesc'].strip()}")

        # Check and print text1 if available
        if "character" in prompt and "text1" in prompt and prompt["text1"].strip():
            self.array_input("assistant", prompt["character"], prompt["text1"].strip())
            print(f"{prompt['character']}: {prompt['text1'].strip()}")

        # Check and print text2 if available
        if "character" in prompt and "text2" in prompt and prompt["text2"].strip():
            self.array_input("assistant", prompt["character"], prompt["text2"].strip())
            print(f"{prompt['character']}: {prompt['text2'].strip()}")

        self.user_input()

    def user_input(self):
        # Remove "You: " added for aesthetics
        # then make lowercase + check for commands

        user_input = input("You: ").strip().lower()

        if user_input == "exit":  # Exit the program
            print()
            print("Are you sure you want to exit? Type yes to confirm.")
            print()
            confirm = input().strip().lower()  # Get user confirmation
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
            print()
            print(f":{content}")
            print()

        self.user_input()

if __name__ == "__main__":
    talk_instance = Talk()