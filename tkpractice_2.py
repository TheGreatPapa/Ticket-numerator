import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save")

        self.action_menu = tk.Menu(self.menu_bar,tearoff=0)
        self.action_menu.add_command(label="show message", command=self.show_message)

        self.menu_bar.add_cascade(menu=self.file_menu,label="File")
        self.menu_bar.add_cascade(menu=self.action_menu,label="Action")

        self.root.config(menu=self.menu_bar)
        
        self.label = tk.Label(self.root, text="Your message", font=("papyrus",14))
        self.label.pack(padx=20, pady=20)

        self.text_box = tk.Text(self.root, height=5, font=("Arial",16))
        self.text_box.bind("<KeyPress>",self.enter_shortcut)
        self.text_box.pack(padx=20,pady=20)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="show messagebox", font=("Arial",16),variable=self.check_state)
        self.check.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="message",font=("Arial",16),command=self.show_message)
        self.button.pack(padx=20,pady=20)

        self.clear_button = tk.Button(self.root, text="Clear",font=("Arial",16),command=self.clear)
        self.clear_button.pack(padx=20, pady=20)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.text_box.get('1.0',tk.END))
        else: 
            messagebox.showinfo(title="Message", message=self.text_box.get('1.0', tk.END))

    def enter_shortcut(self, event):
        if event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="do you really want to close?"):
            self.root.destroy()

    def clear(self):
        self.text_box.delete("1.0",tk.END)
   



MyGUI()