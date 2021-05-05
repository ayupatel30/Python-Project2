#Ayushi Patel
#Type to Hear

#Imported Tkinter, gTTS, and playsound from library
from tkinter import *
from gTTS import gTTS
from playsound import playsound

#Its for font style, and font size for the display windowss and text.
top = Tk()
top.geometry("500x500")
top.configure(bg='ghost white')
top.title("DataFlair - TYPE TO HEAR")

Label(top, text = "TYPE_TO_HEAR", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(top,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(top, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

#Once user types the sentence they will be able to hear it because of the library we imported
def Type_to_hear():
    Message = entry_field.get()
    hear = gTTS(text = Message)
    hear.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
 
#It will help user exit
def Exit():
    top.destroy()

#It will help user reset the text and restart.
def Reset():
    Msg.set("")

#Button will be used when they want to click on category instead of writing it out
B =Button(top, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4')
B.place(x=25,y=140)

B =Button(top, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1')
B.place(x=100 , y = 140)

B =Button(top, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset)
B.place(x=175 , y = 140)

#Final statement for program to know it ready to run
top.mainloop()