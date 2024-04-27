from Conversation import Talk
import Commands
import os


def makesave(save):
    # Implement proper logic later
    Commands.printpure(f"Creating new save: {save}")
    try:
        os.mkdir ("Saves/" + save)
    except:
        Commands.print("Didn't work")
    
    Commands.printspace("If an error didn't pop up, a folder was made for your game! If you use the next command on the last prompt, it'll automatically save the Array used by LLM.")

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