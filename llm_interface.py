from openai import OpenAI
import commands


settings = None
client = None
is_starting = True

tab = commands.read("Settings/last_tab_index")
tab = 0 # Temp

def starting():
    global settings
    global client
    global is_starting
    if tab == 0:
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
    
        is_starting = False

    elif tab == 1:
        settings = commands.load("Settings/HuggingFace.json")

    else:
        return


## Call Function ##
def main(msgs):
    global settings
    global client
    global is_starting
    
    if tab == 0:

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
        
    elif tab == 1:
        
        return