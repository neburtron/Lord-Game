If you want a deeper look into how this project works, and where it's going, this is the place to look. Expect things to change, this is a public project and I am still figuring out how it's going to work.




## Game Design

This is a summary of the current plans / idea for how this game is going to look if and when it's finished. Currently I'd not recommend reading through this part, it's not organized and I'm gonna edit it later. Maybe go for the current state of the game / some other section in this doc.

Really, right now I'm still working on how the game is to work, it's not going to make sense. Trust me, you're better off skipping it unless you looked at other stuff and want to help, this focuses on how the LLM aspects work and ignores everything else. It also talks about stuff in detail arbitrarally where and only where I thought of stuff to add, where I am now, working on certain bits of the project.



The game works in turns. There are ten events, prompts, or pre-written situations per turn, and the player's role is to react to them. This is the simple gameplay structure taken from Sort the Court that I am building on into something monsterous.

When you start a new game, there is some pre-set info like the first day's worth of events, some starting seperate storylines (things happening independent to player), and some details about the setting. Memory system hasn't been written yet and as there's a lot of unwritten sections of this thing, the working demo just works with the Prompts.json file in the root directory of this project for now.




The first thing to talk about is Conversation.py, where the player interacts with the LLM.

Give or take a chatbot
Right now it isn't done, but a working build of this script has been written.
The player is given a pre-written bit of text giving them a decision to make, and the player decides what they want to do. A chatbot RPs with the player if they want to ask questions or their decision takes more than one message

When the player (or later LLM) thinks the situation is done, they can call a command to end the turn. Currently this works by seeing if the user's input is "next" ignoring capitalization and  extra   spaces. Half implemented is a way to read text written in {}'s as commands, and execute them in an external script callable throughout the project. Not done yet. When there's a GUI, these'll probably be buttons. LLM can't yet call the Next commands and if this is going to turn into something, there's gonna need to be some care put into the prompting and working with the LLM to get it to respond as desired, and not halicinate new prompts, or ask the user to make decisions they shouldn't be making.

Biggest features not yet implemented is callable commands (by LLM and player), and access to the currently theoretical memory system. There's also a few missing prompts, give or take a few depending on if we want 10 examples for prompt writing section, or if we don't need that many. First, second, and last I think are a bit wierd, maybe a few others, so probably not the best examples.


Next, interpretion

Currently in development / being planned out.

Value_Evaluation is a temp script with some plans writen in it. It's called by Conversation.py, and right now just saves Array (LLMs version of conversation log) as a json file I think in the save file made in main.py

I am not going to go too far in depth with this, because it largely depends on how the memory system is going to be setup, and that is still really in the air. I just wrote the plans in that doc + if you want to know more maybe refer to that / just ask me about it. I might've just forgotten to mention whatever you're curious about, but I might've also just not figured out how I want to handle that, so be warned.

Simply put, summarize doccument in two senses: Story / lore notes (or changes), and value changes.

In this game, value changes come in the form of changes to a set of values the player has to manage. Like in Sort the Court. Unlike Sort the Court, I'm gonna be including value changes that happen every turn for X turns, until something stops it, or whatever other end states. 

Then there's story stuff. Summarize, remove fluff, seperate items from one another, maybe other stuff, and send 'em off to the memory system, distant_simulated.py, and the bit that writes new prompts.



Memory system

This is a really important part of this project, I'm kind of putting off working on it (or would be if I was less ambitious), and am at the point where I kind of need to think about how this is going to work to further develop the core gameplay of this project.

Memory is going to work as a timeline. At the end of every turn the conversation log is summarized, then the first script goes through and figures out how each thing effects the world. Somehow. New files are made as the system works along. new text files are made if references to a thing that doesn't exist are made and lore details are put in, last turn / however many turn's back files are updated with new information / updated to better fit the current state of the simulated world, and all of that stuff.

There should be either a summary of important content for each file, or they should be short enough to be accessible to LLM.

I want everything to be saved, because this is a story game, and being able to look back eventually is something I want to be possible.

I think the biggest things are figuring out the specifics and making this relatively simple idea work in practice with the limited nature of LLMs and whatever other problems I face.

Another thing - Storylines should be a thing. Things that are unresolved / currently being worked on that the player has access to. Either here or as part of the Eval bit, there should be a series of commands that gives the LLM control over setting something up to happen in a few days time, and whatever needs to be written to have those plans being interupted.



Writing new Prompts

This part is less pivotal and I don't think it's gonna be as hard, but I still need to figure out how I'm going to exactly handle it. At the end of every turn, new prompts need to be generated. Based on the current state of the world, maybe some stuff from the memory system, example prompts from Prompts.json, open storylines / events timetabled or ready to be used, etc, and write new prompts. This should follow the format of Prompts.json, and at the end of the script it should make a new script called Prompts.json + rename +/ move the last one. That or just make a new Prompts.json with the new prompts with an earlier bit renaming and moving the old Prompts{turn number}.json file.



That's a general look at the core LLM structure I'm thinking about, alongside implemented aspects. It is not coherent, it skips over / doesn't adress a bunch of stuff that is core to the project, but I'm currently reworking my plans and when I'm able to give a coherent overview of how the game design works, I will.




## Now, soon, and later

### Current State of Game

Right now there is a working build, but it is as bare bones as you can get. It's in essence a chatbot. However, I've rewritten a lot of it more than once, and as this is an ambitious project, I've tried to keep it as modular as I could.

Here's how this project works so far, in some detail. Plans / out of the way unfinished stuff will not be included, just what each thing is here for / what each thing does.

Starting with Python scripts:

1
main.py
This is the main script, and the one you should run if you want to run this project and it's not currently broken.

What it does:
- Print starting text
- Handles choosing save and making new saves
- Runs Conversaton.py W save's name, and a Bool var for if it's a newly made save

2
Commands.py
General script for doing stuff like making a new json file + saving thing to it. Called by other scripts.

What it does: (functions in it)
- save: Save thing to file
- Load: return contents of given json file 
- append: Add thing to end of file (Supports appending dictionaries in JSON format)
- read: Read contents of given file (for txt files I think)
- prompts: Load Prompts.json specifically. (how to work after builds W more than one turn commented in)
- printspace: Print input to terminal, but with empty space above and below
- printpure: Same as above, but without spaces. These are commands so it's easier to add a proper GUI
- input1: the 1's there so it's distinquishable from input(). Same idea as above, get user input. + return it
- list_saves: Used in main.py, list folders in save folder + return list

3
Conversation.py:
Currently the only core script implemented to any serious extent. Handle's the player's interaction with the game and hands off the conversation logs at the end. It's not perfect, the prompts aren't good and I still need to setup the commands properly, I need to get it to interact with the memory system + whatnot, but besides that it's pretty complete. Not polished, not done by any means, but it does what it should.

I went through the first 2 pretty thoroughly, but I think I'm gonna stop here and go back to describing files later. Rest are unedited from previous draft when this was part of the readme. It's out of date and I'm still working on formatting and whatnot. 

4
llm_interface.py:
A simple script in charge of sending whatever server is hosting the LLM the messages, returning whatever the LLM responds with. Also stores data like the model being used, the temperature, the API Key, etc.

5
Refreshed_Prompts.py
Temp script, this is for rewriting scripts and will be called at the end of eval when the user is reading through the results of turn. It's got some stuff in it, I don't remember what I was working on to have me make the script and the contents of it, but it's not all that important and should just be looked at as an extension of whatever calls it / as an early thing to deal with when properly developing the prompt writing section of this game.

6
Value_Evaluation.py:
Temp script made for Conversation.py. Conversation.py calls a function in it with the chatlog array the LLM is given. Right now it just saves a file with that data, but this script is going to be responsible for starting or doing the 2nd part of the turn. 

7
Find_Commands.py:
Currently unused. The script itself works from the tests I've done. All that's needed to implement it is getting whatever commands python script it's calling all setup, telling the LLM it can call the commands and telling it what they do, and writing in the call Find_Commands script + do what it says bit to the script calling it. Conversation.py has an unfinished version of this commented in. 

Basically this script looks for {}'s in the text, puts them into an array, gets the commands python file to use (in Commands folder), runs whatever functions, and returns values.

8
Commands/Conversation_Commands.py
Empty python script. Gonna be part of the giving LLM instances access to commands thing, made for the Conversation.py script / the LLM instance directly interacting with the user, has list of potential functions, made because I'm working on Find_Commnads.py.




Other Files:

9
Conversation_Start_Prompt.txt:
This is the prompt used for telling the LLM instances created by Conversation.py what it should be doing.

10
Prompts.json:
A set of prompts used for the first turn. Used by Conversation.py and will eventually be used in part 3 for the format + style the LLM should be writing in.

11
Saves
Empty folder
Empty folders made in it when you make a new save, and if you make it through turn 1, the LLM's context array from Conversation.py is dropped in there as a json.

12
Commands folder
folder full of python scripts containing list of functions different instances of LLM can call. Originally made for Find_Commands.py, as it uses a list of these functions to only call commands that exist.




### Roadmap
I'm gonna redo this later. this is old. I'm thinking more about how this project is going to look when it's done + how I want to implement things, so a lot of change is to come.

DONE (Just the stuff I plan on doing, not everything I end up implementing)
- Add a main script or parent script to Conversation.py, that takes on save file management



I'm not going to be the most organized. I'll move from place to place, but I'll try to work on one area at a time.

I'm thinking of going through again and fixing things. Make the code more intuitive and clear, and going through the documentation and fixing that in the process. Might not, might do it now, might do it later.

1 - Conversation.py
The plan for this project right now is to build up around Conversation.py. Before I move on there's some more stuff I want to work on in this script. 

- Give LLM access to commands + have it working as intended in Conversation.py (Started)
- Polish / edit existing scripts for expandability / modularity
- Additional info for LLM taken from elsewhere
- Probably a good idea to work out how I'm gonna implement core values 
    (values the player has to manage like gold, pops, etc.)
- retcon / reroll command
- Make it so that user message also runs the Find_Commands.py script, temporarally, so they can finish a thing, while also ending the converation naturally + whatnot. Better if they've got their own commands script.

2 - Saves
From there I am going to focus on save data. This is a pretty narritive focused game where what happens is generated as you go. Saving your stuff is pretty important. This is going to take some time, while rewriting Conversation.py I had saving in mind and know how user interactions through that script are going to happen.

- Change it so that it deletes saves if they aren't played in. Needed for Conversation.py, runs first turn's prompts if it's told it is a new turn, and that happens if the main.py script runs the create new save thing.




Prompts are going to be saved in Saves/{save}/Prompts, and this is going to include unused prompts, saved as Prompts.json, and used prompts as Prompts{turn number}.json.

I'm also focusing on trying to make this script more accessible and whatnot for people who are not myself. I've spent hours and hours on this readme and I started from scratch this morning. I think people have seen this thing, and although I think the comments I've got in my code are pretty clear, the more fundamental, planning and instructions have not been good for a while. I'm gonna make this shorter too. I know it's way too long.

### Other features I'm not doing right now, but at some point probably.


add 4-5 additional prompts to prompts.json so there's about 10, plus the first one, and maybe the second one, or last one W the demon, because they're gonna be used for telling the LLM what format to write in and those might convince it to do stuff like paralize the player + say it's the end of the day in the middle.

A command for until GUI is setup: print turn - print json like that made from Value_Evaluation.py.

Later into development, I want to move over to something with a GUI. Not for some time though

If the stuff I'm working on now is completed, there might be a second part of your turn, something with a more turn based, card style town management thing, or some sort of civ clone, or something else. the LLM stuff is gonna be really slow, even on strong devices if better models are used because they can be, so something for the player to do in the meantime is a good idea.



#### looser ideas
I like the idea of giving the LLM a sense of scale for what the values are worth at different intervals.

Probability either called by LLM through some command or automatically fired that LLM uses to decide what happens is a cool idea
