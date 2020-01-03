"""
Date: 2019-12-28
Purpose: Text editor application.
Author: Zach Archibald
"""

import tkinter as tk
import tkinter.filedialog as tkf
import os


class TextEditorApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Zach's Text Editor")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu)
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)
        menu.add_cascade(label="File", menu=file_menu)

        scroll = tk.Scrollbar(self.master)
        scroll.pack(side=tk.RIGHT, fill=tk.BOTH)
        text_area = tk.Text(self.master, padx=5, pady=5, borderwidth=3)
        text_area.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        text_area.config(yscrollcommand=scroll.set)


    def new_file(self):
        print("New File")

    def open_file(self):
        print("Open File")

    def save_file(self):
        print("Save File")
        save_file = tkf.asksaveasfile(mode="w", defaultextension=".txt")
        contents = str(self.text_area.get("1.0", tk.END))
        save_file.write(contents)
        save_file.close()


root = tk.Tk()
editor = TextEditorApplication(master=root)
editor.mainloop()
