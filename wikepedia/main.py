import wikipedia as wk
import tkinter
import requests
from PIL import ImageTk, Image
from io import BytesIO
def search():
    global input
    input = entry.get()
    #try:
    output = wk.summary(input)
    info = wk.page(input)
    image1 = info.images[0]
    print(image1)
    response = requests.get(image1)
    imagedata = response.text
    print(imagedata)
    image=ImageTk.PhotoImage(Image.open(BytesIO(imagedata)))
    label2.config(text = output)
    picture.config(image = image)
    #except:
    #   label2.config(text = "No results")
root = tkinter.Tk() 
frame = tkinter.Frame(root)
root.title("Wikipedia Search")
root.geometry("600x600")
label1 = tkinter.Label(root, text = 'Search here:')
label1.pack()
entry = tkinter.Entry(root)
entry.pack()
Button = tkinter.Button(root, text = "Search", command = search)
Button.pack()
label2 = tkinter.Label(frame, text = "", wraplength = 900)
label2.pack(pady = 40)
picture = tkinter.Label(frame)
picture.pack()
frame.pack()
root.mainloop()