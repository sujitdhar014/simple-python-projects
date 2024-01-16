import random
from tkinter import *


root = Tk()

bg = PhotoImage(file = "image1.png")

canvas1 = Canvas( root, width = 930,
                 height = 620)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")


user_input = Entry(root, bd=0, bg="blue",width="22",  font=("Arial", 23), foreground="#00ffff")
user_input.place(x=30, y=50, width=100)




QA1 = ['hello', 'hi', '', 'hey!', 'hey']
Q2 = ['How are you?', 'How are you doing?']
Ans2 = ['Okay', "I'm fine"]
Q3=["what is your name?","what's your name"]
Ans3=['i am AeroOxy','i am a bot ']
Sorry= ["I am learning "]

def cb():
    user_text = user_input.get()
    if user_text.lower() in QA1:
        bot_text = random.choice(QA1)
        # user_input.delete(0,END)
    
    elif user_text in Q2:
        bot_text = random.choice(Ans2)
        # user_input.delete(0,END)
    elif user_text in Q3:
            bot_text = random.choice(Ans3)
    else:
        bot_text = Sorry
    output.config(text=bot_text)



Buttone= Button(root, text="Send",  width="10", height=2,command=cb, padx=5,
                    bd=1, bg="#008000", activebackground="#008000",foreground='#008000',font=("Arial", 12) )
Buttone.place(x=310, y=580, height=40)


scrollbar = Scrollbar(root, command="output" , cursor="star")
scrollbar.place(x=405,y=340, height=230)

output = Label(root, bd=1, bg="green", width="44",height=14, font=("Arial", 15), foreground="#00ffff",cursor='circle')

output.place(x=6,y=6, height=3, width=370)

output_canvas = canvas1.create_window( 15, 340, 
                                       anchor = "nw",
                                       window =output)
user_input_canvas = canvas1.create_window( 15, 580,
                                       anchor = "nw",
                                       window = user_input)

root.mainloop()
# root.geometry("930x620")
# root.configure(background='dark blue')