from tkinter import *
import random

city = ['california', 'beirut', 'london','paris','sydney','washington d.c']
word = random.choice(city)
shuffle = (''.join(random.sample(word, len(word))))
index = 0
current_text = ""

def hint():
    global index, current_text
    if index < len(word):
        current_text += word[index]
        lb3.config(text=current_text)
        index += 1
    else:
        lb2.config(text="I N C O R R E C T", fg="red")

def answer():
    global index, current_text
    if e1.get() == word:
        randoms()
        v1.set("")
        lb2.config(text="C O R R E C T", fg="green")
        reset()
        lb3.config(text="")
    else:
        lb2.config(text="I N C O R R E C T", fg="red")
        v1.set("")



def randoms():
    global word, index, current_text
    word = random.choice(city)
    shuffle = (''.join(random.sample(word, len(word))))
    lb1.config(text=shuffle)
    reset()
    

def reset():
    global index, current_text
    index = 0
    current_text = ""


win =Tk()
win.geometry('400x400')
win.title("word scrambler")
lb1 =Label(win ,text=shuffle, fg='blue')
lb2 = Label(win ,text="" ,fg="green")
lb3 = Label(win ,text="", fg="green")
v1 = StringVar()
e1 = Entry(win, textvariable=v1)
bt1 = Button(win , text="my answer is", width=12, command=answer)
bt2 = Button(win ,text="hint", width= 12, command=hint)
bt3 = Button(win,text="pick another", width=12, command=randoms)

lb1.place(x=150 ,y=50)
lb2.place(x=250 , y =150)
lb3.place(x=250 ,y=200)
e1.place(x=150 , y=100)
bt1.place(x =150 ,y=150)
bt2.place(x =150 ,y=200)
bt3.place(x =150 ,y=250)

win.mainloop()