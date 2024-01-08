import customtkinter as ctk
from PIL import Image
from random import choice

def changeOurPhoto(option: str):
    Us.configure(image = eval(option + "PNG"))

def game():
    comChoice = choice(["Rock", "Paper", "Scissors"])
    ourChoice = Options.get()
    Computer.configure(image = eval(comChoice + "PNG"))
    if comChoice == ourChoice:
        winner.configure(text = "Tie!")
    else:
        if comChoice == "Rock":
            if ourChoice == "Paper":
                winner.configure(text = "You win!")
            else:
                winner.configure(text = "You lose!")
        elif comChoice == "Paper":
            if ourChoice == "Scissors":
                winner.configure(text = "You win!")
            else:
                winner.configure(text = "You lose!")
        else:
            if ourChoice == "Rock":
                winner.configure(text = "You win!")
            else:
                winner.configure(text = "You lose!")

window = ctk.CTk()
window.geometry("500x500")
window.resizable(False, False)
ctk.set_appearance_mode("dark")

RockPNG = ctk.CTkImage(Image.open("Rock.png"), size = (200, 200))
PaperPNG = ctk.CTkImage(Image.open("Paper.png"), size = (200, 200))
ScissorsPNG = ctk.CTkImage(Image.open("Scissors.png"), size = (200, 200))

ctk.CTkLabel(window, text = "Rock Paper Scissors", font = ("Arial", 35)).pack(pady = 10)

winner = ctk.CTkLabel(window, text = "", font = ("Arial", 25))
winner.pack()

Us = ctk.CTkLabel(window, image = RockPNG, font = ("Arial", 25), text = "")
Us.place(x = 25, y = 100)

Computer = ctk.CTkLabel(window, image = None, font = ("Arial", 25), text = "")
Computer.place(x = 275, y = 100)

Options = ctk.CTkOptionMenu(window, values = ["Rock", "Paper", "Scissors"], command = changeOurPhoto)
Options.place(x = 180, y = 325)

Go = ctk.CTkButton(window, text = "Go", command = game)
Go.place(x = 180, y = 375)

window.mainloop()
