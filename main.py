import customtkinter as ctk
from customtkinter import filedialog
from pygame import font
from pathlib import Path



def main():
    ticket_GUI()
    
    

class ticket_GUI:
    def __init__(self):

        #initialize root
        self.root = ctk.CTk()
        self.root.geometry("800x500")
        

        # Text variables
        self.text_template = ctk.StringVar()
        self.text_output = ctk.StringVar()
        self.text_image = ctk.StringVar()
        self.text_font = ctk.StringVar()

        # Initialize text variables
        self.text_template.set("No seleccionado")
        self.text_output.set("No seleccionado")
        self.text_image.set("No seleccionado")
        self.text_font.set("No seleccionado")

        # Frame for grid-managed widgets
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=10, pady=12)

        # Buttons
        self.btn_image = ctk.CTkButton(master=self.frame,
                                       text="Seleccionar ticket",
                                       font=("Roboto", 14),
                                       command=self.select_image_file)
        
        self.btn_output_save = ctk.CTkButton(master=self.frame,
                                             text="Seleccionar carpeta destino",
                                             font=("Roboto", 14),
                                             command=self.select_saving_path)
        
        self.btn_select_font = ctk.CTkButton(master=self.frame,
                                             text="seleccionar font",
                                             font=("Roboto", 14),
                                             command=self.select_font_file)
        
        self.btn_open_template = ctk.CTkButton(master=self.frame,
                                               text="abrir plantilla",
                                               font=("Roboto", 14),
                                               command=self.select_template_file)
        
        # Labels
        self.label_template = ctk.CTkLabel(master=self.frame,
                                           textvariable=self.text_template,
                                           font=("Roboto", 14))
        
        self.label_output = ctk.CTkLabel(master=self.frame,
                                         textvariable=self.text_output,
                                         font=("Roboto", 14))
        
        self.label_image = ctk.CTkLabel(master=self.frame,
                                        textvariable=self.text_image,
                                        font=("Roboto", 14))
        
        self.label_font = ctk.CTkLabel(master=self.frame,
                                       textvariable=self.text_font,
                                       font=("Roboto", 14))
        
        # Positioning elements with grid
        self.btn_output_save.grid(row=0, column=0, padx=10, pady=12)
        self.label_output.grid(row=0, column=1, padx=10, pady=12)
        
        self.btn_image.grid(row=1, column=0, padx=10, pady=12)
        self.label_image.grid(row=1, column=1, padx=10, pady=12)
        
        self.btn_select_font.grid(row=2, column=0, padx=10, pady=12)
        self.label_font.grid(row=2, column=1, padx=10, pady=12)
        
        self.btn_open_template.grid(row=3, column=0, padx=10, pady=12)
        self.label_template.grid(row=3, column=1, padx=10, pady=12)

        # Create a new frame for the generate button
        self.frame_generate = ctk.CTkFrame(self.root)
        self.frame_generate.pack(padx=10, pady=12, fill="x")

        self.btn_generate = ctk.CTkButton(master=self.frame_generate,
                                          text="Generar",
                                          font=("Roboto", 14),
                                          command=self.generate_file,
                                          fg_color="green")
        self.btn_generate.pack(padx=10, pady=12)

        self.root.mainloop()
       
        

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
            if len(self.save_path)> 10:
                display_save_path = ".../"+ self.save_path.rsplit("/",1)[-1]
            else:
                display_save_path = self.save_path
            self.text_output.set(display_save_path)
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


