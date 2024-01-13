from tkinter import *

def filler():

    hide_stuff(howtotext)
    hide_stuff(backhome)
    
    hide_stuff(score)
    
    hide_stuff(frame1)
    hide_stuff(frame2)
    hide_stuff(frame3)  
      


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
    
    show_stuff(score)
    
    show_stuff(frame1)
    show_stuff(frame2)
    show_stuff(frame3)
    
def hide_stuff(widget):
    widget.pack_forget()

def show_stuff(widget):
    widget.pack()
    
def checker(value,cellname):
    cellname.config(text=value)
    
    i=0
    a = [0,0]    
    
    for i in range(0,2):
        a[i] = value
        i = i+1

    if a[0] == a[1]:
        score.config(text="works")

##########################################################################

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

score = Label(root,text="Score : ",
              font=('Arial',15),
              bg='green',
              fg='white',)
score.pack()


frame1 = Frame(root,bg='green')
frame1.pack(side=TOP, padx=5, pady=5,)

frame2 = Frame(root,bg='green')
frame2.pack(side=TOP, padx=5, pady=5)

frame3 = Frame(root,bg='green')
frame3.pack(side=TOP, padx=5, pady=5)

cell1 = Button(frame1,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(1,cell1))
cell1.pack(side=LEFT,
           padx=10,
           pady=10)

cell2 = Button(frame1,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(2,cell2))
cell2.pack(side=LEFT,
           padx=10,
           pady=10)

cell3 = Button(frame1,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(5,cell3))
cell3.pack(side=LEFT,
           padx=10,
           pady=10)

cell4 = Button(frame1,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(4,cell4))
cell4.pack(side=LEFT,
           padx=10,
           pady=10)

#############################################################

cell5 = Button(frame2,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(2,cell5))
cell5.pack(side=LEFT,
           padx=10,
           pady=10)

cell6 = Button(frame2,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(1,cell6))
cell6.pack(side=LEFT,
           padx=10,
           pady=10)

cell7 = Button(frame2,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(3,cell7))
cell7.pack(side=LEFT,
           padx=10,
           pady=10)

cell8 = Button(frame2,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(6,cell8))
cell8.pack(side=LEFT,
           padx=10,
           pady=10)

########################################################

cell9 = Button(frame3,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(3,cell9))
cell9.pack(side=LEFT,
           padx=10,
           pady=10)

cell10 = Button(frame3,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(6,cell10))
cell10.pack(side=LEFT,
           padx=10,
           pady=10)

cell11 = Button(frame3,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(4,cell11))
cell11.pack(side=LEFT,
           padx=10,
           pady=10)

cell12 = Button(frame3,text="?",
              font=("Arial",25),
               bg="black",
               fg='white',
               command=lambda:checker(5,cell12))
cell12.pack(side=LEFT,
           padx=10,
           pady=10)





















filler()


root.mainloop()
