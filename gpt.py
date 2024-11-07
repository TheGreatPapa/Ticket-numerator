import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image, ImageTk

class ImageClickApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Drag Circle to Get Coordinates")

        # Canvas for displaying image
        self.canvas = ctk.CTkCanvas(self.root, width=500, height=400)
        self.canvas.pack(padx=10, pady=10)

        # Button to select image file
        self.btn_select_image = ctk.CTkButton(master=self.root,
                                              text="Seleccionar imagen",
                                              font=("Roboto", 14),
                                              command=self.select_image_file)
        self.btn_select_image.pack(pady=10)

        # Button to get coordinates
        self.btn_get_coords = ctk.CTkButton(master=self.root,
                                            text="Obtener coordenadas",
                                            font=("Roboto", 14),
                                            command=self.get_coordinates)
        self.btn_get_coords.pack(pady=10)

        self.image = None
        self.scale_x = 1
        self.scale_y = 1
        self.circle = None
        self.drag_data = {"x": 0, "y": 0, "item": None}

    def on_circle_press(self, event):
        if self.circle is not None:
            # Record the item and its location
            self.drag_data["item"] = self.circle
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_circle_drag(self, event):
        if self.circle is not None:
            # Compute how much the mouse has moved
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            # Move the circle
            self.canvas.move(self.drag_data["item"], delta_x, delta_y)
            # Record the new position
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
            print(f"x:{event.x}, y:{event.y}")

    def on_circle_release(self, event):
        # Reset the drag data
        self.drag_data = {"x": 0, "y": 0, "item": None}
        

    def get_coordinates(self):
        if self.circle is not None:
            # Get the final coordinates
            
            coords = self.canvas.coords(self.circle)
            https://www.youtube.com/watch?v=52NXldtvOnE&ab_channel=Atlas
            if coords:
                print("Hello")
                x1, y1, x2, y2 = coords
                # Calculate the center of the circle
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                real_x = int(center_x / self.scale_x)
                real_y = int(center_y / self.scale_y)
                print(f"Coordinates on Canvas: ({center_x}, {center_y})")
                print(f"Real Coordinates: ({real_x}, {real_y})")

    def select_image_file(self):
        image_path = filedialog.askopenfilename(title="Abrir archivo PNG",
                                                filetypes=(("PNG", "*.png"), ("Todos los archivos (*.*)", "*.*")))
        if image_path:
            self.load_image(image_path)

    def load_image(self, image_path):
        # Load the image using PIL
        self.image = Image.open(image_path)
        # Calculate the scale factors
        self.scale_x = 500 / self.image.width
        self.scale_y = 400 / self.image.height
        # Resize the image to fit the canvas
        resized_image = self.image.resize((500, 400), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        # Create a small circle in the middle of the canvas
        self.circle = self.canvas.create_oval(240, 190, 260, 210, fill="red", outline="black")
        # Bind mouse events to the circle
        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_circle_press)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_circle_drag)
        self.canvas.tag_bind(self.circle, "<ButtonRelease-1>", self.on_circle_release)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageClickApp(root)
    root.mainloop()