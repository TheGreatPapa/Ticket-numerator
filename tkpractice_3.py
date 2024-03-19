import customtkinter
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

def login():
    print("logged")


root = customtkinter.CTk()
root.geometry("800x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Roboto",24))
label.pack()

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(padx=10, pady=12)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(padx=10,pady=12)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(padx=10,pady=12)

root.mainloop()

