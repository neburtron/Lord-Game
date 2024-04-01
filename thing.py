import os
import random
import Call_LLM

def get_random_line_from_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines).strip()
        print("Random Line:", random_line)
        return random_line

def makeprompt():
    desired_line = get_random_line_from_file("Prompts.txt")
    print("Desired Line:", desired_line)
    
    return [
        {"role": "system", "content": "this is a test. talk about rocks or something."},
        {"role": "user", "content": "for instance, you could say rocks are cool."},
        {"role": "user", "content": desired_line}
    ]

Prompt = makeprompt()
response = Call_LLM.main(Prompt)
print(response)


