from conversation import Talk
import commands
import os

def check_text_file():

    file_name = "llm_settings.json"
    
    # Check if the LLM details file exists
    if os.path.isfile(file_name):
        # Do nothing if so
        return
    else:
        # Array to store settings in
        details =[]

        commands.printspace("llm_settings.json not found. Enter your details below to automatically generate one, or write one yourself with the names used by OpenAI.")
        
        commands.printspace("What model do you want to use?")
        model = commands.input1().strip().lower()
        details.append({"model": model})

        commands.printspace("What temperature do you want to use (Doesn't really matter, I set it as 0.7)")
        temp = commands.input1().strip()
        details.append({"temp": temp})

        commands.printspace("What is your API Key?")
        API = commands.input1()
        details.append({"api_key": API})

        commands.printspace("Do you want to specify the URL? If you're using OpenAI's servers to run LLM leave this blank, if not put whatever here.")
        base_url = commands.input1().strip().lower()
        if base_url:
            details.append({"base_url": base_url})

        commands.printspace("")
        commands.printspace("")

        commands.printspace("If you mispelled anything, want to change the values, or otherwise want to change  things, open the llm_settings.json file and add, remove, or change stuff as you see fit.")

        commands.save(file_name, details) 
        # save to json file

        return

def makesave(save):
    # Implement proper logic later
    commands.printpure(f"Creating new save: {save}")
    try:
        os.mkdir ("Saves/" + save)
    except:
        commands.printspace("Didn't work")
    else:
        commands.printspace("Save Creation Success!")

def inputsave(existing_saves):
    
    commands.printspace("Saves:")

    # Display existing save names
    for save in existing_saves:
        commands.printpure(save)

    commands.printpure("")  # Blank line for spacing

    save_name = commands.input1()

    if save_name in existing_saves:
        Talk_Instance = Talk(save_name, False) # Replace this with formatprompts.json
    else:
        commands.printspace("No save found by that name. Type 'back' to write a different name, or type anything else to start a new game.")
        confirm = commands.input1()

        if confirm.lower() == "back":
            # Rerun function
            inputsave(existing_saves)
        else:
            makesave(save_name)
            Talk_Instance = Talk(save_name,True) # Replace this with formatprompts.json

def main():
    # Get nessisary LLM Settings
    check_text_file()

    # Start Prompt
    commands.printpure("")
    commands.printpure("Welcome to Lord Game!")
    commands.printpure("Type in the name of an existing save listed below, or a new name to create a new game.\n")
    commands.printpure("")
    commands.printpure("Note - Game saves are not fully implemented, and current version only goes up to turn 1.")
    commands.printpure("If you play all the way through, your progress will be saved, but you can't play an existing save without error or your old save being overwritten.")
    commands.printpure("")

    existing_saves = commands.list_saves()
    inputsave(existing_saves)

if __name__ == "__main__":
    main()