from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry("500x500")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme('green')

app.title("Dinn-o-matic" )

img = ImageTk.PhotoImage(Image.open("food.png"))
background = ctk.CTkLabel(master=app, image=img)

frame = CTkFrame(master=app, fg_color = "#8EA15A", border_color="#F2F8E5", border_width=2)
frame.pack(expand=True)

label = CTkLabel(master=frame, text="Welcome to the \n Dinn-o-matic!", font=("Comic Sans", 20) )
entry = CTkEntry(master=frame, placeholder_text="Type something")
button = CTkButton(master=frame, text="Submit")

label.pack(expand=True, pady=10, padx=30)
entry.pack(expand=True, pady=10, padx=30)
button.pack(expand=True, pady=10, padx=30)

label = ctk.CTkLabel(master=app, text="Dinn-o-matic", font=("Comic Sans", 20), text_color= '#FFCC70')


app.mainloop()

