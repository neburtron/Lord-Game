# Lord Game

This is a project that I am currently developing. Currently a lot of the core mechanics are still in development, and a working prototype is my current end goal. 

The idea is Sort the Court, but with a text input rather than just yes or no. The idea is to use an LLM (Large Language Model), like ChatGPT to do the following: 
Deal with follow up questions
interpret the decisions the player makes into a series of effects that change a set of values the player has to balance
manage relevant information and storylines
plan + write out new situations or prompts the user has to deal with.

The game is formatted W a series of turns. Each turn consists of a set of ~10 situations that the player makes a decision on. The LLM writes new prompts in batches. Another thing to make this less of a chatbot and more of a game.

Whereas Sort the Court is designed to be a small, simple, cute, replayable, relaxing game with a loose narritive and the same decisions being handed to you again and again, this is a more player lead game. 

I've played Sort the Court far too much considering the limited scope of the game, picking it up every some amount of months and playing for an hour or two. I highly respect the devs and I want to make it clear that I am not trying to replace artists. This is a game in the same genre, but of a different type to sourt the court. Where that game was narritively focused and had cute, relaxing gameplay and a matching asthetic, my goals are entirely different. I am taking the simple style of gameplay for this prototype of a story generator game that tries to capture enough of the potential LLMs have to convince actual programmers to make story generator games that use LLMs and give me a free copy of it. When I say Story Generator I mean the genre that surrounds DF: Rimworld, minecraft, PDX map games, Civilization, etc. Stuff where you control some person, a country, a town, or a group of people, and get to control their actions and see what happens. 

Stuff I've done so far:
First I've got a call LLM script that takes an input array, sends that to the LLM, and returns the response.
Second I've got a WIP for the first turn of the game (TempTerminal.py). It works to some extent, I haven't written a prompt for the LLM so if you want to run that you'll need to do that. Next moves on to the next prompt, exit exists.
Third I've got a script that saves the chat log from Temp, and is going to evaluate the chat logs given by TempTerminal.
Third I've got a saves folder, and some stuff to do with the values the player has to balance
Also main.py, a GUI thing using Tkinter that I've hardly touched.


If you're interested in helping me with development, or running the very incomplete state the game's in, you can try. I'm trying to make things organized and coherent, and I think I'm making some progress. I'm not a professional coder, so by all means tell me exactly what I'm doing wrong and how, that'd be really helpful. 