import customtkinter
from customtkinter import filedialog
from pygame import font
from pathlib import Path

def fonts_getting():
    fonts = font.get_fonts()
    fonts.sort()
    return fonts


def main():
    ticket_GUI()
    
    

class ticket_GUI:
    def __init__(self):

        self.fonts = fonts_getting()
        #initialize root
        self.root = customtkinter.CTk()
        self.root.geometry("800x500")

        #text variables
        self.text_template = customtkinter.StringVar()
        self.text_output = customtkinter.StringVar()
        self.text_image = customtkinter.StringVar()
        self.text_font = customtkinter.StringVar()

        #initialize text variables
        self.text_template.set("No seleccionado")
        self.text_output.set("No seleccionado")
        self.text_image.set("No seleccionado")
        self.text_font.set("No seleccionado")
        

        #Boton seleccion de imagen
        self.btn_image = customtkinter.CTkButton(master=self.root,
                                                    text="Seleccionar ticket",
                                                    font=("Roboto",14),
                                                    command=self.select_image_file)
        
        self.btn_output_save = customtkinter.CTkButton(master=self.root,
                                                    text="Seleccionar carpeta destino",
                                                    font=("Roboto",14),
                                                    command=self.select_saving_path)
        
        self.btn_select_font = customtkinter.CTkButton(master=self.root,
                                                    text="seleccionar font",
                                                    font=("Roboto",14),
                                                    command=self.select_font_file)
        
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
        
        self.label_font = customtkinter.CTkLabel(master=self.root,
                                                textvariable=self.text_font,
                                                font=("Roboto",14))
        

        #checkboxes
        #self.check_letters = customtkinter.CTkCheckBox(master=self.root, text="Incluir letras?")

        #dropdown menu
        #self.dropdown_fonts = customtkinter.CTkComboBox(master=self.root,values=self.fonts)
       
        
        
        #posicionamiento de elementos 

        self.label_output.pack(padx=10,pady=12)
        self.label_image.pack(padx=10,pady=12)
        self.label_template.pack(padx=10,pady=12)
        self.label_font.pack(padx=10,pady=12)
        #self.check_letters.pack(padx=10,pady=12)
        self.btn_image.pack(padx=10,pady=12)
        self.btn_select_font.pack(padx=10,pady=12)
        self.btn_open_template.pack(padx=10,pady=12)
        self.btn_output_save.pack(padx=10,pady=12)
        self.btn_generate.pack(padx=10,pady=12)
        #self.dropdown_fonts.pack(padx=10,pady=12)
       
        

        self.root.mainloop()

    #select the image through a windows filedialog
    def select_image_file(self):
        self.image_path = filedialog.askopenfilename(title="Abrir archivo PNG",
                                                     filetypes=(("PNG","*.png"),("Todos los archivos (*.*)","*.*")))
        if self.image_path:
            display_image = Path(self.image_path).name
            self.text_image.set(display_image)
        #print(self.image_path)

    def select_saving_path(self):
        self.save_path = filedialog.askdirectory(title="Escoger lugar a guardar imágenes")
    
        if self.save_path:
            self.text_output.set(self.save_path)
        #print(self.save_path)

    def select_template_file(self):
        self.template_path = filedialog.askopenfilename(title="Abrir archivo xlsx",
                                                     filetypes=(("Excel (*.xlsx)","*.xlsx"),("Todos los archivos (*.*)","*.*")))
        
        if self.template_path:
            display_template = Path(self.template_path).name
            self.text_template.set(display_template)

    def select_font_file(self):
        self.font_path = filedialog.askopenfilename(title="Seleccionar archivo Font",
                                                     filetypes=(("Font file (*.ttf)","*.ttf"),("Font file (*.TTF)","*.TTF"),("Todos los archivos (*.*)","*.*")))
        print(self.font_path)
        if self.font_path:
            display_font = Path(self.font_path).name
            self.text_font.set(display_font)
            
    def generate_file(self):
        pass


if __name__ == "__main__":
    main()


