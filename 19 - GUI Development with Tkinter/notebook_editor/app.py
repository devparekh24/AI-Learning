import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_contents = dict()


class ClosableNotebook(ttk.Notebook):
    def __init__(self, *args, **kw):
        self._active = None
        self._setup_style()
        kw.setdefault("style", "ClosableNotebook")
        super().__init__(*args, **kw)
        self.bind("<ButtonPress-1>", self._on_press, True)
        self.bind("<ButtonRelease-1>", self._on_release)

    @staticmethod
    def _make_x_image(name, fg, size=16):
        img = tk.PhotoImage(name=name, width=size, height=size)
        margin = 3
        for y in range(size):
            for x in range(size):
                on_diag1 = abs(x - y) <= 1
                on_diag2 = abs(x - (size - 1 - y)) <= 1
                in_bounds = margin <= x <= size - 1 - margin and margin <= y <= size - 1 - margin
                if (on_diag1 or on_diag2) and in_bounds:
                    img.put(fg, to=(x, y, x + 1, y + 1))
        return img

    def _setup_style(self):
        style = ttk.Style()
        self._img_close = self._make_x_image("img_close", "#606060")
        self._img_close_active = self._make_x_image("img_close_active", "#cc0000")
        self._img_close_pressed = self._make_x_image("img_close_pressed", "#880000")
        style.element_create(
            "close", "image", "img_close",
            ("active", "pressed", "!disabled", "img_close_pressed"),
            ("active", "!disabled", "img_close_active"),
            border=8, sticky="",
        )
        style.layout("ClosableNotebook", [("ClosableNotebook.client", {"sticky": "nswe"})])
        style.layout("ClosableNotebook.Tab", [
            ("ClosableNotebook.tab", {"sticky": "nswe", "children": [
                ("ClosableNotebook.padding", {"side": "top", "sticky": "nswe", "children": [
                    ("ClosableNotebook.focus", {"side": "top", "sticky": "nswe", "children": [
                        ("ClosableNotebook.label", {"side": "left", "sticky": ""}),
                        ("ClosableNotebook.close", {"side": "left", "sticky": ""}),
                    ]}),
                ]}),
            ]}),
        ])

    def _on_press(self, event):
        elem = self.identify(event.x, event.y)
        try:
            index = self.index("@%d,%d" % (event.x, event.y))
        except tk.TclError:
            return
        if "close" in elem:
            self.state(["pressed"])
            self._active = index
            return "break"

    def _on_release(self, event):
        if not self.instate(["pressed"]):
            return
        elem = self.identify(event.x, event.y)
        try:
            index = self.index("@%d,%d" % (event.x, event.y))
        except tk.TclError:
            pass
        else:
            if "close" in elem and self._active == index:
                self.select(index)
                self.event_generate("<<CloseTab>>")
        self.state(["!pressed"])
        self._active = None


def create_file(
    content="",
    title="Untitled",
):
    container = ttk.Frame(notebook)
    container.pack()
    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)
    notebook.add(container, text=title)
    notebook.select(container)
    text_contents[str(text_area)] = hash(content)
    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    else:
        if name[-1] == "*":
            notebook.tab("current", text=name[:-1])


def get_text_widget():
    tab_widgets = root.nametowidget(notebook.select())
    text_widgets = tab_widgets.winfo_children()[0]
    return text_widgets


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    confirm = messagebox.askyesno(
        message="You have unsaved changes. Do you want to close?",
        icon="question",
        title="Unsaved Changes",
    )
    return confirm


def close_current_tab():
    if current_tab_unsaved() and not confirm_close():
        return
    text_widget = get_text_widget()
    del text_contents[str(text_widget)]
    if len(notebook.tabs()) == 1:
        create_file()
    notebook.forget("current")


def confirm_quit():
    # for text_widget in notebook.winfo_children():
    #     if hash(text_widget.get("1.0", "end-1c")) != text_contents[str(text_widget)]:
    #         return True
    # return False
    unsaved = False
    for tab in notebook.tabs():
        tab_widget = notebook.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break
    if unsaved and not confirm_close():
        return False
    root.destroy()


def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        file_name = os.path.basename(file_path)
        text_widgets = get_text_widget()
        content = text_widgets.get("1.0", "end-1c")
        with open(file_path, "w") as f:
            f.write(content)
    except (AttributeError, FileNotFoundError):
        print("Save operation failed.")
        return
    notebook.tab("current", text=file_name)
    text_contents[str(text_widgets)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()
    try:
        file_name = os.path.basename(file_path)
        with open(file_path, "r") as f:
            content = f.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation failed.")
        return

    create_file(content, file_name)


def show_about_info():
    messagebox.showinfo(
        message="This is a simple text editor written in Python using Tkinter.",
        title="About",
    )


root = tk.Tk()
root.title("Notebook Editor")
root.geometry("800x700")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))


menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(
    label="Close Tab", command=close_current_tab, accelerator="Ctrl+W"
)
file_menu.add_command(label="Exit", command=confirm_quit)

help_menu.add_command(label="About", command=show_about_info)

notebook = ClosableNotebook(main)
notebook.pack(
    fill="both",
    expand=True,
)
notebook.bind("<<CloseTab>>", lambda _: close_current_tab())
create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-w>", lambda event: close_current_tab())

root.mainloop()
