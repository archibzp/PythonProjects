"""
Date: 2019-12-28
Purpose: Text editor application.
Author: Zach Archibald
"""

import tkinter as tk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm


class TextEditorApplication(tk.Frame):
    def __init__(self, master=None):
        super(TextEditorApplication, self).__init__(master)
        self.master = master
        self.update_title(None)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Main text area
        self.text_area = tk.Text(self.master, padx=5, pady=5, borderwidth=3)

        # Vertical Scrollbar
        scroll = tk.Scrollbar(self.master)
        scroll.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.text_area.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self.text_area.config(yscrollcommand=scroll.set)

        # Build menu
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="New Window", command=self.new_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu, tearoff=False)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear", command=self.clear)
        menu.add_cascade(label="Edit", menu=edit_menu)

        format_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="View", menu=format_menu)

    def cut(self):
        self.copy()
        self.delete_selection()

    def copy(self):
        try:
            selection = str(self.text_area.selection_get())
            self.clipboard_clear()
            self.clipboard_append(selection)
        except tk.TclError:
            pass

    def paste(self):
        item = self.clipboard_get()
        mark = self.text_area.mark_next('current')
        # If current selection is a range, delete that range prior to pasting
        self.delete_selection()
        self.text_area.insert(mark, item)

    def delete_selection(self):
        '''
        Used by cut and paste functions to delete selected text
        '''
        try:
            first_index = self.text_area.tag_ranges('sel')[0]
            last_index = self.text_area.tag_ranges('sel')[1]
            self.text_area.delete(first_index, last_index)
        except IndexError:
            pass

    def clear(self):
        self.text_area.delete("1.0", tk.END)

    def new_file(self):
        print("New File")
        if self.data_loss_warning():
            self.text_area.delete("1.0", tk.END)
            self.update_title(None)

    def open_file(self):
        print("Open File")
        if self.data_loss_warning():
            file = tkf.askopenfile(mode="r")
            if file is not None:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", content)
                self.update_title(file)

    def save_file(self):
        print("Save File")
        file = tkf.asksaveasfile(mode="w", defaultextension=".txt")
        contents = str(self.text_area.get("1.0", tk.END))
        file.write(contents)
        self.update_title(file)
        file.close()

    def new_window(self):
        root2 = tk.Tk()
        new_editor = TextEditorApplication(master=root2)
        new_editor.mainloop()

    def update_title(self, file):
        if file is not None:
            file_path = file.name
            file_name = file_path.split("/")[-1]
            self.master.title("Text Editor  -  " + file_name)
        else:
            self.master.title("Text Editor  -  (New File)")

    def data_loss_warning(self):
        return tk.messagebox.askyesno(title="Message", message="Opening a new file will lose any "
                                                               "unsaved work. Continue?")


root = tk.Tk()
editor = TextEditorApplication(master=root)
editor.mainloop()
