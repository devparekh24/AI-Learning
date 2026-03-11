import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, world!")


# tk._test()
root = tk.Tk()
root.title("My App")
root.geometry("600x400")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(
    side="left",
    padx=10,
    pady=10,
    fill="x",
    expand=True,
)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(
    side="left",
    padx=10,
    pady=10,
    fill="x",
    expand=True,
)


root.mainloop()
