# Lord-Game

NOTE - If anything is broken go back to the version from around the 7th. It should work, but I changed some stuff and haven't tested everything out to verify that I have in fact fixed everything. I made a new branch to preserve a working version of the game and just merged it since it's been a while since and it seems like it works fine overall. 



This project is hugely inspired by the game Sort the Court, a story-based, no-stakes, relaxing game where you are tasked with being the king, and responding yes or no to people asking for your rulings. This project replaces that binary choice with a textbox. The current build goes through the first turn, and I'll be honest, right now, it's basically just a chatbot. This is a chatbot I've spent a lot of time working on and writing in such a way that it can be expanded, and I have no intention to stop any point soon. Unless I die in a freak accident, it's not going to stay another lame chatbot. 

One of the four core parts of the core gameplay loop are implemented in some working state, conversation.py and the stuff that it needs to work. That's the bit where the user interacts with the game. It needs work, and I'm currently working on making it better and less of a chatbot through changing the format it writes in, giving it access to a set of commands, giving it a bunch more info + editing the prompts, etc. That's alongside some other QOL + other changes.

The other three are really important for this proof of concept: the memory system, a system for simulating stuff happening independently to the player through a rigid structure of the goal / trajectory of some agent and a process for deciding what happens and how things change at the end of every turn, and a system for writing the next set of prompts. This is an ambitious project, it isn't anything special now. If you find it interesting I'd suggest starring or watching this project and coming back in like a year. Alternatively, I'm 100% open to hearing ideas or talking about this project.

you can read about them more in [Plans_and_Files.md](Plans_and_files.md).


Lord Game is a proof of concept for the implementation of Large Language Models (LLMs) in story generator games. Story Generator games are a particular genre of games that focus on making a complex simulation, and letting the player interact with this world. Think DND but as a video game. Story Generator video games and Table Top Role Playing Games (TTRPGs) like DND are two different genres of the same medium / artform, but TTRPGs have a similar balance of true flexibility and structure this project is aiming for. In other words, this is like a proper dnd video game, but it's not a dnd port, the way you go about achieving the same thing is different depending on the medium you're working I've spent a lot less time playing DND than CK2, CK3, Vicky 3, Civ 6, and rimworld each. 

Representation:

This is a proof of concept in the public domain designed to be customizable. I'm making a generic kingdom management game with a steryotypical europian king in it. I wrote this as a placeholder and it really really needs to be replaced and I'm gonna change the format to make it easier to write new prompts and to give the LLM a lot more info for the first proper version of this project. This is a story generator games, feel free to change how the story starts. I don't know if anyone's actually played this thing and liked the limited current state of the game enough to consider revistiting + writing new prompts, but thought I'd put this here anyways. for the current build, some text might be stored in the actual python scripts.

 the prompts are stored in prompts.json, and the LLM's instructions are stored in conversation_start_prompt.txt

## Instalation Instructions

### Necessary to run project:

Access to LLM VIA OpenAI API. You can't just use ChatGPT, you need to go through the API.

This project uses the OpenAI API, but this doesn't mean you need to use their services. Working on this project, I've use LLama 2 7B Q8 through LM Studio run locally on my M1 Macbook Pro. this is not an endorsement of them, I didn't put in the most due diligence when selecting the LLM to run, it's competitors likely have similar features. 

I don't know a lot about LLM APIs. I'm going to look more into them with setting up different response formats. With this I plan on setting it up so you can use another API / setup infastructure to allow that. I think huggingface is one of the major alternatives, I don't know, I'm gonna look into this more later. LM Studio's worked for me.


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

```bash
 python main.py
```

main.py should ask you to select your LLM's settings. If you type 'Y', a tkinter window should open and let you select your settings. Right now only OpenAI's API works, multiple tabs are there for when I setup Huggingface or whatever other API stuff. Later which tab you close on will be the model you've got selected. 

The current build only works for the first turn and I've not implemented most of what I have planned. I had an ok time testing it out, and if you like the demo and are looking for more, it's gonna be a while and playing around with the prompts is probably your best bet... or DND. 

prompts.json and conversation_start_prompt.txt are the main ones. Prompts.json has 2 bits of text sent to both the player and LLM and notes sent only to the LLM. Format's gonna change a ton pretty soon, so be aware of that. 

## How this project works and future plans

Refer to [Plans_and_Files.md](Plans_and_files.md)

## Contributing

Refer to [CONTRIBUTING.md](CONTRIBUTING.md)


## License

Refer to: [License](LICENSE)

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