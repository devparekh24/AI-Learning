# import tkinter as tk
# from tkinter import ttk


# def greet():
#     print(f"Hello, {user_name.get() or 'World'}!")


# root = tk.Tk()
# root.title("My App")
# user_name = tk.StringVar()


# # Top widgets
# name_label = ttk.Label(root, text="Name:")
# name_label.pack(side="left", padx=10, pady=10)
# name_entry = ttk.Entry(root, textvariable=user_name)
# name_entry.pack(side="left", padx=10, pady=10)
# name_entry.focus()
# # greet_button.pack()


# # Frame for buttons (new line)
# button_frame = ttk.Frame(root)
# button_frame.grid(row=0, column=0)

# greet_button = ttk.Button(button_frame, text="Greet", command=greet)
# greet_button.grid(row=1, column=1)

# quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
# quit_button.grid(row=2, column=1)

# # greet_button = ttk.Button(root, text="Greet", command=greet)
# # greet_button.pack(
# #     side="left",
# #     padx=10,
# #     pady=10,
# #     fill="x",
# #     expand=True,
# # )
# # quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# # quit_button.pack(
# #     side="left",
# #     padx=10,
# #     pady=10,
# #     fill="x",
# #     expand=True,
# # )
# # quit_button.grid(
# #     column=1,
# #     row=0,
# #     padx=10,
# #     pady=10,
# #     sticky="nsew",
# #     columnspan=2,
# #     rowspan=2,
# #     ipadx=10,
# #     ipady=10,
# # )
# root.mainloop()

import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("My App")

user_name = tk.StringVar()

# ---- Row 1 (Name input) ----
top_frame = ttk.Frame(root)
top_frame.pack(pady=10)

name_label = ttk.Label(top_frame, text="Name:")
name_label.pack(side="left", padx=5)

name_entry = ttk.Entry(top_frame, textvariable=user_name)
name_entry.pack(side="left", padx=5)
name_entry.focus()

# ---- Row 2 (Buttons) ----
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

greet_button = ttk.Button(button_frame, text="Greet", command=greet)
greet_button.pack(side="left", padx=10)

quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.pack(side="left", padx=10)

root.mainloop()
