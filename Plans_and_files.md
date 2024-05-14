If you want a deeper look into how this project works, and where it's going, this is the place to look. Expect things to change, this is a public project and I am still figuring out how it's going to work.

If you want to help send me a message or look through this for something to work on / some of the other files in this thing, I tried to comment in what I had in mind.


## Game Design

This is an overview of the idea I've got for how the game's gonna look.

This isn't the most organised project or planning doc. I had close to no programming experience when I started this thing, I've been working on this thing for a month, but still. 

### Idea

The player is given 10 pre-written situations to deal with. They write in what they want to say or do, and an LLM decides what happens. I want as much structure as possible for the LLM.

There are 10 events per turn, and after the player makes their decisions, a whole lot of stuff happens under the hood. First off, there are to be a set of storylines or happenings going on independent from the player. For turn 1, the prompts are taken from the prompts.json file in the root directory, after that the prompts are written by an instance of the LLM. Simularally, 10 or so active agents / things with motivations are provided for the first turn.

Here's the procedure the game goes through at the end of the player's turn:

1. The LLM takes relevant info out of each situation's text log
2. The results of those decisions are determined through the LLM's decisonmaking and the roll of dice called by LLM
3. The LLM evaluates how those effect the independent storylines. For the first turn what the active agents / core member(s) of storyline do are given, after that based on the longer term goals, world, etc, etc, the following actions are created.
4. The LLM decides how the independent agent's actions + plans + whatever turn out / are effected
5. All the stuff that's happened is recorded in new copy of memory folder created for turn, has to be done in a readable way(here or earlier on)
6. Based on current state of world, what happened, and other stuff, ideas for what could happen are added to list of sown seeds. You don't need to plan your story out if you set a good enough foundation, this is a list of stuff that could come up again.
7. Write the prompts - This is a big one I don't know exactly how I'm gonna handle. Check if independent storylines get close enough to player for them to cross paths in some form, check to see if there's any scheduled / setup events for current turn, get some proportion of sown seeds + write out prompt, and fill the rest with prompts based on some set of data from memory.

then it loops back around.


The biggest thing I haven't quite figured out is the memory system. It's pivotal for this project and I don't know exactly how it's going to work. I think I want to have an LOD inspired thing with the capital city, the nearby area, stuff a short ways away, and stuff far away tracked seperately with pre-determined details like towns, landmarks, and the specifics of those details tracked. This should also enable simulation of other town's economies in a way the more flexable LLM can interact with. 

Then characters, independent storylines, and other stuff should have their own sections. Character motivations are really important, both in the longer + shorter terms for what I've got in mind.

Accessing stored data is also going to be tough, but hopefully it can be managed to some extent. If I can get the prompt writing script to get all the relevant info, hopefully I can include that in the context and have the LLM call for info the player references it doesn't know about. still precarious to say the least.

Also, I plan on saving each turn's data seperately since you might want to read back through after a good playthrough / for debugging to see why something weird happened / looking through the stuff that happened you had no involvement in for characters you like / did cool stuff. New memory folder created for every turn / something. 

Storylines the player instigated / is involved with should also be kept track of. I don't know how far I want this to be pushed. Simulating 50 AI characters doing their buisness every month / season is not reasonable, but I want characters to do stuff they would do.



## Now, soon, and later

### Current State of Game

Right now there is a working build, but it is as bare bones as you can get. It's in essence a chatbot. However, I've rewritten a lot of it more than once, and as this is an ambitious project, I've tried to keep it as modular as I could. I'm laying the groundwork for something actually interesting and I've got an idea of where I'm headed. 


Proper doccumentation is gonna come later, I'm not organized enough to edit things every time I update this project, look through it yourself, send me a message, or wait for me to get around to making this thing more professional and put together. 


### Roadmap

There is no working build for this project. Right now a lot of the code required for a full turn hasn't been written, and it will take a while to get to that point, let alone a clean build you can play ad infinitum.


##### Cleanup / work that I'm gonna get around to: 
(not part of current goal)

Moving readme, license, this doc, etc to a docs folder or whatever
Formalizing the formatting and applying it
Documentation / adding comments



#### Current Goal: 

First proper version:
Alpha Version 0.1.0 

It will be done when it's done, and that won't be for some time. I'd say the work I've got in mind will probably take like a month or two, but I am not great with timelines and this is the first cohesive plan I've setup. It's may 5th as of writing this btw. 


Main features:
- Proper UI (temp + very barebones)
- LLM Interface + Other LLM API Support
- Better prompting
- Commands
- Preparation for proper game

NOTE - this build will NOT include planned memory systems, prompt writing systems, and moving past turn 1. That's gonna take a few months to like a year if things continue at the current pace. 


#### More in depth breakdown:

I've started work planning and implementing various features, and I've done this to the extent that I think I've got enough to make a cohesive update to this project. 

##### Proper UI

The only reason I feel comfortable putting this here is because some simple tkinter stuff written by chatgpt seems to really work well. I've got a prototype for the LLM settings selection thing, and it's just fricking perfect. Then all I need is a basic main menu and a chat interface with a few buttons and I don't think that's gonna be too hard, since I've already got the backend setup. Only reason this is here is because I've been working on commands and writing in {next} is kinda lame. I also might add in some screen for the end of the turn to have that there for when the main gameplay loop is ready. 

##### LLM Interface + Other LLM API Support

This is a big one. Apparently you can get LLMs to respond in a custom json format, depending on the API you use. Right now I just call the LLM as a chatbot with a conversation log. I'm going to look into OpenAI's API and other LLM APIs. I don't know much about LLM API stuff. According to ChatGPT HuggingFace's Transformers thing is the other main LLM conversational / whatever text generation thing, and I'm probably going to look at that. I don't know what I'm talking about, I know that, if you know about this stuff send me a message or something, if you don't I'll get around to putting in the time to figure whatever stuff out.

Besides conversation.py, llm_interface.py needs to change, alongside a better way to change the settings. I've doe that last one already, minus the input details and having the rest of the project interact with it. 

##### Better Prompting

This is kinda nessesitated by several things, and I've been meaning to get around to it. First off, I've started some groundwork for the write prompt stuff, and changing the prompting to be more rigid in the formatting to easier obtain and express info is a good step. Second, I'm changing the conversation.py LLM formatting anyways, so why not. Third, commands. Fourth, it's better if the LLM knows exactly what it's supposed to be doing. Fifth, I want to break up each prompt into it's own chatlog, so even more stuff around the prompting stuff. I can't really put this off for another release.

##### Commands

I've got a decent way's into it, I might redo most of it to better align with the API, this is an important piece I'm ready to implement and it's gonna be great!

Prep for proper game (Moving beyond turn 1)

Various stuff including cleaning up the code. I want to seperate the prompts to not run into token limits and keep the LLM on task, implement the format_prompts.py script I made to handle existing saves, and whatever else. Basically everything fits into this category, but I'm keeping this here.


Also the retcon command where you can edit the last message you sent / get the LLM to try the thing again. Also options for rerolling probabilities rolled if the LLM rolled dice.

I could've forgotten some stuff / might add stuff on if things go well, or I feel like it.

#### Later down the road

The three main things I haven't really started work on yet are the memory system, the simulation, and the prompt generator.

The memory system works as you would intuit, the LLM gathers relevant info + that info is retrieved. Beyond that it's up in the air. 

Simulation refers to the world going on around the player. I plan on having a set amount of story / plotlines going on that impact the world around the player, potentially alongside some more mechanical stuff W what season it is being tracked. I'm not going to get deep into it right now, but I have a good idea of what I want in my head and despite the amount of changes + work needed to implement it I'm confident in what it's gonna look like, despite how much resources it's gonna take up.

Prompt generation is going to be a pretty important part of this thing. I want the process to be rigid and a particular proportion coming from sown seeds / setup plotlines / what's already happened, alongside new stuff.

Then I'm gonna focus on making it run well all together, saving and loading games, being fun, etc. 

Then at some point graphics would be nice.

If I get everything planned done, a turn based town management thing would be interesting as a way to give the user something to do while the actually planned stuff happens.

