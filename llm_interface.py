from openai import OpenAI
import commands




## Some LLM Details ##

# This script needs to be edited to work with different APIs + stuff


settings = None
client = None
is_starting = True

def starting():
    global settings
    global client

    settings = commands.load("Settings/OpenAI.json")

    if 'base_url' in settings:
        client = OpenAI(
            base_url=settings['base_url'], 
            api_key=settings['api_key']
        )
    else:
        client = OpenAI(
            api_key=settings['api_key']
        )
    
    global is_starting
    is_starting = False

# Results depend on model and other settings.

## Call Function ##
def main(msgs):
    global settings
    global client
    global is_starting
    
    if is_starting:
        starting()

    try:
        completion = client.chat.completions.create(
            model=settings['model'],
            messages=msgs,
            temperature=settings['temp'],
        )

        return completion.choices[0].message
    except Exception as e:
        commands.printspace(f"Error during LLM interaction: {e}")
        return None