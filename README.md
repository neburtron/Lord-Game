# Lord-Game

This project is hugely inspired by the game Sort the Court, a story-based, no-stakes, relaxing game where you are tasked with being the king, and responding yes or no to people asking for your rulings. This project replaces that binary choice with a textbox. The current build goes through the first turn, and I'll be honest, right now, it's basically just a chatbot. This is a chatbot I've spent a lot of time working on and writing in such a way that it can be expanded, and I have no intention to stop any point soon. Unless I die in a freak accident, it's not going to stay another lame chatbot.

Lord Game is a proof of concept for the implementation of Large Language Models (LLMs) in story generator games. Story Generator games are a particular genre of games that focus on making a complex simulation, and letting the player interact with this world. Some Table Top Role Playing Games (TTRPGs) aim for the same ideals of player agency in a structured world. DND, Pathfinder, Fate, and a billion other game systems have the sort of freedom this prototype aims to inspire the creation of. 

To be clear though, this is not a digitize DND attempt. There is a saturated market of games with this goal, and Virtual Tabletops have already achieved this. I would argue that the difference between the mediums of Tabletop Games and Video Games has led to two different approaches to achieving the same goal and this prototype fits cleanly into the video game medium's philosophy. In a dnd game, the DM is also a player, and their job is to be the world, with the help of rule books. In a game of CK3, there isn't a DM. The rules work without an interpreter.


## Instalation Instructions

### Necessary to run project:

Access to LLM VIA OpenAI API. You CAN'T just use ChatGPT, you need to go through the API.

This project uses the OpenAI API, but this doesn't mean you need to use their services. Working on this project, I've use LLama 2 7B Q8 through LM Studio run locally on my M1 Macbook Pro. this is not an endorsement of them, I didn't put in the most due diligence when selecting the LLM to run, it's competitors likely have similar features. 


### Actual Setup

1. Clone the repository:

```bash
 git clone https://github.com/neburtron/Lord-Game.git
```

Get the game files on your computer. You can also download the game as a zip file.

2. Navigate to the project directory (through terminal)

```bash
 cd Lord-Game
```

Open the terminal, and navigate to wherever you put the game files. the CD command moves you into the folder you write after, if there is one with the name you listed. 

To leave the folder you're in if you go the wrong way or want to have the game files somewhere else, you can type:
```bash
cd ../
```

If you use the git clone command (in step 1), you should just be able to type CD Lord-Game because git pull puts stuff in the directory you're in, so all you need to do is go into the project file you just downloaded.

3. Install requirements

```bash
 pip install -r requirements.txt
```

4. Run Project

Just run the main.py script!

Only the first turn is setup for now, so running the main script directly should work.

Main.py should automatically ask you the settings to use to connect to the llm. After this it will put it into a json called llm_settings, so if you want to go through that again just remove that file, if you want to change those values edit llm_settings.json in a text editor, and if you want to change what settings are used, change that file and llm_interface.py.

```bash
 python main.py
```

This project is early in development, and this is a rather simple prototype. I am focusing on getting a complete build finished, so polishing the working gameplay is not a priority. If you want to run the demo, I suggest editing the prompts. There are two sets of prompts used in the current working build, Prompts.json and Conversation_Start_Prompt.txt, both in this project's root directory. 

Prompts.json has several sections in it. Text1, Text2, and EnterDesc, are both printed and given to the LLM, with the name of the characters attached to text1 and text2. Notes is only given to the LLM.

If you change stuff / make stuff with this project, I'd be interested to see what you came up with, and by all means post it.


## How this project works and future plans

Refer to Plans_and_Files.md


## Contributing

Refer to CONTRIBUTING.md

## License

Refer to the license document
(I use the Unlicense, which basically just says this is public domain)

## Developers

MuteMaroonWorm - Only dev for now + creator

Right now I'm the only one to work on this thing. Hello, I'm MuteMar, I'm the person writing all of this for now. I think you're able to contact me through GitHub. My old handle's Neburtron, that's also me. Here's my email too. I've also got a Deviantart if you like looking at graphite on paper, it's linked to my GitHub.

https://github.com/neburtron
mutemaroonworm@gmail.com



## Inspiration

Sort the Court
The core gameplay of this project is hugely inspired by Sort the Court, a small indie game that I've played far far too much considering the limited narrative content for a game driven more by a pre-written story than gripping gameplay. Play the game. search for sort the court in Google or click the link below. Think that's the original posting, but I'm not sure.
https://graebor.itch.io/sort-the-court