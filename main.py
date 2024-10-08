from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox



window = Tk()
window.title("Add Watermark")
window.config(padx=30, pady=30, bg='lightblue')

canvas = Canvas(width=100, height=100, highlightbackground='white')

title = Label(text='Welcome to the Add Watermark App', font=('Victor Mono', 24, 'italic'), padx=30, pady=30, bg='lightblue',fg='white')
title.grid(column=0, columnspan=2, row=1)

logo_label = Label(text="Logo to be added:", bg='lightblue')
logo_label.grid(column=0, row=4)

logo_image = Image.open("./assets/cropped_logo.png")
new_logo_image = logo_image.resize((105, 105), Image.Resampling.LANCZOS)
logo= ImageTk.PhotoImage(new_logo_image)

canvas.create_image(0,0, image=logo, anchor=NW)
canvas.grid(column=1, row=4, padx=10, pady=10)

watermark_label= Label(text='Watermark Text:', bg='lightblue')
watermark_label.grid(column=0, row=6)

watermark_entry = Entry(width=25, bg='lightblue', highlightbackground='white')
watermark_entry.grid(column=1, row=6, padx=10, pady=10)

image_label= Label(text='Image File Name:', bg='lightblue')
image_label.grid(column=0, row=8)

image_entry = Entry(width=25, bg='lightblue', highlightbackground='white')
image_entry.grid(column=1, row=8, padx=10, pady=10)



def add_watermark():

    image_entry_text = image_entry.get()

    # add logo
    with Image.open(f"./assets/{image_entry_text}") as image:
        width, height = image.size

        font = ImageFont.load_default(30)
        draw = ImageDraw.Draw(image)
        text = watermark_entry.get()
        text_width = font.getlength(text)

        print(text_width)

        text_x = (width  /2 )- (text_width/2)
        text_y = height - 10 - 10 - 100

        draw.text((text_x,text_y), text, font=font)

        pasted_logo = Image.open("./assets/cropped_logo.png")
        pasted_logo_width = int(width*0.05)
        pasted_logo_height = int(height*0.05)
        logo_to_paste = pasted_logo.resize((pasted_logo_width, pasted_logo_height), Image.Resampling.LANCZOS)

        logo_x = (width - pasted_logo_width) //2
        logo_y = height - pasted_logo_height - 10

        image.paste(logo_to_paste, (logo_x, logo_y))
        image.save(f"./assets/new_{image_entry_text}")
        messagebox.showinfo(title="Saved! Close this program to see your new image!")


add_button = Button(text='Add', width=10, bg='lightblue', fg='black', highlightbackground='lightblue', command=add_watermark)
add_button.grid(column=0, columnspan=2, row=10)

window.mainloop()