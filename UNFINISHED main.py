from Conversation import Talk
import Commands

# NOT DONE YET
# Run Conversation.py until UNFINISHED disapears and this is just main.py.

def getsaves():
    # Replace this with logic to get contents of save folder
    # Put in commands.py
    saves = ["save1", "save2", "save3"]  # Temp list of existing save names
    return saves


def makesave(save):
    # Implement logic to create a new save with the given name later
    Commands.printpure(f"Creating new save: {save}")

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
            makesave(save_name)
            Talk_Instance = Talk(save_name)
        else:
            # Retry input if invalid choice
            inputsave(existing_saves)


def main():
    Commands.printspace("")
    Commands.printpure("Welcome to Lord Game!")
    Commands.printpure("Type in the name of an existing save listed below, or a new name to create a new game.\n")
    Commands.printpure("")

    existing_saves = getsaves()
    inputsave(existing_saves)

    

if __name__ == "__main__":
    main()