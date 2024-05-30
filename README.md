# Lord-Game

ABANDONED
I am starting fresh, the right way. New version called "The Head that Wears the Crown". The github project is just called Wears the Crown because short. This code is a mess, I do not suggest looking thorugh it, if you've got any interest in this project just wait or contact me to be close to development.







NOTE - This is a very broken, incomplete, rough project. I hope it works, it might not. The idea is good though. I'm gonna work on this and get it to the point where it works in it's most minimal state and I'm happy with it, then I'll release it. That might be after a full rewrite, though.


## Game Idea

This game's trying to be a story generator game. Story generator as in the type of game DF, Rimworld, Minecraft, Viky3, CK3, etc are. A world is simulated and the player acts. This is a pet project, because for ages I've wanted to see a game where you can do literally whatever you want if you put in the effort. Video game specifically, I know about DND, but that's it's own thing, mediums impact the art and the existance of what I'm looking for in a movie doesn't make my wanting a tv show that delivers the same idea invalid. They're different, I like PDX Interactive games, I want to kill the space pope with a rocketlauncher without needing to sit through another stupid waste of time intervention.  



LLMs have demonstrated some emergent reasoning capabilities, and this project aims to structure that. The core gameplay is simple, modeled off of the game Sort the Court. People come in with problems, you deal with them. Some specifics are in the air currently, but every turn 10 new prompts are written based on information stored about the simulated world. The user talks with a second LLM instance that plays the role of the petitoner and anyone else in the room. A third decides the probable outcomes of the player's choice, one outcome is chosen, and a fourth instance turns that subjective effect into changes to the data stored about the world and whatever else. This is a proof of concept to enable better devs to do this better. I want to go to the moon in CK4, how have we got to CK3 without space travel?!?

Then to make the world more alive, later in this project I plan on simulating things happening independent from the player. Independent storylines. The idea is to start off with 5 - 10 characters with a lot of info on their motivations, ways of buisness, what they want, etc, and have them move one step towards that every turn, the rest run the same way as the player's choices. Then there's some logic that determines when a new independent agent is needed, either if storylines are resolved and there's less than enough, or if a character goes off to do a thing and it wouldn't make sense to just have them return in X turns, or if other criteria is met. Then a character that meets criteria will be taken from the game, or an external folder, and given agency. This should make gameplay more chaotic.

That's the current goal. Simulating other things is out of my wheelhouse, I'm not a game dev, just a novice inventor. If I'm done my plans or if I get people working on this thing with me and they're interested in this, I had another idea. Add on this a turn based card game town management bit or something. The LLMs are gonna take their sweet time, so a second phase of gameplay while the first does it's stuff is a good idea. Something simple that doesn't require a lot of computation. I want to add a resource managment aspect, and having gold and pops through some sort of basic thing, even if it's just an idle game, that's more world simulated without another order of magnitude of storylines.

Right now we're not there. The simplest bit, the place the player interacts with the game isn't close to done and it's the simpliest. The rest I've got but ideas for. I still need to setup the GUI. I started this project with no experience on the first of april, and a proper build's not gonna be out for at least a year.

The memory system is still really underdeveloped. I want a sown seeds text file for the prompt writer, I want town folders tied to a 2d plane with cords, and I want character files. Doing this well is going to take a lot of creativity.

The independent storylines thing isn't hard. All I need to do is have the memory system and LLM interface stuff figured out. I have something working for the LLM interface, but it's kinda dogshit unless I'm mistaken. Besides that it's just applying what I've already got.

The writing prompts thing also relies on the memory system. Writing through the different systems I'm just now realizing I've been putting this off. 

Evaluation isn't that hard. Only part that's in the air is how it interacts with the memory system and that's old news by now.

Interaction needs work. The way the LLM is called needs work, so do the prompts, and commands need to be figured out, and I just want to make it better written. Conversation.py rewrite underway.

GUI's a matter of doing it. Something that looks good is gonna take some time, but I want something working for now.

I also need to write out the starting info and write out docs for changing around that stuff.



Planning doc has more, it might be outdated, but so might the readme. Here: [Plans_and_Files.md](plans_and_files.md).



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

The current build only works for the first turn and it's honestly not worth playing if I didn't break something. I had an ok time testing it, you're better off playing with DungeonAI or running a game of Pathfinder.



## How this project works and future plans

Refer to [Plans_and_Files.md](Plans_and_files.md)

## Contributing

Refer to [CONTRIBUTING.md](CONTRIBUTING.md)

Outdated, just contact me, I'm the only one working on this thing, I know some people have seen this project, but the extent is a star and a watch, and I'd be 100% open to talk about it if you're interested.

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
