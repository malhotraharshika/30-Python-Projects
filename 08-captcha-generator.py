from io import BytesIO
from tkinter import *
from tkinter import messagebox
from random import *
from captcha.image import ImageCaptcha
import string

image = ImageCaptcha(fonts=[r'C:\Users\malho\Downloads\Chelsea_Market\ChelseaMarket-Regular.ttf', r'C:\Users\malho\Downloads\VT323\VT323-Regular.ttf'])

randum = str(randint(100000, 999999))
data = image.generate(randum)
assert isinstance(data, BytesIO)
image.write(randum, 'out.png')

def verify():
    global randum
    x = t1.get("0.0",END).strip()
    if (int(x)==int(randum)):
        messagebox.showinfo("success", "verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    randum = str(randint(100000, 999999))
    data = image.generate(randum)
    assert isinstance(data, BytesIO)
    image.write(randum, 'out.png')
    photo = PhotoImage(file="out.png")
    # l1.config(image=photo, height=100, width=200)
    l1.config(image=photo)
    l1.image = photo
    l1.update()
    # UpdateLabel()

root = Tk()
photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="submit", command=verify)
b2 = Button(root, text="refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()
