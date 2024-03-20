import customtkinter
from customtkinter import filedialog

def main():
    ticket_GUI()



class ticket_GUI:
    def __init__(self):

        #initialize root
        self.root = customtkinter.CTk()
        self.root.geometry("800x500")

        #text variables
        self.text_template = customtkinter.StringVar()
        self.text_output = customtkinter.StringVar()
        self.text_image = customtkinter.StringVar()

        #initialize text variables
        self.text_template.set("No seleccionado")
        self.text_output.set("No seleccionado")
        self.text_image.set("No seleccionado")

        #Boton seleccion de imagen
        self.btn_image = customtkinter.CTkButton(master=self.root,
                                                    text="Seleccionar ticket",
                                                    font=("Roboto",14),
                                                    command=self.select_image_file)
        
        self.btn_output_save = customtkinter.CTkButton(master=self.root,
                                                    text="Seleccionar carpeta destino",
                                                    font=("Roboto",14),
                                                    command=self.select_saving_path)
        
        self.btn_open_template = customtkinter.CTkButton(master=self.root,
                                                    text="abrir plantilla",
                                                    font=("Roboto",14),
                                                    command=self.select_template_file)
        
        self.btn_generate = customtkinter.CTkButton(master=self.root,
                                                    text="Generar",
                                                    font=("Roboto",14),
                                                    command=self.generate_file,
                                                    fg_color="green")
        
        #etiquetas
        self.label_template = customtkinter.CTkLabel(master=self.root,
                                                textvariable=self.text_template,
                                                font=("Roboto",14))
        
        self.label_output = customtkinter.CTkLabel(master=self.root,
                                                textvariable=self.text_output,
                                                font=("Roboto",14))
        
        self.label_image = customtkinter.CTkLabel(master=self.root,
                                                textvariable=self.text_image,
                                                font=("Roboto",14))
        

        #checkboxes
        self.check_letters = customtkinter.CTkCheckBox(master=self.root, text="Incluir letras?")

        
        #posicionamiento de elementos 

        self.label_output.pack(padx=10,pady=12)
        self.label_image.pack(padx=10,pady=12)
        self.label_template.pack(padx=10,pady=12)
        self.check_letters.pack(padx=10,pady=12)
        self.btn_image.pack(padx=10,pady=12)
        self.btn_open_template.pack(padx=10,pady=12)
        self.btn_output_save.pack(padx=10,pady=12)
        self.btn_generate.pack(padx=10,pady=12)

        self.root.mainloop()

    #select the image through a windows filedialog
    def select_image_file(self):
        self.image_path = filedialog.askopenfilename(title="Abrir archivo PNG",
                                                     filetypes=(("PNG","*.png"),("Todos los archivos (*.*)","*.*")))
        if self.image_path:
            self.text_image.set(self.image_path)
        #print(self.image_path)

    def select_saving_path(self):
        self.save_path = filedialog.askdirectory(title="Escoger lugar a guardar imágenes")
        self.text_output.set(self.save_path)
        if self.save_path:
            self.text_output.set(self.save_path)
        #print(self.save_path)

    def select_template_file(self):
        self.template_path = filedialog.askopenfilename(title="Abrir archivo xlsx",
                                                     filetypes=(("Excel (*.xlsx)","*.xlsx"),("Todos los archivos (*.*)","*.*")))
        print(self.image_path)
        if self.template_path:
            self.text_template.set(self.template_path)
            
    def generate_file(self):
        pass


if __name__ == "__main__":
    main()


