from openai import OpenAI
import commands

settings = None
client = None
is_starting = True
tab = commands.read_file("Settings/last_tab_index")
tab = 0  # Temp

def initialize_openai():
    global settings, client, is_starting

    settings = commands.load_json("Settings/OpenAI.json")
    client = OpenAI(
        base_url=settings.get('base_url'),
        api_key=settings['api_key']
    )
    is_starting = False

def initialize_huggingface():
    global settings, is_starting

    settings = commands.load_json("Settings/HuggingFace.json")
    is_starting = False

def starting():
    if tab == 0:
        initialize_openai()
    elif tab == 1:
        initialize_huggingface()
    else:
        return

def main(msgs):
    global settings, client, is_starting

    if is_starting:
        starting()

    if tab == 0:
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
        # Placeholder for future HuggingFace integration
        return