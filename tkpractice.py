import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.title("My first GUI")

label = tk.Label(root, 
                 text="Hello world!", 
                 font=("Arial", 18))
label.pack(padx=0,pady=20)

textbox = tk.Text(root, height=3, font=("Arial",16))
textbox.pack(padx=20)

my_entry = tk.Entry(root)
my_entry.pack()

button = tk.Button(root, text="click me", font=("Arial",16))
button.pack(pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial",16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial",16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial",16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial",16))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial",16))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial",16))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=("Arial",16))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=("Arial",16))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=("Arial",16))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

button_place = tk.Button(root, text="another one",font=("Arial",8))
button_place.place(x=500,y=20,width=200,height=30)


root.mainloop()

