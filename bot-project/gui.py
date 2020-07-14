from tkinter import *
import os
from PIL import ImageTk, Image


def onClick():
    print("Button clicked")
    root.destroy()
    import bot
    os.system('bot.py')


root = Tk()
root.title("SpaceX Discord Bot")
photo = PhotoImage(file="F:\\Programming\\Discord\\bot-project\\spacex.png")
root.iconphoto(False, photo)
root.geometry("600x650+10+20")

my_img = ImageTk.PhotoImage(Image.open(
    'F:\\Programming\\Discord\\bot-project\\spacex.png'))
my_label = Label(image=my_img)
my_label.pack()

btn1 = Button(root, text="Run Bot", command=onClick)

btn1.pack()


root.mainloop()
