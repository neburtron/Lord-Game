# Lord Game

Lord Game is a text-based decision-making game prototype that uses Large Language Models (LLMs) rather than a pre-written script to let the player make decisions. Largely inspired by Sort the Court, 

This is MuteMar talking, I'm the only one to contribute so far, it's my project, I'm the one who's spent hours and hours working on it. 

This is my first proper coding project. It's a proof of concept for an LLM based decision making game. The idea is to take sort the court's narritive focused cute, relaxing gameplay with little player agency, and throwing out the pre-written narritive, and making player agency the core of the game. Taking the pre-written story type of game and trying to push that close enough to the story generator genre (PDX map games lineup, DF, Rimworld, Minecraft, etc) for a CK4 where you can invent the steam engine or space ship without any mods.

LLMs are cool. They're stupid, anyone who uses them for non-filler / formulaic writing is lazy or bad at writing, but their ability to write coherently enough and reason enough for idiots and students to use it makes them useful for automation where the procedure can't be broken down to just if else. 

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



## Development
What development's probably going to look like:

I will try to be organized and make my plans open, but being consise and clear is hard and I am not writing a novel. I'm going to go at my own pace, but I'll try and get things setup because the whole idea of this thing is to get a working proof of concept done.

Right now the main thing I've got implemented is Conversation.py and the scripts that it interacts with. The best way forwards in my mind isn't to have a bunch of different seperate parts, but build from the working chatbot type thing. I'll write bad code, fix it, then go a step further. 

Sorry, I'm going to rewrite this section later

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

Note - there are two commands you can run through the user input thing. Next and Exit. Self explanitory. Next moves on to next person / decision to make, exit closes the thing. I don't say this explicitly in the pre-written prompts yet, and the llama model I'm running doesn't tell the user to say next like I told it to.


Might or might not work on Windows or Linux. 

Does work on my M1 macbook pro. 


## How to Contribute

Contributions to this project are welcome! Here's how you can help:

- Play around with the prompts (prompts.json and conversation_start_prompt.txt) and share what you find.
- Fix things in the script / bugfix / improve the code / add comments / whatever else
- Test the game on different platforms and report issues.
- Write things for the project you think fit / work towards vision
- Implement something not yet implemented you see commented in or mentioned somewhere.

Fork the repository, make your changes, and submit a pull request!

You can contact me through github (I think) or mutemaroonworm@gmail.com

If anything here is wrong / not working just tell me, I'm new to github + coding + sections of this read me use ChatGPT.