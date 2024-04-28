from Conversation import Talk
import Commands
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

        Commands.printspace("llm_settings.json not found. Enter your details below to automatically generate one, or write one yourself with the names used by OpenAI.")
        
        Commands.printspace("What model do you want to use?")
        model = Commands.input1().strip().lower()
        details.append({"model": model})

        Commands.printspace("What temperature do you want to use (Doesn't really matter, I set it as 0.7)")
        temp = Commands.input1().strip()
        details.append({"temp": temp})

        Commands.printspace("What is your API Key?")
        API = Commands.input1()
        details.append({"api_key": API})

        Commands.printspace("Do you want to specify the URL? If you're using OpenAI's servers to run LLM leave this blank, if not put whatever here.")
        base_url = Commands.input1().strip().lower()
        if base_url:
            details.append({"base_url": base_url})

        Commands.printspace("")
        Commands.printspace("")

        Commands.printspace("If you mispelled anything, want to change the values, or otherwise want to change  things, open the llm_settings.json file and add, remove, or change stuff as you see fit.")

        Commands.save(file_name, details) 
        # save to json file

        return

def makesave(save):
    # Implement proper logic later
    Commands.printpure(f"Creating new save: {save}")
    try:
        os.mkdir ("Saves/" + save)
    except:
        Commands.printspace("Didn't work")
    else:
        Commands.printspace("Save Creation Success!")

def inputsave(existing_saves):
    
    Commands.printspace("Saves:")

    # Display existing save names
    for save in existing_saves:
        Commands.printpure(save)

    Commands.printpure("")  # Blank line for spacing

    save_name = Commands.input1()

    if save_name in existing_saves:
        Talk_Instance = Talk(save_name)
    else:
        Commands.printspace("No save found by that name. Type 'back' to write a different name, or type anything else to start a new game.")
        confirm = Commands.input1()

        if confirm.lower() == "back":
            # Rerun function
            inputsave(existing_saves)
        else:
            makesave(save_name)
            Talk_Instance = Talk(save_name,True)


def main():
    # Get nessisary LLM Settings
    check_text_file()

    # Start Prompt
    Commands.printpure("")
    Commands.printpure("Welcome to Lord Game!")
    Commands.printpure("Type in the name of an existing save listed below, or a new name to create a new game.\n")
    Commands.printpure("")
    Commands.printpure("Note - Game saves are not fully implemented, and current version only goes up to turn 1.")
    Commands.printpure("If you play all the way through, your progress will be saved, but you can't play an existing save without error or your old save being overwritten.")
    Commands.printpure("")

    existing_saves = Commands.list_saves()
    inputsave(existing_saves)

if __name__ == "__main__":
    main()