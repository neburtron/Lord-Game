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

Not going to go into detail, might add it in later though.

4
llm_interface.py:
A simple script in charge of sending whatever server is hosting the LLM the messages, returning whatever the LLM responds with. Also stores data like the model being used, the temperature, the API Key, etc.


5
Value_Evaluation.py:
Temp script made for Conversation.py. Conversation.py calls a function in it with the chatlog array the LLM is given. Right now it just saves a file with that data, but this script is going to be responsible for starting or doing the 2nd part of the turn. 

There's some commented in plans here too.

6
Find_Commands.py:
Not yet implemented properly. The script itself works from what I can tell. the Conversation.py LLM commands script should work, and all that's needed to implement is writing in logic in Commands.py, and prompting the LLM better. For other sets of commands you need to do the same, but also write a python file in commands_callable the same as the one already in there.

Basically this script looks for {}'s in the text, puts them into an array, takes the given commands script to use (in Commands folder), and runs whatever functions are called, returning values for parent script to interpret.

7
Commands/Conversation_Commands.py
Set of commands the LLM instance run by Conversation.py, that directly interacts with the player has access to. Used by Find_Commands.py. 

Other Files:

8
Conversation_Start_Prompt.txt:
This is the prompt used for telling the LLM instances created by Conversation.py what it should be doing.

9
Prompts.json:
A set of prompts used for the first turn. Used by Conversation.py and will eventually be used in part 3 for the format + style the LLM should be writing in.

10
Saves
Empty folder
Empty folders made in it when you make a new save, and if you make it through turn 1, the LLM's context array from Conversation.py is dropped in there as a json.

11
commands_callable folder
folder full of python scripts containing list of functions different instances of LLM can call. Originally made for Find_Commands.py, as it uses a list of these functions to only call commands that exist.


### Roadmap

0. I'll change as I go

- Improve / fix scripts when I see problems

- Formatting: I think I should have lowercase script titles, I'm gonna probably change them in a while, but I'm not doing it now because it's a decent chunk of work to look through to check if I broke anything. I'm gonna lowercase + put_these_inbetween_words for new scripts. Sorry, I know, if you want me to fix it I'll do that sooner rather than later, just send me a message or something

- Documentation: I'm gonna try and fix this doc and the readme, and the other ones if I see problems with them. I did a decent amount of work today on this stuff, but it's kinda dull work.


1. Things I am going to focus on in the immediate future

- Plan out and develop how the memory and other attached, unbuilt systems are to work, and start turning that into actual working code
- add retcon / reroll command 
- Add stuff wherever I feel like


2. Other stuff I'm gonna probably work on in the not so immediate future

- Properly implement commands into Conversation.py + give the player their own python file in commands_callable
- Add info taken from memory to Conversation.py - either add a bit to prompts.json that calls to relevant data, or some other way of doing it.
- Implement stuff I plan on implementing, commented in throughout this project

- Work on building core gameplay. I don't know what I'm gonna focus on first, but right now I am focused on the LLM integration. Either eval, memory, fixing Conversation.py, adding more stuff to conversation.py, the balancing values part of the game I haven't setup yet, or something else.


3. Further away ideas

- Moving beyond turn 1 (there's not gonna be a playable build W more than one turn for a while unless things change.)

- Rewrite code: Probably a few times with more local + project wide rewrites. I've done it a few times already. I'm new to coding and I don't know the best way to get what I'm looking for. Not a good idea with where I'm at, I tried a little while ago and I just got lost, later down the road when I've got other systems setup like the memory stuff +/ the eval stuff.


4. I'll probably get around to it eventually

- Change it so that main.py or wherever else deletes saves if they aren't played in. Needed for Conversation.py, runs first turn's prompts if it's told it is a new turn, and that happens if the main.py script runs the create new save thing.

- add like 4 - 5 additional prompts to prompts.json. They should be rather normal prompts, not like the first, second, and last one. These are to be used to tell LLM what it should make prompts look like.

- Improving prompts

5. If I get what I want to get done none

- Add a GUI W buttons so you don't need to type {next} at the end of your message (when I fix commands)

- Add a simple, traditional turn based strategy game section the player goes through to give LLM more time to work on stuff some civ clone, or an idle game, or some card based thing, or something else.


I know this isn't that useful of a roadmap, but I don't feel comfortable enough setting more rigid plans.