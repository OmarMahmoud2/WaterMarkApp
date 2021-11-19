from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog


root = Tk()

root.title('Photo Copyrighter')
root.minsize(500,500)
root.config(padx=50, pady=50)
x = 'logo.png'
img = Image.open(x)
img = img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img
panel.grid(column=1, row=0)


def text_logo(photo, text):
    with Image.open(photo).convert('RGBA') as img:
        fnt = ImageFont.truetype('font.otf', 22)
        draw = ImageDraw.Draw(img)
        draw.text((5,5),text ,'black',font=fnt)
        img.show()
        img.save('New.png', quality=95)


def photo_logo(photo, logo):
    photo = Image.open(photo).convert('RGBA')
    watermark = Image.open(logo).resize((90,90))
    photo.paste(watermark, (5, 5), watermark)
    photo.save('New.png', quality=95)
    photo.show()


def text_log():
    top = Toplevel(root)
    top.title('Text Logo')
    top.minsize(300,300)
    top.config(padx=40, pady=40)
    lab = Label(top, text='Text Logo', font=('Georgia', 29, 'bold'))
    lab.grid(column=1, row=0, pady=20)
    def openfilename():
        filename = filedialog.askopenfilename(title='Choose a picture')
        logo_text = ent.get()
        text_logo(filename, logo_text)
    leb = Label(top, text='Enter your text logo')
    leb.grid(column=1, row=1, padx=20)
    ent = Entry(top, bd=5)
    ent.grid(column=1, row=2, rowspan=2, padx=20)
    btn = Button(top, text='Choose a Photo', command=openfilename, relief=RAISED, padx=40, pady=20)
    btn.grid(column=1, row=4, padx=20, pady=20)



def photo_log():
    top = Toplevel(root)
    top.title('Photo Logo')
    top.minsize(300, 300)
    top.config(padx=40, pady=40)
    x = 'logo.png'
    img = Image.open(x)
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(top, image=img)
    panel.image = img
    panel.grid(column=1, row=0)
    def openfilename():
        filename = filedialog.askopenfilename(title='Choose a picture')
        return filename
    def logofile():
        logo = filedialog.askopenfilename(title='Choose a picture')
        photo_logo(openfilename(), logo)

    label = Label(top, text='Choose a logo photo \n then choose the photo ', font=('Times', 15, 'italic'), padx=40, pady=20)
    label.grid(column=1, row=4, padx=20, pady=20)
    btn1 = Button(top, text='Choose a logo then photo', command=logofile, relief=RAISED, padx=40, pady=20)
    btn1.grid(column=1, row=5, padx=20, pady=20)


btn = Button(root, text='Text Logo ', relief=RAISED, command=text_log, padx=50, pady=20)
btn.grid(column=0, row=1, padx=20, pady=20)


btn1 = Button(root, text='Photo Logo ', relief=RAISED, command=photo_log, padx=50, pady=20)
btn1.grid(column=2, row=1, padx=20, pady=20)

label= Label(root, text='2021@Omar Mahmoud')
label.grid(column=1, row=3,pady=20)

exit = Button(root, text='Exit', command=root.destroy, relief=RAISED, padx=50, pady=30)
exit.grid(column=1, row=2, pady=20)


root.mainloop()