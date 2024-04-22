# Lord-Game

Lord Game is a proof of concept for the implementation of Large Language Models (LLMs) in story generator games. Story Generator games are a particular genre where a complex world is simulated, the player is given some role in this world, and the fun comes from the player doing whatever they want. Think Minecraft, Rimworld, games produced by Paradox Interactive, etc. The idea is to use LLMs and their emergent creativity and flexibility, to further player agency.

This proof of concept is hugely inspired by the game Sort the Court, a story-based, no-stakes, relaxing game where you are tasked with being the king, and responding yes or no to people asking for your rulings. This project replaces that binary choice with a textbox. (It's gonna be more than a chatbot I swear)

This is not a story game, it is a story generation game. I denounce anyone who wants to replace artists with by-design derivative algorithms, as the pursuit and creation of art is only meaningful for someone who can experience its majesty. This is a game that uses LLMs as an algorithm for its emergent properties of reason and decision-making. It is an early proof of concept and uses Sort the Court as inspiration because of its simplicity.

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
cd ../
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

Just run the main.py script! If that doesn't work replace 'main' with 'Conversation', but it should. game saves are not yet implemented, just put in giberish for now.

Only the first turn is setup for now, so running the main script directly should work.

```bash
 python main.py
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

main.py
Start of script responsible for save selection + running conversation.py. Starts the game and handles save selection. Saving game and all that not yet implemented, but besides that pretty done.

Commands.py:
This script is responsible for some basic actions done across the project. currently, it handles interacting with the terminal, so if and when a proper GUI is implemented Conversaton.py doesn't need to be edited, and basic file operations including a more specific command for reading prompts.json and future prompt jsons for specific turns.

Conversation.py:
Currently the main file for this project, it handles the user interaction section of the turn. Interacted with through the terminal it uses the first turn's set of prompts from Prompts.json, calls the LLM using llm_interface.py, and gets the user input, handling moving on to the next prompt and exiting the program by checking if the user's message is "next" or "exit" and handling that appropriately. It also handles the chat log used by the LLM. If it reaches the last prompt and the command to move on to the next is fired, it sends the chat log array on to Value_Evaluation.py, a temp script to be used later.

llm_interface.py:
A simple script in charge of sending whatever server is hosting the LLM the messages, returning whatever the LLM responds with. Also stores data like the model being used, the temperature, the API Key, etc.

Refreshed_Prompts.py
Temp script, this is for rewriting scripts and will be called at the end of eval when the user is reading through the results of turn. It's got some stuff in it, I don't remember what I was working on to have me make the script and the contents of it, but it's not all that important and should just be looked at as an extension of whatever calls it / as an early thing to deal with when properly developing the prompt writing section of this game.

Value_Evaluation.py:
Temp script made for Conversation.py. Conversation.py calls a function in it with the chatlog array the LLM is given. Right now it just saves a file with that data, but this script is going to be responsible for starting or doing the 2nd part of the turn. 

Find_Commands.py:
Not usable yet. This gets handed copy of raw LLM output, it checks for commands called by LLM in whatever format, issues those commands in the order they were called, and returns a copy of the LLM output without commands in it (this is for Conversation.py so player doesn't need to see LLM's called commands)

Commands/Conversation_Commands.py
Empty python script. Gonna be part of the giving LLM instances access to commands thing, made for the Conversation.py script / the LLM instance directly interacting with the user, has list of potential functions, made because I'm working on Find_Commnads.py.

#### Other Files

Conversation_Start_Prompt.txt:
This is the prompt used for telling the LLM instances created by Conversation.py what it should be doing.

Prompts.json:
A set of prompts used for the first turn. Used by Conversation.py and will eventually be used in part 3 for the format + style the LLM should be writing in.

Saves
Empty folder
Empty folders made in it when you make a new save, and if you make it through turn 1, the LLM's context array from Conversation.py is dropped in there as a json.

Save_Template
Empty folder that's gonna be copied into saves by main.py when I handle save file stuff.

Commands folder
folder full of python scripts containing list of functions different instances of LLM can call. Originally made for Find_Commands.py, as it uses a list of these functions to only call commands that exist.

## Now, soon, and later

### Current State of Game

Right now only the first part is implemented, and it is a very basic implementation at that. The prompts aren't good, the LLM's response is printed directly and it can not call commands, the user has to say next to move on to the next turn and how it currently works is just clunky, no info is given to the LLM besides what is in the prompts for turn 1 in the prompts.json file and the instructions in Converstaion_Start_Prompt.txt.

I rewrote much of the stuff I wrote and it should not be the hardest thing to expand things further. Several placeholder scripts are there so that the written scripts that are already written and are going to interact with those scripts can.

Much of the game is still in development, and sections may be nonsense or not yet implemented. I will try to finish things before publishing them and clean up unfinished garbage I forgot about or just left somewhere.

### Roadmap
DONE
- Add a main script or parent script to Conversation.py, that takes on save file management



I'm not going to be the most organized. I'll move from place to place, but I'll try to work on one area at a time.

1 - Conversation.py
The plan for this project right now is to build up around Conversation.py. Before I move on there's some more stuff I want to work on in this script. 

- Give LLM access to commands + have it working as intended in Conversation.py
- Polish / edits to existing scripts for expandability / modularity
- Additional info for LLM taken from elsewhere
- Probably a good idea to work out how I'm gonna implement core values 
    (values the player has to manage like gold, pops, etc.)
- retcon / reroll command

2 - Saves
From there I am going to focus on save data. This is a pretty narritive focused game where what happens is generated as you go. Saving your stuff is pretty important. This is going to take some time, while rewriting Conversation.py I had saving in mind and know how user interactions through that script are going to happen.

Prompts are going to be saved in Saves/{save}/Prompts, and this is going to include unused prompts, saved as Prompts.json, and used prompts as Prompts{turn number}.json.

I'm also focusing on trying to make this script more accessible and whatnot for people who are not myself. I've spent hours and hours on this readme and I started from scratch this morning. I think people have seen this thing, and although I think the comments I've got in my code are pretty clear, the more fundamental, planning and instructions have not been good for a while. I'm gonna make this shorter too. I know it's way too long.

### Other features I'm not doing right now, but at some point probably.

add 4-5 additional prompts to prompts.json so there's about 10, plus the first one, and maybe the second one, or last one W the demon, so there's 10 pretty standard examples.

A command for until GUI is setup: print turn - print json like that made from Value_Evaluation.py.


Later into development, I want to move over to something with a GUI. Not for some time though

#### looser ideas
I like the idea of giving the LLM a sense of scale for what the values are worth at different intervals.

Probability either called by LLM through some command or automatically fired that LLM uses to decide what happens is a cool idea


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