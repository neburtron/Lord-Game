import commands
import select_llm_details
from format_prompts import Prompts
import os

def main():
    commands.printpure("Do you want to change LLM settings? (write Y for yes, N for no)")
    choose = commands.input1().strip().upper()
    if choose == "Y":
        select_llm_details.run_llm_settings()
    elif choose != "N":
        commands.printspace("Invalid input. Exiting...")
        return

    # Display start text
    display_start_text("start_text.txt")

    existing_saves = commands.list_saves()
    inputsave(existing_saves)

def display_start_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            commands.printpure(line.strip() if line.strip() else "\n")

def makesave(save):
    try:
        os.mkdir("Saves/" + save)
        commands.printspace("Save Creation Success!")
        return "Success"
    except Exception as e:
        commands.printspace(f"Save Creation Failed: {e}")
        return "Save Creation Failed"

def inputsave(existing_saves):
    commands.printspace("Saves:")
    for save in existing_saves:
        commands.printpure(save)
    commands.printpure("")
    save_name = commands.input1()

    if save_name in existing_saves:
        Game_Instance = Prompts(save_name)
    else:
        commands.printspace("No save found by that name. Type 'back' to write a different name, or type anything else to start a new game.")
        confirm = commands.input1()
        if confirm.lower() == "back":
            inputsave(existing_saves)
        else:
            makesave(save_name)
            Game_Instance = Prompts(save_name)

if __name__ == "__main__":
    main()