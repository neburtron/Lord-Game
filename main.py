from Conversation import Talk
import Commands

def makesave(save):
    # Implement logic to create a new save with the given name later
    Commands.printpure(f"Creating new save: {save}")
    Commands.printpure("NOTE: creating saves is not yet implemented.")

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
            Talk_Instance = Talk(save_name)


def main():
    Commands.printspace("")
    Commands.printpure("Welcome to Lord Game!")
    Commands.printpure("Type in the name of an existing save listed below, or a new name to create a new game.\n")
    Commands.printpure("")

    existing_saves = Commands.list_saves()
    inputsave(existing_saves)

     

if __name__ == "__main__":
    main()