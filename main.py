from tkinter import *
from PIL import Image,ImageTk
from random import randint

top = Tk()  
top.title("Rock Paper Scissor")
top.configure(background="#6bff93")  
top.geometry('470x540')



#Player and Comp heading
Player_label = Label(text="You ",font='900',bg='#6bff93',fg='Black').grid(row=0,column=0)
Comp_label = Label(text="Computer ",font='900',bg='#6bff93',fg='Black').grid(row=4,column=0)

Name_label = Label(text="Made by Puru ",font='900',bg='#6bff93',fg='Black').grid(row=0,column=4)


#Pictures
rock_img = ImageTk.PhotoImage(Image.open("images/Rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("images/Paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("images/Scissor.png"))

#opening Pictures
User_image = Label(top,image=rock_img,bg='#6bff93')
Comp_image = Label(top,image=paper_img,bg='#6bff93')
User_image.grid(row=1,column=0)
Comp_image.grid(row=3,column=0)




result_msg = Label(top, font='bold',bg="#6bff93",fg='black')
result_msg.grid(row=5)

#update result msg
def update_result(x):
    result_msg['text'] = x



#Checking who is winner
def Check_Win(player,computer):
    if player == computer:
        update_result("Its a draw !!")
    elif player == "rock":
        if computer == "paper":
            update_result("You lose")
        else:
            update_result("You Won")
    elif player == "paper":
        if computer == "scissor":
            update_result("You lose")
        else:
            update_result("You Won")
    elif player == "scissor":
        if computer == "rock":
            update_result("You lose")
        else:
            update_result("You Won")
    else:
        pass


choices = ["rock", "paper", "scissor"]

def Playerchoice(x):

    compChoice = choices[randint(0, 2)]

    if x == "rock":
        User_image.configure(image=rock_img)
    elif x == "paper":
        User_image.configure(image=paper_img)
    else:
        User_image.configure(image=scissor_img)


    if compChoice == "rock":
        Comp_image.configure(image=rock_img)
    elif compChoice == "paper":
        Comp_image.configure(image=paper_img)
    else:
        Comp_image.configure(image=scissor_img)

    Check_Win(x, compChoice)    



#buttons
rock = Button(top, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white",command=lambda: Playerchoice("rock")).grid(row=1, column=4,padx=40)
paper = Button(top, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white" ,command=lambda: Playerchoice("paper")).grid(row=2, column=4,padx=40)
scissor = Button(top, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white" ,command=lambda: Playerchoice("scissor")).grid(row=3, column=4,padx=40)




top.mainloop()  
