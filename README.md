# Lord Game Rewrite

not done yet

This is a project I've been thinking about for a while.

Sort the court but with LLMs. This isn't a replace writers type thing, Fuck anyone who thinks getting rid of writers is a good idea. This is a different type of game. Where Sort the Court is about the story, this game is more about specific decisionmaking and player lead stuff. Games are an interactive medium and this is my attempt at a less telltale, more rimworld / DF type game. 

Sort the Court Devs, I just want to say, big fan of your stuff, you made a great game and this doesn't come across as an insult, your work is great, even though I exhausted the story I've revisited the game so many times, multiple times this year, it really is great, AI doesn't exist and ChatGPT is a glorified word guesser, I just want to boss computer people around, don't be mad at me plz.


Stuff I've done so far:
- Made a script that calls LLM through openAI API
- Created a set of prompts to start the game off and give an example to the the LLM what it should aim for stylistically
- a script that can get a random line from a txt doc, and put that into a call prompt. Prototype to be pulled apart and applied.
- The most basic of placeholder GUIs with just a start button and second frame with a bit of text on it
- A json with some prompts on it that I think are ok.

The call script is the biggest thing I've done so far, there's a section on the top of the script where you can put your details in, if you don't want to use OpenAI's models and servers you can host an LLM locally, I know LM Studio lets you host a local server that works for the OpenAI API, not an endorsement of them, that's just what I use and no thought or foresight was put into that decision. Just downloaded one of them. Other local LLM software probably has the same features. 

If you want to do something with it just make a script that imports Call_LLM.py, call the main command like in thing.py, and write the prompt as a Json in the format it likes. Not that anyone's reading this or anything.