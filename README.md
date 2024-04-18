# Lord Game

Lord Game is a text-based decision-making game prototype that uses Large Language Models (LLMs) rather than a pre-written script to let the player make decisions. Largely inspired by Sort the Court, 


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

Conversation.py: 


There's a commands.py file, that contains some file interactions - save, load, load saves file, etc.

llm_interface.py, formerly Call_LLM.py, calls the LLM W the OpenAI API.

Next_Turn.py is a placeholder script for now, here because it's called by another script

Prompts.json is the first turn's prompts formatted in a way Conversation.py can read
Conversation_Start_Prompt.txt is the place where the conversation system prompt is stored for Conversation.py

Refresh Prompts is another placeholder, it's to be called by Value_Evaluation.py to write the next set of prompts + start the next turn when it's done

Conversation.py is the core script for this thing, at least for now. It's basically the conversation bit all set up. This isn't saying much since chatbots are so overdone for LLMs that it's not even an achievement, but there's other stuff too and I'm working on the actually interesting LLM stuff...

New script, now instead of being called TempTerminal and interacting with the terminal itself, conversation.py now tells Terminal.py what to do. Should make moving to GUI easier, hopefully. 

Then there's the saves folder, I am going to look at that later, it's not anything yet, it's the thing that calls next turn.py, yeah.




What development's probably going to look like:

I'm going to improve things at my own pace, and I'm going to focus on what I want to focus on. Expect broken and unfinished code.

First I'm probably work in the area of the Conversation.py script, I'll need to get the save data stuff figured out before moving on to val eval + refresh prompts, and all of that really requires thought put into info storage / memory and I don't know how I'm going to tackle that. If I make something, it'll be bad and rewritten after some time if I feel like it. Stuff has, and also will be added in a minimal state, and then removed. Yeah.

## Installation

This project uses the OpenAI API, so you need to get some LLM that goes through the OpenAI API to get this to work. You can host an LLM locally through LM Studio or probably it's competitors, or you can get an OpenAI API thing. 

To install the required dependencies for this project, ensure you have Python installed on your system. Then, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/yourproject.git

2. Navigate to the project directory:
    
    cd yourproject

3. Install the dependencies using pip:

    pip install -r requirements.txt

4. Put your OpenAI API details into llm_interface.py 

    You can also change whatever config

5. Run game

    python Conversation.py

If this is bad, sorry, it was worse before + I got ChatGPT to fill in the install commands + whatever. I don't know if it'll work on Linux or Windows, I don't know why it wouldn't, but I don't know a lot about coding for different OS's. 




## How to help

This is an open source project. I am new to coding and still setting things up as I go. Find something that I stay I plan on doing and do it, or figure out how this thing works and improve it, or write / fix prompts, etc.

If you can't help because I didn't set something up / set something up wrong, just contact me.


## How to Contribute

Contributions to this project are welcome! Here's how you can help:

- Improve existing prompts or add new prompts to `prompts.json` and share them publically.
- Optimize game logic in `Conversation.py` or other scripts for better user interaction.
- Test the game on different platforms and report any issues.
- Provide feedback on the project's design and usability.
- Implement planned features noted in comments.

Fork the repository, make your changes, and submit a pull request!

You can contact me through github (I think) or mutemaroonworm@gmail.com
