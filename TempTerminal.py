# Write your own LLM prompt for now. I wrote the current one while testing script to see if it worked.
# I suggest starting W telling it to write just a few sentences tops, and what it's job is.

import json
import Call_LLM
import Value_Evaluation
import Commands

class Conversation:

    def __init__(self, prompts_file='prompts.json'):
        
        # Get prompts from prompts JSON
        self.prompts = []
        try:
            with open(prompts_file) as f:
                self.prompts = json.load(f).get("prompts", [])
        except FileNotFoundError:
            print("Error: prompts.json file not found.")
            self.prompts = [] 
        
        # set stuff used elsewhere
        self.conversation = []
        self.current_prompt_index = 0
        LLM_start_prompt = Commands.Read("Start_Prompt.txt")
        self.Array_Input("system","",LLM_start_prompt)
        # give the LLM it's start prompt before anything else

        if self.prompts:
            first_prompt = self.get_next_prompt()
            if first_prompt:
                self.relayprompt(first_prompt)
            else:
                print("No prompts available.")
        else:
            print("No prompts found in prompts.json.")
        # Run relayprompt command for first prompt, or don't if there's a problem.


    def get_next_prompt(self):
        #check if there's more prompt
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index] # Continue to next prompt
            self.current_prompt_index += 1  # Move to the next prompt for the next call
            return next_prompt
        else:
            Value_Evaluation.main(self.conversation)
            # End of turn, run eval script
            # Then prepare for next turn
            # Then this script will run again with new prompts


    def relayprompt(self, prompt):
       # Temp notation of current prompt
        print(self.current_prompt_index)

        # Check and print enter description if available
        if "EnterDesc" in prompt and prompt["EnterDesc"].strip():
            self.Array_Input("assistant", "Scene", prompt["EnterDesc"].strip())
            print(f"Scene: {prompt['EnterDesc'].strip()}")

        # Check and print text1 if available
        if "character" in prompt and "text1" in prompt and prompt["text1"].strip():
            self.Array_Input("assistant", prompt["character"], prompt["text1"].strip())
            print(f"{prompt['character']}: {prompt['text1'].strip()}")

        # Check and print text2 if available
        if "character" in prompt and "text2" in prompt and prompt["text2"].strip():
            self.Array_Input("assistant", prompt["character"], prompt["text2"].strip())
            print(f"{prompt['character']}: {prompt['text2'].strip()}")

        self.user_input()




    def Array_Input(self,thing,person,msg):
        if person:
            self.conversation.append({"role": thing, "content": person + ": " + msg})
        else:
            self.conversation.append({"role": thing, "content": msg})
        # Just the format for putting stuff in Array
        # Checks to see if the name + message are seperate, and combines them if they are not.
        # This is a thing because OpenAI API only accepts User, System, and Assistant... for my setup at least.


    def user_input(self):
        # Remove "You: " added to line of user input before user input
        # then make lowercase + check for commands

        user_input = input("You: ").strip().lower()

        if user_input == "exit":  # Exit the program
            Value_Evaluation.main(self.conversation)
            return
        elif user_input == "next":  # Move on to next prompt
            self.Array_Input("user", "player", "next")
            prompt = self.get_next_prompt()
            if prompt:
                self.relayprompt(prompt)
            else:
                print("Out of Prompts")
        else:
            # Send message to Array and send Array to LLM for response
            self.Array_Input("user", "player", user_input)
            self.llmresponse()

    def llmresponse(self):
        try:
            # Call LLM and get response
            llmresponse = Call_LLM.main(self.conversation)
            print("LLM Response:", llmresponse)  # Print the response, maybe pretty up later

            if llmresponse:
                # Extract role and content from llmresponse object attributes
                role = llmresponse.role
                content = llmresponse.content

                # Save to conversation array
                # Role is Assistant, unnessisary to seperate character + message for this part
                self.Array_Input(role, "", content)

                # Print the message
                print()
                print(f":{content}")
                print()
                
                # go back to user when LLM's done + printed.
                self.user_input()

            else:
                print()
                print("Empty LLM response.")
                print()
                # If you're getting this error some of the time uncomment:
                # self.user_input()
                # not doing now because if you want this line is case specific. 
                # I think you should just be able to press enter again
                # add another elseif to user_input without the self.Array_Input for if user input is empty if if that doesn't work.

        except Exception as e:
            print()
            print(f"Error while calling LLM: {e}")
            print()
            self.user_input()


# This command runs stuff if and only if this script is being run directly.
if __name__ == "__main__":
    conversation_manager = Conversation()