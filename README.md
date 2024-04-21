# Lord-Game

Lord Game is a proof of concept for the implementation of Large Language Models (LLMs) in story generator games. Story Generator games are a particular genre where a complex world is simulated, the player is given some role in this world, and their job is to interact with it. Think Minecraft, Rimworld, games produced by Paradox Interactive, etc. The idea is to use LLMs and their emergent creativity and flexibility, to further player agency.

This proof of concept is hugely inspired by the game Sort the Court, a story-based, no-stakes, relaxing game where you are tasked with being the king, and responding yes or no to people asking for your rulings. This project replaces that binary choice with a textbox. (It's gonna be more than a chatbot I swear)

This is not a story game, it is a story generation game. I denounce anyone who wants to replace artists with by-design derivative algorithms, as the pursuit and creation of art is only meaningful for someone who can experience its majesty. This is a game that uses LLMs as an algorithm for its emergent properties of reason and decision-making. It is an early proof of concept and uses Sort the Court as inspiration because of its simplicity.

I have not seen all that much LLM integration in gaming, and for games where player agency and the world reacting to it are the essence of their gameplay, it seems like an innovation waiting to happen. Although in this early stage of development, this is a step away from yet another glorified chatbot, the goal is to push for more complexity and structure for something that is still a game, while letting the player do almost anything within reason, their character's abilities, and setting.


## Instalation Instructions

Necessary to run core project functionalities:
- Access to LLM VIA OpenAI API. You CAN'T use ChatGPT, you need the API.
If you don't want to pay them, you can imitate an OpenAI server W LM Studio for a local LLM model. 
(other LLM software probably has similar features)


1. Clone the repository:

```bash
 git clone https://github.com/neburtron/Lord-Game.git
```

Get the game files on your computer. I think you can also download the game as a zip file.


2. Navigate to the project directory (through terminal)

```bash
 cd Lord-Game
```

Open the terminal, and navigate to wherever you put the game files. the CD command moves you into the folder you write after, if there is one with the name you listed. 

To leave the folder you're in if you go the wrong way or want to have the game files somewhere else, you can type:
```bash
CD ../
```

If you use the git clone command (in step 1), you should just be able to type CD Lord-Game because you're making it in the root directory, and all you need to do to set things up is go into the folder you got onto your computer.

3. Install requirements

```bash
 pip install -r requirements.txt
```
Requirements.txt was created automatically, I think the only thing I've installed for this was the OpenAI API, maybe one or two others, but there's a pretty big list. I'm pretty sure it's mainly just nested dependencies, but I could be wrong, I am new to coding.

4. Put your details into llm_interface.py 

Just open up llm_interface.py in a text editor or code editor, and change the values. I left out some because I didn't find the need to, it should be rather simple to add them in.

Things you'll probably need to change/look at:
- API Key
- Model
- Base_URL

5. Run Project

Conversation.py is the core script of what I've implemented.

```bash
 python Conversation.py
```

This project is early in development, and this is a rather simple prototype. If you're interested in this project, I suggest playing around with the prompts. If you make something you like/improve the ones I wrote, feel free to share them for others to use. At some point, I plan to focus on improving the prompts, but I'm not there yet.

Additionally, anyone who wants to look at the code stuff is also encouraged to. it's public domain, if you're interested in helping out with this project I'm open to that, this is a thing I want to see materialize, any help in that effort is really appreciated. Refer to the CONTRIBUTING.md file if you're interested.


## Game Design

A lot of this hasn't been implemented yet...

The game is divided into turns. Each turn consists of 10 or so prompts, or pre-written situations your character is to make.

Each turn starts with 10 prompts pre-written. The first turn's prompts are already written out, but after that they are to be written by the LLM, using the starting prompts as a formatting guide, based on what's happened previously.

Each turn has 3 parts to it.

The first part is where the user directly interacts with the game. The user is given a prompt, and they make their decision or talk with the person asking for a decision from them, then when the player or LLM deems the interaction over, the next pre-written situation is given to the user.

The second part is interpretation. Value_Evaluation is given the chat logs and gets 2 pieces of info from that: Changes to a set of values the player has to manage, and info important for the story or world being portrayed. Two LLM instances with different prompts/orders will be called, and their task is to write a series of commands using a format that can be interpreted and executed by a Python script. Specifics are not in stone, I haven't worked on this yet, and don't know how I'm going to exactly manage the memory stuff. 

For the values, there are to be 3 commands: Immediate effects, delayed effects, and regular effects. Regular as in every turn. Each value command will be able to affect all values and has a name that indicates where it's from.


Then the player is given a screen showing changes to their core values, with text saying why they changed the way they have. Also potentially have some text describing more ground level, story/world changes.

The third and final part is the writing of the prompts for the next turn. This is the part furthest from development, maybe besides a working GUI, so it's the least fleshed out. Based on hand-written prompts from Prompts.json and info about the current state of the world and open storylines / sown seeds / however story info is stored, it is tasked with writing 10 new prompts.

#### Scripts

Commands.py
This script is responsible for some basic actions done across the project. currently, it handles interacting with the terminal, so if and when a proper GUI is implemented Conversaton.py doesn't need to be edited, and basic file operations including a more specific command for reading prompts.json and future prompt jsons for specific turns.

Conversation.py
Currently the main file for this project, it handles the user interaction section of the turn. Interacted with through the terminal it uses the first turn's set of prompts from Prompts.json, calls the LLM using llm_interface.py, and gets the user input, handling moving on to the next prompt and exiting the program by checking if the user's message is "next" or "exit" and handling that appropriately. It also handles the chat log used by the LLM. If it reaches the last prompt and the command to move on to the next is fired, it sends the chat log array on to Value_Evaluation.py, a temp script to be used later.

llm_interface.py
A simple script in charge of sending whatever server is hosting the LLM the messages, returning whatever the LLM responds with. Also stores data like the model being used, the temperature, the API Key, etc.

Next_Turn.py
Temp script that doesn't do anything, old, and might just remove.

Refreshed_Prompts.py
Temp script, this is for rewriting scripts and will be called at the end of eval when the user is reading through the results of turn. It's got some stuff in it, I don't remember what I was working on to have me make the script and the contents of it, but it's not all that important and should just be looked at as an extension of whatever calls it / as an early thing to deal with when properly developing the prompt writing section of this game.

Value_Evaluation.py
Temp script made for Conversation.py. Conversation.py calls a function in it with the chatlog array the LLM is given. Right now it just saves a file with that data, but this script is going to be responsible for starting or doing the 2nd part of the turn. 

#### Other Files

Saves
I'm going to deal with / remove this later. Old work for game saves. 

Conversation_Start_Prompt.txt
This is the prompt used for telling the LLM instances created by Conversation.py what it should be doing.

Prompts.json
A set of prompts used for the first turn. Used by Conversation.py and will eventually be used in part 3 for the format + style the LLM should be writing in.


## Now, soon, and later

### Current State of Game

Right now only the first part is implemented, and it is a very basic implementation at that. The prompts aren't good, the LLM's response is printed directly and it can not call commands, the user has to say next to move on to the next turn and how it currently works is just clunky, no info is given to the LLM besides what is in the prompts for turn 1 in the prompts.json file and the instructions in Converstaion_Start_Prompt.txt.

I rewrote much of the stuff I wrote and it should not be the hardest thing to expand things further. Several placeholder scripts are there so that the written scripts that are already written and are going to interact with those scripts can.

I tried to set up game saves, but what I have is very incomplete and I might start fresh when I return to that.

Much of the game is still in development, and sections may be nonsense or not yet implemented. I will try to finish things before publishing them and clean up unfinished garbage I forgot about or just left somewhere.

### Roadmap
Development will center around the Conversation.py script for some time. There are things I still want to implement + improve upon there, and I think I've commented in a lot of those plans.

Chances are, the next thing I will focus on is the save system. I've played around with the idea of one a bit, and in the current draft of the Conversation.py script, I've got a way to handle selecting saves setup. I want to do this before focusing on eval + writing new prompts because I want a lot of the data to be saved in case the user wants to look back at it + everything isn't just lost to the aether.

I'm also focusing on trying to make this script more accessible and whatnot for people who are not myself. I've spent hours and hours on this readme and I started from scratch this morning. I think people have seen this thing, and although I think the comments I've got in my code are pretty clear, the more fundamental, planning and instructions have not been good for a while. I'm gonna make this shorter too. I know it's way too long.

### Unplanned features / potential future

At some point I want there to be a GUI for this thing. I'm focusing on the gameplay right now, and that'll take a while to finish.

The future of this type of game is more simulated world. The goal is CK3 but you can do literally anything, if you want to make a game in this genre go ahead, if you want to contact me (MuteMar) about this sort of stuff go ahead, I'd love to talk about this sort of stuff / help you as much as I can with your own project. Even though I don't know what I'm doing, I'm tens and tens of hours into this thing as of April 20th, 2024, I know some stuff if we're talking about the type of game I've been working on.

I also like the idea of giving the LLM a sense of scale for what the values are worth at different intervals.

Also having the LLM roll dice to determine outcomes / having that done automatically is a cool idea. 

## Contributing

Refer to CONTRIBUTING.md

## License

Refer to the license document
(I use the Unlicense, which basically just says this is public domain)

## Developers

MuteMaroonWorm - Only dev for now + creator
    Right now I'm the only one to work on this thing, hello, I'm MuteMar, most things in the first person I'm saying. I think you're able to contact me through GitHub, my old handle's neburtron. Here's my email too. I've also got a Deviantart if you like looking at graphite on paper, it's linked to my GitHub.
    https://github.com/neburtron
    mutemaroonworm@gmail.com


## Inspiration

Sort the Court
    The core gameplay of this project is hugely inspired by Sort the Court, a small indie game that I've played far far too much considering the limited narrative content for a game driven more by a pre-written story than gripping gameplay. Play the game. search for sort the court in Google or click the link below.
    https://graebor.itch.io/sort-the-court