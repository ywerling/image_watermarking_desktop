import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

WATERMARK_COLOR = 'green'
WATERMARK_FONT = 'arial.ttf'
WATERMARK_SIZE = 36

class ImageWatermarkingApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # create the tkinter UI basic structure
        self.config(padx=400, pady=300)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)

        # put widget on UI
        self.canvas = tk.Canvas(width=200, height=150, bg="#f7f5dd", highlightthickness=0)
        self.canvas_img = ImageTk.PhotoImage(file="assets/black_hexagon.png")
        self.image_id = self.canvas.create_image(100, 100, image=self.canvas_img, tag='image')
        self.canvas.grid(row=1, column=1)
        self.start_button = tk.Button(width=10, height=1, text="Select Image", command=self.ask_directory)
        self.start_button.grid(column=0, row=0)
        self.image_location = tk.Entry(width=35)
        self.image_location.grid(column=1, row=0)
        self.watermark_text = tk.Entry(width=50)
        self.watermark_text.grid(column=1, row=2)
        self.watermark_button = tk.Button(width=15, height=1, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.grid(column=0, row=2)
        self.save_button = tk.Button(width=10, height=1, text="Save Image", command=self.save_image)
        self.save_button.grid(column=2, row=2)


# open a dialogue to ask for the location of the image to watermark
    def ask_directory(self):
        image_path=filedialog.askopenfile().name
        # image_location.insert(0, image_path)
        canvas_open_img = Image.open(image_path)
        self.canvas_img = ImageTk.PhotoImage(canvas_open_img)
        self.canvas.itemconfig(self.image_id, image=self.canvas_img)


    def add_watermark(self):
        temp_image = ImageTk.getimage(self.canvas_img)
        watermark_str=self.watermark_text.get()
        text_overlay = Image.new("RGBA", temp_image.size, (255, 255, 255, 0))
        w_font = ImageFont.truetype(WATERMARK_FONT, WATERMARK_SIZE)
        d = ImageDraw.Draw(text_overlay)
        d.text((20, 20), watermark_str, font=w_font, fill=(255, 255, 255, 255))
        watermarked_image = Image.alpha_composite(temp_image, text_overlay)
        self.canvas_img=ImageTk.PhotoImage(watermarked_image)


    def save_image(self):
         formats = [('Bitmap', '*.bmp'), ('Portable Network Graphics', '*.png'), ('JPEG', '*.jpg'), ('GIF', '*.gif') ]
         name_save_file=filedialog.asksaveasfilename(filetypes=formats)
         savable_image = ImageTk.getimage(self.canvas_img)
         savable_image.save(name_save_file)


if __name__ == "__main__":
    window = tk.Tk()
    window.title="Image Watermarking Application"
    ImageWatermarkingApp(window)
    window.mainloop()
