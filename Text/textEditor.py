"""
Date: 2019-12-28
Purpose: Text editor application.
Author: Zach Archibald
"""

from tkinter import *


class TextEditorApplication:
    def __init__(self, master):
        self.master = master
        master.title("Zach's Text Editor")

        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)

    def new_file(self):
        print("New File")

    def open_file(self):
        print("Open File")


def main():
    root = Tk()
    editor = TextEditorApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()