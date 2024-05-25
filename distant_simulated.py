import commands

"""

Distant Simulated script Planning

What this script does:

To make the world more real, I'm having other stuff going on in the world too.

In World Starting Info, there's gonna be a list of storylines.

Think the starting Prompts.json, but different. Instead of openended opportunities
for the player though, they're more active this person wants X to happen with enough
details to get the thing off the ground.

Core to this is the trajectory, the thing the agent is aiming towards. Alongside details
on who the person is, why they want what they want is also included. At the end of every 
turn, an LLM instance decides how the main character / simulated person the storyline tracks 
spends that turn. This is based on their trajectory and whatever other info the character has
access to, alongside other character / storyline details. This happens at the end of the turn
right before the next turn's set of prompts is written. 



After conversation.py, either the direct results of each decision / prompt / conversation 
are determined or before, an LLM instance goes through each prompt and storyline, and determine
if what happened as a result of the prompt will impact the independent storyline. If so, it does,
and whatever info is sent to the next step of the LLM. Some storylines can be ruled out if they're
happening in a far off town or something.

Next the results of the turn are determined. Based on a bunch of info provided to a fresh instance
of an LLM per storyline, a set of outcomes are written with probabilities. After this dice are rolled
and a new LLM instance determines what that means to the world and storyline and whatever else. This
includes changes to the trajectory.

independent storyline and results from the player's decisions coming into contact should be figured 
out later.

Then we've made ourselves back around to the start, the stuff the main character does / tries to do
next turn are decided and the other scripts do their thing. 



"""
