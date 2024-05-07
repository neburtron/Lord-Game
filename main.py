from conversation import Talk
import commands
import select_llm_details

import os
import tkinter as tk					 
from tkinter import ttk 


def check_text_file():

    print("testing")
    select_llm_details.run_llm_settings()

    last_tab_index = commands.read("Settings/last_tab_index")
    selected = commands.read(last_tab_index)

    if selected == 0:
        details = commands.load("Settings/OpenAI.json")
        return details
    elif selected == 1:
        details = commands.load("Settings/HuggingFace.json")
        return details
    else:
        commands.printspace("Error with finding selected API")
        return None

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
    # Add if around here that checks if the settings files exist. 
    # Make the settings jsons and run check_text_file if not, this whole thing if so.

    commands.printpure("Do you want to change LLM settings? (write Y for yes, N for no)")    
    choose = commands.input1().strip().upper()
    
    if choose == "Y":
        check_text_file()
    elif choose == "N":
        pass
    else:
        commands.printspace ("you didn't type what I told you to, I am disapointed in you. You don't get to play anymore. Deleting python version 3.12 ...")

        commands.printspace("\n\n\n Successfully deleted Python.")
        return

    # Start Prompt
    commands.printspace("\n\n\n")
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