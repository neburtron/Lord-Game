import json
import Call_LLM

def get_prompts(prompts_file='prompts.json'):
    # Get prompts from prompts JSON
    prompts = []
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