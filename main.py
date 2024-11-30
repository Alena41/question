import tkinter as tk
from PIL import Image, ImageTk
import random


def on_no_hover(event):
    no_button.place(x=random.randint(0, 400), y=random.randint(0, 400))


def on_yes_click():
    img = Image.open("fon1.jpg")
    img = img.resize((root.winfo_width(), root.winfo_height()))
    img_tk = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk
    img_label.place(relx=0.5, rely=0.5, anchor='center')


root = tk.Tk()
root.title("Вопрос")
root.geometry("500x500")

question_label = tk.Label(root, text="Ты котик?", font=("Arial", 16))
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Да", command=on_yes_click)
yes_button.pack(side=tk.LEFT, padx=50)

no_button = tk.Button(root, text="Нет")
no_button.pack(side=tk.RIGHT, padx=50)
no_button.bind("<Enter>", on_no_hover)

root.mainloop()
