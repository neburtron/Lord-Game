import sys
import value_evaluation
import llm_interface
import commands

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

        # Temp, done right in rewrite
        self.turn = 0
        self.isturn1 = True
        
        first_prompt = self.get_next_prompt()
        self.relayprompt(first_prompt)

        # Get LLM's conversation directions, add it to the array, and get prompts 
        LLM_start_prompt = commands.read_file("conversation_start_prompt.txt")
        self.array_input("system","",LLM_start_prompt)
 

    def array_input(self,thing,character,msg):
        if character:
            self.array.append({"role": thing, "content": character + ": " + msg})
        else:
            self.array.append({"role": thing, "content": msg})

    def get_next_prompt(self):
        #check if there's more prompt
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index] # Continue to next prompt
            self.current_prompt_index += 1  # Move to the next prompt for the next call
            
            value_evaluation.main(self.array, self.save, self.current_prompt_index)
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

        self.user_input()

    def user_input(self):

        user_input = commands.input1()

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
        llmresponse = llm_interface.main(self.array)
        if llmresponse:
            # Get content from llmresponse
            content = llmresponse.content
            
            # Save what they said to conversation array
            self.array_input("assistant", "", content)
            
            # Print for player
            commands.printspace(f":{content}")

        self.user_input()

