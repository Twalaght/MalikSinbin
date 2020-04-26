import random
import tkinter
from PIL import ImageTk, Image

# Display a slideshow of the given images, with a delay for each
def slideshow(images, delay):
    def next_image():
        # Open the image, read in its size, and calculate the scale
        input_image = Image.open(next(img_iter))

        # Get image dimensions and scale it to fit screen
        dims = list(input_image.size)
        dims = [int(dims[0] * viewer.winfo_screenheight() / dims[1]), viewer.winfo_screenheight()]

        # Set the image into the displays label
        img_label.img = ImageTk.PhotoImage(input_image.resize((dims), Image.ANTIALIAS))
        img_label.config(image = img_label.img)
        img_label.after(delay, next_image)

    # Sets up the iterator, labels, and slideshow config
    random.shuffle(images)
    img_iter = iter(images)
    viewer = tkinter.Tk()
    viewer.config(background="#222222")
    viewer.attributes("-fullscreen", True)
    img_label = tkinter.Label(viewer)
    img_label.pack()

    # Call next image once to start recursion, and run the main loop
    next_image()
    viewer.mainloop()