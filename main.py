#!/usr/bin/env python3

import customtkinter as ctk
import openpyxl
from customtkinter import filedialog
from pygame import font
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm
import os



def main():
    ticket_GUI()
    
class WarningDialog(ctk.CTkToplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Warning")
        self.geometry("500x150")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text=message, font=("Roboto", 14))
        self.label.pack(padx=20, pady=20)

        self.btn_ok = ctk.CTkButton(self, text="Bueno :(", command=self.on_ok)
        self.btn_ok.pack(pady=10)

        # Make the dialog modal
        self.grab_set()
        self.focus_set()
        self.transient(parent)
        self.bell()  # Make default warning sound

    def on_ok(self):
        self.grab_release()
        self.destroy()

class ticket_GUI:

    

    def __init__(self):
        
        #initialize root
        self.root = ctk.CTk()
        self.root.geometry("400x750")
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.root, orientation="horizontal", mode="determinate")
        self.progress_bar.pack(padx=10, pady=12, fill="x")
        self.progress_bar.set(0)

        #ticketing variables
        self.image_path= ""
        self.save_path = ""
        self.template_path = ""
        self.font_path = ""
        

        # Text variables
        self.text_template = ctk.StringVar()
        self.text_output = ctk.StringVar()
        self.text_image = ctk.StringVar()
        self.text_font = ctk.StringVar()
        self.tb_color = ctk.StringVar()
        self.tb_lx_coord = ctk.StringVar()
        self.tb_ly_coord = ctk.StringVar()
        self.tb_nx_coord = ctk.StringVar()
        self.tb_ny_coord = ctk.StringVar()
        self.tb_font_size = ctk.StringVar()

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
        self.label_hex = ctk.CTkLabel(master=self.frame,
                                       text="Color #HEX value (FFFFFF)",
                                       font=("Roboto", 14))
        self.label_lx = ctk.CTkLabel(master=self.frame,
                                       text="Coordenada letra x",
                                       font=("Roboto", 14))
        self.label_ly = ctk.CTkLabel(master=self.frame,
                                       text="Coordenada letra y",
                                       font=("Roboto", 14))
        self.label_nx = ctk.CTkLabel(master=self.frame,
                                       text="Coordenada numero x",
                                       font=("Roboto", 14))
        self.label_ny = ctk.CTkLabel(master=self.frame,
                                       text="Coordenada numero y",
                                       font=("Roboto", 14))
        self.label_font_size = ctk.CTkLabel(master=self.frame,
                                    text="Tamaño de fuente",
                                    font=("Roboto", 14))

        
        #textboxes
        self.color_entry = ctk.CTkEntry(master=self.frame,
                                        textvariable=self.tb_color,
                                        placeholder_text="#HEX value (FFFFFF)")

        self.letter_x_coord = ctk.CTkEntry(master=self.frame,
                                        textvariable=self.tb_lx_coord,
                                        placeholder_text="Letra coordenas x")
        self.letter_y_coord = ctk.CTkEntry(master=self.frame,
                                        textvariable=self.tb_ly_coord,
                                        placeholder_text="Letra coordenas y")

        self.number_x_coord = ctk.CTkEntry(master=self.frame,
                                        textvariable=self.tb_nx_coord,
                                        placeholder_text="Numero coordenas x")
        self.number_y_coord = ctk.CTkEntry(master=self.frame,
                                        textvariable=self.tb_ny_coord,
                                        placeholder_text="Numero coordenas y")
        self.font_size_entry = ctk.CTkEntry(master=self.frame,
                                    textvariable=self.tb_font_size,
                                    placeholder_text="Tamaño")


        # Positioning elements with grid
        self.btn_output_save.grid(row=0, column=0, padx=10, pady=12)
        self.label_output.grid(row=0, column=1, padx=10, pady=12)
        
        self.btn_image.grid(row=1, column=0, padx=10, pady=12)
        self.label_image.grid(row=1, column=1, padx=10, pady=12)
        
        self.btn_select_font.grid(row=2, column=0, padx=10, pady=12)
        self.label_font.grid(row=2, column=1, padx=10, pady=12)
        
        self.btn_open_template.grid(row=3, column=0, padx=10, pady=12)
        self.label_template.grid(row=3, column=1, padx=10, pady=12)

        self.label_hex.grid(row=4,column=0,padx=10,pady=12)
        self.color_entry.grid(row=4,column=1, padx=10, pady=12)
        
        self.label_lx.grid(row=5,column=0,padx=10,pady=12)
        self.letter_x_coord.grid(row=5,column=1, padx=10, pady=12)

        self.label_ly.grid(row=6,column=0,padx=10,pady=12)
        self.letter_y_coord.grid(row=6,column=1, padx=10, pady=12)

        self.label_nx.grid(row=7,column=0,padx=10,pady=12)
        self.number_x_coord.grid(row=7,column=1, padx=10, pady=12)

        self.label_ny.grid(row=8,column=0,padx=10,pady=12)
        self.number_y_coord.grid(row=8,column=1, padx=10, pady=12)

        self.label_font_size.grid(row=9, column=0, padx=10, pady=12)
        self.font_size_entry.grid(row=9, column=1, padx=10, pady=12)

        # Create a new frame for the generate button
        self.frame_generate = ctk.CTkFrame(self.root)
        self.frame_generate.pack(padx=10, pady=12, fill="x")

        self.btn_generate = ctk.CTkButton(master=self.frame_generate,
                                          text="Generar",
                                          font=("Roboto", 14),
                                          command=self.generate_file,
                                          fg_color="green")
        

         # Create a new frame for the letters checkbox
        self.frame_checkbox = ctk.CTkFrame(self.root)
        self.frame_checkbox.pack(padx=10, pady=12, fill="x")
        #checkbox
        self.chk_letters = ctk.CTkCheckBox(master=self.frame_checkbox,
                                           text="Incluir letras?", 
                                           font=("Roboto",14))
        
        
        self.chk_letters.pack(padx=10,pady=12)
        self.btn_generate.pack(padx=10, pady=12)
               

        self.root.mainloop()



    #select the image through a windows filedialog
    def select_image_file(self):
        self.image_path = filedialog.askopenfilename(title="Abrir archivo PNG",
                                                     filetypes=(("PNG","*.png"),("Todos los archivos (*.*)","*.*")))
        if self.image_path:
            display_image = Path(self.image_path).name
            self.text_image.set(display_image)


    def select_saving_path(self):
        self.save_path = filedialog.askdirectory(title="Escoger lugar a guardar imágenes")
    
        if self.save_path:
            if len(self.save_path)> 10:
                display_save_path = ".../"+ self.save_path.rsplit("/",1)[-1]
            else:
                display_save_path = self.save_path
            self.text_output.set(display_save_path)
             

    def select_template_file(self):
        self.template_path = filedialog.askopenfilename(title="Abrir archivo xlsx",
                                                     filetypes=(("Excel (*.xlsx)","*.xlsx"),("Todos los archivos (*.*)","*.*")))        
        if self.template_path:
            display_template = Path(self.template_path).name
            self.text_template.set(display_template)     


    def select_font_file(self):
        self.font_path = filedialog.askopenfilename(title="Seleccionar archivo Font",
                                                     filetypes=(("Font file (*.ttf)","*.ttf"),("Font file (*.TTF)","*.TTF"),("Font file (*.otf)","*.otf"),("Todos los archivos (*.*)","*.*")))
        if self.font_path:
            display_font = Path(self.font_path).name
            self.text_font.set(display_font)

            
    def generate_file(self):
        self.progress_bar.set(0)
        if not self.font_path or not self.save_path or not self.template_path or not self.image_path:
            WarningDialog(self.root, "Seleccione todos los archivos correctamente")
        else:
            if self.chk_letters.get():
                max_column = 2
            else:
                max_column = 1
            
            colour = self.tb_color.get()
            if not colour:
                colour = "ffffff"
        
            #open excel template
            # Load the workbook and select the first sheet
            workbook = openpyxl.load_workbook(self.template_path)
            sheet = workbook.active
            # Initialize a list to store the values
            data_values = []

            # Iterate through the rows of the first two columns
            for row in sheet.iter_rows(min_row=1, min_col=1, max_col=max_column, values_only=True):
                # Append the tuple (value1, value2) to the list
                if self.chk_letters.get():
                    
                    data_values.append([row[0],row[1]])
                else:
                    data_values.append(row[0])
            
            #open image template
            template = Image.open(self.image_path)
            draw = ImageDraw.Draw(template)

            #define font and size
            font = ImageFont.truetype(self.font_path, size=100)
    
            # Define the position where you want to place the number
            x1_position = int(self.letter_x_coord.get())
            y1_position = int(self.letter_y_coord.get())
            x2_position = int(self.number_x_coord.get())
            y2_position = int(self.number_y_coord.get())

            #iterations
            num_tickets = len(data_values)
            # Loop through each ticket

            # Inside generate_file method, update the font size based on user input
            font_size = int(self.tb_font_size.get()) if self.tb_font_size.get().isdigit() else 100  # Default to 100 if empty or invalid

            # Define font and size
            font = ImageFont.truetype(self.font_path, size=font_size)

            if self.chk_letters.get():
                for i in range(num_tickets):
                    # Draw the number on the ticket
                    draw.text((x1_position, y1_position), str(data_values[i][0]), fill=f"#{colour}", font=font)
                    draw.text((x2_position, y2_position), str(data_values[i][1]), fill=f"#{colour}", font=font)
                    
                    # Save the ticket with the number
                    ticket_path = f"{self.save_path}/ticket_{i}.png"
                    template.save(ticket_path)
                    
                    # Open the template again for the next iteration
                    template = Image.open(self.image_path)
                    draw = ImageDraw.Draw(template)
            else:
                for i in range(num_tickets):
                    # Draw the number on the ticket
                    draw.text((x1_position, y1_position), str(data_values[i]), fill=f"#{colour}", font=font)
                    
                    # Save the ticket with the number
                    ticket_path = f"{self.save_path}/ticket_{i}.png"
                    template.save(ticket_path)
                    
                    # Open the template again for the next iteration
                    template = Image.open(self.image_path)
                    draw = ImageDraw.Draw(template)
        self.images_to_pdf()
          # Grab the image from folder and store them in a pdf
            
    def images_to_pdf(self):
        pdf_path = f"{self.save_path}/tickets.pdf"
        page_width, page_height = 279 * mm, 432 * mm
        c = canvas.Canvas(pdf_path, pagesize=(page_width, page_height))

        # User-defined layout and margins
        images_per_sheet_layout = (8, 3)
        document_margin = 5 * mm
        image_margin = 0.5 * mm
        rows, cols = images_per_sheet_layout

        # High PPI setting for better quality
        ppi = 300  # Set to 300 PPI for higher quality

        # Calculate available width and height for images in points (1 point = 1/72 inch)
        available_width = page_width - 2 * document_margin
        available_height = page_height - 2 * document_margin
        img_width = (available_width - (cols - 1) * image_margin) / cols
        img_height = (available_height - (rows - 1) * image_margin) / rows

        # Convert img_width and img_height to pixels for resizing (based on the target PPI)
        img_width_px = int(img_width / (1 / (ppi / 72)))
        img_height_px = int(img_height / (1 / (ppi / 72)))

        # Background color in RGB for #F8F4F4
        background_color = (249/255, 234/255, 225/255)

        # Get all image files in the save path
        image_files = sorted(Path(self.save_path).glob("ticket_*.png"))
        if not image_files:
            print("No images found to add to PDF.")
            return

        total_images = len(image_files)
        progress_step = 1 / total_images  # Step increment for each image

        sheet_count = 1
        image_index = 0
        for img_file in image_files:
            # Draw background color for each new page
            if image_index % (rows * cols) == 0:
                c.setFillColorRGB(*background_color)
                c.rect(0, 0, page_width, page_height, fill=True, stroke=False)

            # Calculate position on the grid
            row = (image_index // cols) % rows
            col = image_index % cols
            x_offset = document_margin + col * (img_width + image_margin)
            y_offset = page_height - document_margin - (row + 1) * img_height - row * image_margin

            # Resize the image to higher quality
            img = Image.open(img_file)
            img = img.resize((img_width_px, img_height_px), Image.ANTIALIAS)
            temp_img_path = f"{self.save_path}/temp_{img_file.name}"
            img.save(temp_img_path, dpi=(ppi, ppi))
            c.drawImage(temp_img_path, x_offset, y_offset, width=img_width, height=img_height)
            os.remove(temp_img_path)

            image_index += 1

            # Update the progress bar
            self.progress_bar.set(min(1, self.progress_bar.get() + progress_step))

            # Start a new page if the current sheet is filled
            if image_index % (rows * cols) == 0:
                c.showPage()
                sheet_count += 1

        if image_index % (rows * cols) != 0:
            c.showPage()  # Ensure the last page is added if partially filled

        c.save()
        print(f"PDF with {sheet_count} sheet(s) successfully generated at {pdf_path}")

if __name__ == "__main__":
    main()