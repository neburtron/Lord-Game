import llm_interface
import commands
import sys
import value_evaluation
import find_commands

class Talk:

    def __init__(self, save, newsave, prompts):
        # Main.py should call format_prompts + feed info in from there including prompts

        # Values
        self.save = save
        self.current_prompt_index = 0
        self.prompts = []
        self.array = []
        self.newsave = newsave

        self.prompts = prompts

        try:
            self.prompts = commands.prompts(self.save, self.turn)
            # Run the get prompts command from commands.py
            if not self.prompts:
                commands.printpure("Error: No prompts retrieved.")
                sys.exit(1)  # Exit program if prompts are not retrieved successfully
        except Exception as e:
            commands.printpure(f"Error in prompt retrieval: {e}")
            sys.exit(1)  # Exit program for any other unexpected errors


        first_prompt = self.get_next_prompt()
        self.relayprompt(first_prompt)

        # If new game, current turn is 0
        if newsave == True:
            self.turn = 0
            self.isturn1 = True
        else:
            self.turn = self.get_turn()
            self.isturn1 = False
            # Implement get turn number later

        # Get LLM's conversation directions, add it to the array, and get prompts 
        LLM_start_prompt = commands.read("conversation_start_prompt.txt")
        self.array_input("system","",LLM_start_prompt)


    def get_turn(self):
        # implement later
        self.isturn1 = True
        return 0    

    def array_input(self,thing,character,msg):
            if character:
                self.array.append({"role": thing, "content": character + ": " + msg})
            else:
                self.array.append({"role": thing, "content": msg})

            """
            Just for putting stuff in Array
            Checks to see if the name + message are seperate, and combines them if they are not.
            Character seperate from thing because LLM only accepts System, User, and Assistant for
            the person saying the message, and character names are important.
            """

    def get_next_prompt(self):
        #check if there's more prompt
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index] # Continue to next prompt
            self.current_prompt_index += 1  # Move to the next prompt for the next call
            
            value_evaluation.main(self.array, self.save, self.turn, self.current_prompt_index)
            self.array = []
            # This should work, but I'm rewriting a bunch of this project and am not going to test it
            # for a little bit.

            return next_prompt
        
        else:
            commands.printspace("First turn over, second turn not implemented yet. THE END.")

            value_evaluation.main(self.array, self.save, self.turn, self.current_prompt_index)
            # @ end of turn, run the prepare next turn script. 
            #sys.exit()
            commands.printpure ("Out of prompts, that's all I've got for now. If you want you can run it again with the same prompts or play around with prompts.json.")


    def relayprompt(self, prompt):
       # Temp notation of current prompt
        commands.printpure(self.current_prompt_index)

        # Check and print enter description if available
        if "EnterDesc" in prompt and prompt["EnterDesc"].strip():
            self.array_input("system", "Scene", prompt["EnterDesc"].strip())
            commands.printpure(f"Scene: {prompt['EnterDesc'].strip()}")

        # Check and print text1 if available
        if "character" in prompt and "text1" in prompt and prompt["text1"].strip():
            self.array_input("system", prompt["character"], prompt["text1"].strip())
            commands.printpure(f"{prompt['character']}: {prompt['text1'].strip()}")

        # Check and print text2 if available
        if "character" in prompt and "text2" in prompt and prompt["text2"].strip():
            self.array_input("system", prompt["character"], prompt["text2"].strip())
            commands.printpure(f"{prompt['character']}: {prompt['text2'].strip()}")
        
        # Check and give LLM Notes if available
        if "notes" in prompt and prompt["notes"].strip():
            self.array_input("system", "notes", prompt["notes"].strip())
            # For LLM only

        self.user_input(self.isturn1)



    def user_input(self, first):
        # For the first prompt it's better if it skips the LLM alltogether.
        user_input = commands.input1()
            
        if first == True:
            self.isturn1 = False
            self.array_input("user", "player", user_input)
            prompt = self.get_next_prompt()
            self.relayprompt(prompt)
        else:

            if user_input == "exit":  # Exit the program
                commands.printspace("Are you sure you want to exit? Type yes to confirm.")
                confirm = commands.input1()  # Get user confirmation
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
            # Get content from llmresponse
            content = llmresponse.content

            # Save what they said to conversation array
            self.array_input("assistant", "", content)

            """
            WIP
            CommandsList = find_commands.main(content,"Conversation_Commands")
            for command in CommandsList:
                print (command)
            """

            # Print the message for player
            commands.printspace(f":{content}")


        self.user_input(0)

if __name__ == "__main__":
    talk_instance = Talk(0)