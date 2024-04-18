# Lord Game

This is my first proper coding project. It's a proof of concept for an LLM based decision making game. The idea is to take sort the court's narritive focused cute, relaxing gameplay with little player agency, and throwing out the pre-written narritive, and making player agency the core of the game. Taking the pre-written story type of game and trying to push that close enough to the story generator genre (PDX map games lineup, DF, Rimworld, Minecraft, etc) for a CK4 where you can invent the steam engine or space ship without any mods.

LLMs are cool. They're stupid, anyone who uses them for non-filler writing is lazy or bad at writing, but their ability to write coherently enough and reason enough for idiots and students to use it makes them useful for automation where the procedure can't be broken down to just if else. 

There are four core tasks LLMs are to be used for in this project:
Writing the prompts / decisions the king is tasked with
Interpreting that into value changes and summarizing + taking only bits important to future llm and storing
Answering follow up questions / responding to what player says

The first turn starts with a set of pre-written prompts that get the LLM started off and should be able to be used to help it with writing in the correct format. The player is given the chance to respond, they do, the LLM responds back, and when the player is done interacting they write "next" and the next prompt is added in. There are to be about 10 prompts given to the player per turn, but I don't think I have 10 in the current prompts.json file, and haven't written the write new prompts script yet.

Right now I'm developing this by myself and I don't see that changing until I get a decent ways closer to where I want to be. If you want to help, you can either ask me for something to do, or you can just start doing stuff and I might add it in or whatever. I am really new to coding, I don't know what the conventions are, and I don't care to look into that hypothetical narsicistically.

Now, what do I have so far?
This may be outdated by the time you read this, but:


There's a commands.py file, that contains some file interactions - save, load, load saves file, etc.

llm_interface.py, formerly Call_LLM.py, calls the LLM W the OpenAI API.

Next_Turn.py is a placeholder script for now, here because it's called by another script

Prompts.json is the first turn's prompts formatted in a way TempTerminal.py can read
Conversation_Start_Prompt.txt is the place where the conversation system prompt is stored for TempTerminal.py

Refresh Prompts is another placeholder, it's to be called by Value_Evaluation.py to write the next set of prompts + start the next turn when it's done

TempTerminal is the core script for this thing, at least for now. It's basically the conversation bit all set up. This isn't saying much since chatbots are so overdone for LLMs that it's not even an achievement, but there's other stuff too and I'm working on the actually interesting LLM stuff...


Then there's the saves folder, I am going to look at that later, it's not anything yet, it's the thing that calls next turn.py, yeah.




What development's probably going to look like:

I'm going to improve things at my own pace, and I'm going to focus on what I want to focus on. Expect broken and unfinished code.

First I'm probably work in the area of the TempTerminal.py script, I'll need to get the save data stuff figured out before moving on to val eval + refresh prompts, and all of that really requires thought put into info storage / memory and I don't know how I'm going to tackle that. If I make something, it'll be bad and rewritten after some time if I feel like it. Stuff has, and also will be added in a minimal state, and then removed. Yeah.



