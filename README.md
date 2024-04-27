# Lord-Game

Lord Game is a proof of concept for the implementation of Large Language Models (LLMs) in story generator games. Story Generator games are a particular genre where a complex world is simulated, the player is given some role in this world, and the fun comes from the player doing whatever they want. Think Minecraft, Rimworld, games produced by Paradox Interactive, etc. The idea is to use LLMs and their emergent creativity and flexibility, to further player agency.

This proof of concept is hugely inspired by the game Sort the Court, a story-based, no-stakes, relaxing game where you are tasked with being the king, and responding yes or no to people asking for your rulings. This project replaces that binary choice with a textbox. (It's gonna be more than a chatbot I swear)

This is not a story game, it is a story generation game. I denounce anyone who wants to replace artists with by-design derivative algorithms, as the pursuit and creation of art is only meaningful for someone who can experience its majesty. This is a game that uses LLMs as an algorithm for its emergent properties of reason and decision-making. It is an early proof of concept and uses Sort the Court as inspiration because of its simplicity.

## Instalation Instructions

Necessary to run core project functionalities:
- Access to LLM VIA OpenAI API. You CAN'T just use ChatGPT, you need to go through the API.
If you don't want to pay them, you can imitate an OpenAI server W LM Studio on a local device, with a local LLM model. 
(other LLM software probably has similar features)


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

4. Put your details into llm_interface.py 

Just open up llm_interface.py in a text editor or code editor, and change the values. I left out some because I didn't find the need to, it should be rather simple to add them in.

Things you'll probably need to change/look at:
- API Key
- Model
- Base_URL

5. Run Project

Just run the main.py script! If that doesn't work replace 'main' with 'Conversation', but it should. 

Only the first turn is setup for now, so running the main script directly should work.

```bash
 python main.py
```

This project is early in development, and this is a rather simple prototype. If you're interested in this project, I suggest tweaking / playing around with the prompts. If you make something you like or improve what I wrote, feel free to share them for others to use. At some point, I plan to focus on improving the prompts, but I'm not there yet in development.

Additionally, anyone who wants to look at the code stuff is also encouraged to. it's public domain, if you're interested in helping out with this project I'm open to that, this is a thing I want to see materialize, any help in that effort is really appreciated. Refer to the CONTRIBUTING.md file if you're interested.

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