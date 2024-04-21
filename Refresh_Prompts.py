import json
import llm_interface
import Commands
"""
    Early start to new script. This is what goes after the eval script to use whatever info stored 
    + the turn 1 example scripts to create the next set of scripts. Barely started.

"""

def get_prompts(prompts_file='prompts.json'):
    # Get prompts from prompts JSON
    prompts = []
    # Replace W prompts script from Commands at some point
    try:
        with open(prompts_file) as f:
            prompts = json.load(f).get("prompts", [])
    except FileNotFoundError:
        print("Error: prompts.json file not found.")
    return prompts


def format_prompts():
    prompts = get_prompts()
    if prompts:
        for prompt in prompts:
            print(f"thing {prompt}")

if __name__ == "__main__":
    format_prompts()