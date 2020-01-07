import face_recognition
from tkinter import *
from PIL import Image, ImageTk

# config variables
IMAGE_LOCATION_KNOWN = "../images/almaz_office.jpg"
IMAGE_LOCATION_UNKNOWN = "../images/almaz_bike.jpg"
# IMAGE_LOCATION_UNKNOWN = "../images/almazer.jpg"
IMAGE_SCALE = 200

known_image = face_recognition.load_image_file(IMAGE_LOCATION_KNOWN)
unknown_image = face_recognition.load_image_file(IMAGE_LOCATION_UNKNOWN)

known_encoding = face_recognition.face_encodings(known_image)
unknown_encoding = face_recognition.face_encodings(unknown_image)

face_locations_known = face_recognition.face_locations(face_recognition.load_image_file(IMAGE_LOCATION_KNOWN))
face_locations_unknown = face_recognition.face_locations(face_recognition.load_image_file(IMAGE_LOCATION_UNKNOWN))

results = face_recognition.compare_faces([known_encoding[0]], unknown_encoding[0])
print(results[0])


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # Tkinter loads same image on its own
        image_known = Image.open(IMAGE_LOCATION_KNOWN)
        image_unknown = Image.open(IMAGE_LOCATION_UNKNOWN)

        top1, right1, bottom1, left1 = face_locations_known[0]
        top2, right2, bottom2, left2 = face_locations_unknown[0]

        cropped_image_known = image_known.crop([left1 - 20, top1 - 20, right1 + 20, bottom1 + 20])
        cropped_image_unknown = image_unknown.crop([left2 - 20, top2 - 20, right2 + 20, bottom2 + 20])

        cropped_image_known = cropped_image_known.resize((IMAGE_SCALE, IMAGE_SCALE), Image.ANTIALIAS)
        cropped_image_unknown = cropped_image_unknown.resize((IMAGE_SCALE, IMAGE_SCALE), Image.ANTIALIAS)

        render_known = ImageTk.PhotoImage(cropped_image_known)
        render_unknown = ImageTk.PhotoImage(cropped_image_unknown)

        label_known = Label(self, image=render_known)
        label_known.image = render_known

        label_unknown = Label(self, image=render_unknown)
        label_unknown.image = render_unknown

        label_known.place(x=50, y=50)
        label_unknown.place(x=300, y=50)

        text = Label(width=30, height=2, text="Это один и тот же человек" if results[0] else "Это разные человеки, хотя похожи", font="Arial 25", padx=0, pady=0)
        text.pack()


# Rendering window with size based on grid
root = Tk()
app = Window(root)
root.wm_title("Check Person")
root.geometry("550x350")
root.mainloop()
