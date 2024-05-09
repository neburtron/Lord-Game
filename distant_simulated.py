import commands


# Just started putting things into place, this is nothing, I'm gonna go back to it later.

class Simulate:

    def __init__(self, save, turn):
        self.turn = turn
        self.save = save

        if turn == 0:
            self.prompts = self.get_prompts(True)
        else:
            self.prompts = self.get_prompts(False)

        self.prompts = self.get_prompts()
    

    def get_prompts(self,thing):
        
        def open_file():
            return 5

        if thing == True:
            # get data from turn 1. Either keep in root for now or have a starting data folder
            prompts = open_file("filename.json or folder/filename.json")
            return prompts
        else:
            # Get from wherever it's stored for the turn
            thing = 5 # Replace with thing to get file location (saves/save/filename.json or whatever)
            prompts = open_file(thing)
            return prompts



if __name__ == "__main__":
    Sim_Instance = Simulate(5, 5)




"""
Set of ongoing storylines independed, and potentially hidden from user.

Make a file like prompts.py + get starting list there if new game
When doing this, it's probably a good idea for future developments, to put story setup stuff in it's own folder

At end of each turn, after Eval, what the player did / what they dealt with, if it impacts the thing being simulated, 
stuff changes.
Then one step forwards is taken. Either the LLM writes a series of outcomes / changes W probabilities attached + a dice is 
rolled, or the LLM asks for / is given a probability and bases what happens on the result, rather than calling beforehand

Should also be a long term plan written / trajectory or tragectories that determine where things go in the future.
EX
This character wants power, they're gonna look for power, they want this sort of power, they're seeking out X in the long term
currently.
I prefer trajectory over long term plan here to be honest. In the example above specifics dependent on what results of example
character's actions are left up in the air, but the motivations are left intact, and it's rather easy to write in what they go
for next. Better than plan is probably motivation, but tracjectory is more general and I want it to be that way.

There should also be some script or something that makes more of + removes resolved / unimportant hidden storylines. Maybe
just spontanious creation, more likely branching off of things the player's seen / splitting storylines.


Actual Implementation:
Somewhat in the air, but the current, limited one turn demo / build was feeling really light + chatbotty.
This isn't supposed to be a stupid chatbot, it's supposed to be a proof of concept.

Open json file + save to array
    Each item includes a brief history + has a list of defined things it interacts with in the lore
    Should be in the form of {}'s

Go through each, get the {}'s and add the summary of each to the end, titled.

If it's longer than arbitrary limit, ask LLM if it can shorten it / remove outdated stuff without loosing important info, get 
it to do so if it can, move on if it can't.

Get summarized story impacts from Eval part, and go through each simulated thing, and get LLM to decide how that impacts things

Error handling, let it skip them, let it ask for more details, maybe tell it the ways to call each referenced thing to see if
it's related to this that or the other, etc.

Then tell LLM (new or same instance) to take the last short term trajectory planned, and do the bit where it decides what 
happens.

Then ask it to say what trajectory things will move on going forwards.

Change values

Take the new stuff, and ask LLM to combine it with the old stuff

Save all the stuff, try to do it in an organized manner.

I know this is a really big addition to make to the plans, but I want to make a good game and I was able to get this far...

"""

