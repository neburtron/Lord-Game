from tkinter import *
root = Tk()

# Placeholder UI
# Just makes a window, a start and gamescreen frame (screen)
# And also a button on the start to go to gamescreen
# I have no intention to touch this until some other parts are done.


root.title("Hello, World!")
root.geometry("500x500")

label = Label(root, text="Hello, World!")
label.pack()

def start():
    startscreen.destroy()
    gamescreen.pack()




startscreen = Frame(root)
startscreen.pack()

startbutton = Button(startscreen, text="Start", command=start)
startbutton.pack()



gamescreen = Frame(root)

gamescreen.pack_forget()

thisworks = Label(gamescreen, text="This works!")
thisworks.pack()





root.mainloop()