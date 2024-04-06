# I used ChatGPT for this, but I rewrote it from pretty much scratch.
# Still using it's help + suggestions, but being intentional over things are done + organized.
# Should work like the old one, but better. I worked on this script for basically all of today, for added functionality, so hopefully it works good.
# Sorry about LLM response, I want this to work before I commit this and I'm relying on ChatGPT because I don't know enough about arrays and whatnot.
# I removed what turned into LLM_start_prompt I'm gonna write a new one, in the meantime just write your own and change it everytime it doesn't do what you want.
# I suggest starting W telling it to write just a few sentences tops, and what it's job is.

import json
import Call_LLM
import Value_Evaluation
# Still working on Value Evaluation


class Conversation:

    def __init__(self, prompts_file='prompts.json'):
        try:
            with open(prompts_file) as f:
                self.prompts = json.load(f).get("prompts", [])
        except FileNotFoundError:
            print("Error: prompts.json file not found.")
            self.prompts = []

        self.conversation = []
        self.current_prompt_index = 0
        LLM_start_prompt = "This is a test. Just write 'test' regardless of what I say, just the one word so I can test the systems around you without waiting for you to generate lots of text. Don't worry if you say something else, that isn't you, I'm injecting pre-written prompts and putting them under the assistant role because there it's the one that fits best."
        self.Array_Input("system","",LLM_start_prompt)

        if self.prompts:
            first_prompt = self.get_next_prompt()
            if first_prompt:
                self.relayprompt(first_prompt)
            else:
                print("No prompts available.")
        else:
            print("No prompts found in prompts.json.")


    def get_next_prompt(self):
        #check if there's more prompts before moving on
        if self.current_prompt_index < len(self.prompts):
            next_prompt = self.prompts[self.current_prompt_index]
            self.current_prompt_index += 1  # Move to the next prompt for the next call
            return next_prompt
        else:
            Value_Evaluation.main(self.conversation)


    def relayprompt(self, prompt):
        # for printing prompt in terminal + giving to LLM

        print(self.current_prompt_index)

        if "EnterDesc" in prompt:
            self.Array_Input("assistant", "Scene", prompt["EnterDesc"])
            print(f"Scene: {prompt['EnterDesc']}")

        if "character" in prompt and "text1" in prompt:
            self.Array_Input("assistant", prompt["character"], prompt["text1"])
            print(f"{prompt['character']}: {prompt['text1']}")

        if "character" in prompt and "text2" in prompt:
            self.Array_Input("assistant", prompt["character"], prompt["text2"])
            print(f"{prompt['character']}: {prompt['text2']}")
        
        self.user_input()

    def Array_Input(self,thing,person,msg):
        if thing:
            self.conversation.append({"role": thing, "content": person + ": " + msg})
        else:
            self.conversation.append({"role": thing, "content": msg})
        #Just the format for putting stuff in Array


    def user_input(self):
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            Value_Evaluation.main(self.conversation)
            return
        elif user_input == "next":
            self.Array_Input("user", "player", "next")
            prompt = self.get_next_prompt()
            if prompt:
                self.relayprompt(prompt)
            else:
                print("Out of Prompts")
        else:
            # Send message to Array and send Array to LLM
            self.Array_Input("user", "player", user_input)
            self.llmresponse()
    def llmresponse(self):
        try:
            # Call LLM and retrieve response
            llmresponse = Call_LLM.main(self.conversation)
            print("LLM Response:", llmresponse)  # Print the response for debugging

            if llmresponse:
                # Extract role and content from llmresponse object attributes
                role = llmresponse.role
                content = llmresponse.content

                # Save to conversation array
                self.Array_Input(role, "", content)

                # Print the message content
                print()
                print(f"{role}: {content}")
                print()
                
                # go back to user when LLM done + it's stuff is printed.
                self.user_input()

            else:
                print("Empty LLM response.")

        except Exception as e:
            print(f"Error while calling LLM: {e}")
    

if __name__ == "__main__":
    conversation_manager = Conversation()