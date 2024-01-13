from tkinter import *

def filler():

    hide_stuff(howtotext)
    hide_stuff(backhome)


def howtoplayinst(start,quit,howto):
    hide_stuff(start)
    hide_stuff(quit)
    hide_stuff(howto)
    
    
    show_stuff(howtotext)
    show_stuff(backhome)


def homepage():
    hide_stuff(howtotext)
    hide_stuff(backhome)

    show_stuff(start)
    start.pack(padx=20,pady=20)
    show_stuff(howto)    
    show_stuff(quitgame)
    quitgame.pack(padx=20,pady=20)
    

def hide_stuff(widget):
    widget.pack_forget()

def show_stuff(widget):
    widget.pack()
    



root  = Tk(className="Pair Game")
root.geometry('700x700')
root.configure(bg='green')
root.title("Pair Game By Pranav Veeraghanta")

# home section

topfiller = Label(root,text="\n\n\n\n\n\n\n\n\n\n\n\n",
                  bg='green')
topfiller.pack()

start = Button(root,text="Start Game",
               font=("Arial",25),
               bg="black",
               padx=40,
               fg='white')
start.pack(padx=24,pady=20)

howto = Button(root,text="How to Play",
               font=("Arial",25),
               bg="black",
               fg='white',
               padx=37,
               command=lambda:howtoplayinst(start,quitgame,howto))
howto.pack(padx=20)


quitgame = Button(root,text="Exit",
                  command=quit,
                  font=("Arial",25),
                   bg="black",
                   padx=95,
                   fg='white')
quitgame.pack(padx=20,pady=20)

# how to play section

howtotext = Label(root,text="\t     HOW TO PLAY\n\n1. Click on any 2 squares to reveal a picture.\n\n2.If the pictures match you will get 100 points.\n\n3. If the pictures don't match the cards\n    will be hidden and you can try again.\n\n4. You have infinite number of tries!!!\n\n",
                  font=('Arial',15),
                  bg='green',
                  fg='white',
                  padx=95,
                  justify=LEFT)



backhome = Button(root,text="Back",
                  font=("Arial",25),
               bg="black",
               fg='white',
               padx=90,
               command=lambda:homepage())

# game section:





























filler()


root.mainloop()
