from tkinter import *
root = Tk()


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