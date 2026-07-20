from tkinter import *
from PIL import Image, ImageTk, ImageSequence #pip install pillow
import time
from pygame import mixer
mixer.init()
root = Tk()
root.geometry("1000x500")
root.title("    JARVIS    ")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    #global img
    img = Image.open('JARVIS.gif')
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load('JARVIS AUDIO.wav')
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()
    root.mainloop()

play_gif()
