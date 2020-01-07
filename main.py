import face_recognition
import math
from tkinter import *
from PIL import Image, ImageTk

# config variables
IMAGE_LOCATION = "images/almaz_group.jpg"
IMAGE_SCALE = 200

# Getting face locations using face_recognition module
image = face_recognition.load_image_file(IMAGE_LOCATION)
face_locations = face_recognition.face_locations(image)

# Calculating grid for showing images in Tkinter
lf = len(face_locations)
grid_width = math.ceil(math.sqrt(lf))
grid_height = math.ceil(lf / grid_width)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Tkinter loads same image on its own
        load = Image.open(IMAGE_LOCATION)

        for i in range(lf):
            # Getting positions for each images
            top, right, bottom, left = face_locations[i]
            cropped = load.crop([left, top, right, bottom])

            # Resizing each image to same scale
            cropped = cropped.resize((IMAGE_SCALE, IMAGE_SCALE), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(cropped)
            img = Label(self, image=render)
            img.image = render

            # Setting image position according to the grid
            img.place(x=i % grid_width * IMAGE_SCALE, y=i // grid_width * IMAGE_SCALE)


# Rendering window with size based on grid
root = Tk()
app = Window(root)
root.wm_title("Faces")
root.geometry(str(grid_width * IMAGE_SCALE + 5) + "x" + str(grid_height * IMAGE_SCALE + 5))
root.mainloop()
