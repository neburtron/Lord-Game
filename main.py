import commands
import select_llm_details
from format_prompts import Prompts
import os

def main():

    commands.printpure("Do you want to change LLM settings? (write Y for yes, N for no)")    
    
    choose = commands.input1().strip().upper()
    
    if choose == "Y":
        select_llm_details.run_llm_settings()
    elif choose == "N":
        pass
    else:
        commands.printspace ("you didn't type what I told you to, I am disapointed in you. You don't get to play anymore. Deleting python version 3.12 ...")

        commands.printspace("\n\n\n Successfully deleted Python.")
        return

    # Start Prompt
    commands.printspace("\n\n")
    commands.printpure("Welcome to Lord Game!")
    commands.printpure("Type in the name of an existing save listed below, or a new name to create a new game.\n")
    commands.printpure("")
    commands.printpure("Note - Game saves are not fully implemented, and current version only goes up to turn 1.")
    commands.printpure("If you play all the way through, your progress will be saved, but you can't play an existing save without error or your old save being overwritten.")
    commands.printpure("")
    
    existing_saves = commands.list_saves()
    inputsave(existing_saves)

def makesave(save):
    # Implement proper makesave stuff later
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
        Game_Instance = Prompts(save_name, False)
    else:
        commands.printspace("No save found by that name. Type 'back' to write a different name, or type anything else to start a new game.")
        confirm = commands.input1()

        if confirm.lower() == "back":
            # Rerun function
            inputsave(existing_saves)
        else:
            makesave(save_name)
            Game_Instance = Prompts(save_name,True)

if __name__ == "__main__":
    main()