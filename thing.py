# I'm going to leave this here, even though I've moved on past it, it's simple, midnight, and I'll deal with this later.
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
        {"role": "system", "content": "Your job is to take the short descriptions below, and expand them, written from the POV of a character involved talking to the king. You are doing this for a game where the player acts as the king and has to make decisions. Don’t write the King’s reactions for them. Either tell the player what happened giving them a chance to decide what to do now that the thing happened, tell them what’s happening and give them a chance to decide what to do, or try to propose something to the player. Don't make things bigger than they are, if there's a small problem, it is small for a reason. Only generate one prompt. The player is the king, refer to them as such, don't tell them what they do or what they've heard or anything like that. Your job is to be the world around them."},
        {"role": "system", "content": desired_line}
    ]

Prompt = makeprompt()
print(Prompt)
response = Call_LLM.main(Prompt)
print(response)