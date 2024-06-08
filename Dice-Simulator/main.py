import customtkinter
from PIL import Image
import random

img = ["one", "two", "three", "four", "five", "six"]
def button_callback():
    choice = random.choice(img)
    my_image = customtkinter.CTkImage(light_image=Image.open("img\\"+choice+".png"),size=(100, 100))
    image_label = customtkinter.CTkLabel(app, image=my_image, text="")
    image_label.grid(row=1, column=0, padx=20, pady=20)

app = customtkinter.CTk()
app.title("Dice Roll")
app.geometry("350x200")
app.grid_columnconfigure(0, weight=1)

button = customtkinter.CTkButton(app, text="Roll", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()