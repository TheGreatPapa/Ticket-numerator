import customtkinter
from customtkinter import filedialog

def main():
    print("si sirvio")
    ticket_GUI()



class ticket_GUI:
    def __init__(self):
        
        #initialize root
        self.root = customtkinter.CTk()
        self.root.geometry("800x500")


        #Boton seleccion de imagen
        self.btn_imagen = customtkinter.CTkButton(master=self.root,
                                                    text="Select Image",
                                                    font=("Roboto",14),
                                                    command=self.select_image_file)
        
        self.btn_output_save = customtkinter.CTkButton(master=self.root,
                                                    text="Select output folder",
                                                    font=("Roboto",14),
                                                    command=self.select_saving_path)
        
        self.btn_open_template = customtkinter.CTkButton(master=self.root,
                                                    text="open template",
                                                    font=("Roboto",14),
                                                    command=self.select_template_file)
        
        
        #posicionamiento de elementos 
        
        
        
        self.btn_imagen.pack(padx=10,pady=12)
        self.btn_open_template.pack(padx=10,pady=12)
        self.btn_output_save.pack(padx=10,pady=12)

        self.root.mainloop()

    #select the image through a windows filedialog
    def select_image_file(self):
        self.image_path = filedialog.askopenfilename(title="Abrir archivo PNG",
                                                     filetypes=(("PNG","*.png"),("Todos los archivos (*.*)","*.*")))
        print(self.image_path)

    def select_saving_path(self):
        self.save_path = filedialog.askdirectory(title="Escoger lugar a guardar imágenes")
        print(self.save_path)

    def select_template_file(self):
        self.image_path = filedialog.askopenfilename(title="Abrir archivo xlsx",
                                                     filetypes=(("Excel (*.xlsx)","*.xlsx"),("Todos los archivos (*.*)","*.*")))
        print(self.image_path)

if __name__ == "__main__":
    main()


