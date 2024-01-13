from tkinter import *

def filler():

    hide_stuff(howtotext)
    hide_stuff(backhome)
    
    hide_stuff(cell1)
    hide_stuff(cell2)
    hide_stuff(cell3)
    hide_stuff(cell4)
    hide_stuff(cell5)
    hide_stuff(cell6)
    hide_stuff(cell7)
    hide_stuff(cell8)
    hide_stuff(cell9)
    hide_stuff(cell10)
    hide_stuff(cell11)
    hide_stuff(cell12)
    
        


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
    
def startgame():
    hide_stuff(start)
    hide_stuff(howto)
    hide_stuff(quitgame)
    
    show_stuff(cell1)
    show_stuff(cell2)
    show_stuff(cell3)
    show_stuff(cell4)
    show_stuff(cell5)
    show_stuff(cell6)
    show_stuff(cell7)
    show_stuff(cell8)
    show_stuff(cell9)
    show_stuff(cell10)
    show_stuff(cell11)
    show_stuff(cell12)
    
    cell1.pack(side=LEFT)
    cell2.pack(side=LEFT)
    cell3.pack(side=LEFT)
    cell4.pack()
    
    cell5.pack(side=LEFT)
    cell6.pack(side=LEFT)
    cell7.pack(side=LEFT)
    cell8.pack()
    
    cell9.pack(side=LEFT)
    cell10.pack(side=LEFT)
    cell11.pack(side=LEFT)
    cell12.pack(side=LEFT)

def hide_stuff(widget):
    widget.pack_forget()

def show_stuff(widget):
    widget.pack()
    



root  = Tk(className="Pair Game")
root.geometry('700x700')
root.configure(bg='green')
root.title("Match The Pair By Pranav Veeraghanta")

# home section

topfiller = Label(root,text="\n\n\n\n\n\n\n\n\n\n\n\n",
                  bg='green')
topfiller.pack()

start = Button(root,text="Start Game",
               font=("Arial",25),
               bg="black",
               padx=40,
               fg='white',
               command=lambda:startgame())
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

howtotext = Label(root,text="\t     HOW TO PLAY\n\n1. Click on any 2 squares to reveal a number.\n\n2.If the numbers match you will get 100 points.\n\n3. If the numbers don't match the squares\n    will be hidden and you can try again.\n\n4. You have infinite number of tries!!!\n\n",
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


cell1 = Label(root,text="1",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell1.pack()

cell2 = Label(root,text="2",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell2.pack()

cell3 = Label(root,text="3",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell3.pack()

cell4 = Label(root,text="4",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell4.pack()

cell5 = Label(root,text="5",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell5.pack()

cell6 = Label(root,text="6",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell6.pack()

cell7 = Label(root,text="7",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell7.pack()

cell8 = Label(root,text="8",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell8.pack()

cell9 = Label(root,text="9",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell9.pack()

cell10 = Label(root,text="10",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell10.pack()

cell11 = Label(root,text="11",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell1.pack()

cell12 = Label(root,text="12",
              font=("Arial",25),
               bg="black",
               fg='white',)
cell12.pack()
























filler()


root.mainloop()
