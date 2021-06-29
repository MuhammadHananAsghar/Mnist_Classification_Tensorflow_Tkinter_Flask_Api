from tkinter import *
from PIL import Image
import uuid
import numpy as np
import os
import requests
import json

URL = "http://56f73cc857b2.ngrok.io/model"


current_x, current_y = 0,0
def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y

def addline(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), width=40,fill='black',capstyle=ROUND,smooth=True)
    current_x, current_y = event.x, event.y

def reset_canvas():
    canvas.delete("all")
    
    
def predict_canvas():
    filename = uuid.uuid4().hex
    canvas.postscript(file=f"{filename}.eps")
    img = Image.open(f"{filename}.eps")
    img = img.resize((28, 28))
    img = np.array(img).tolist()
    os.remove(f"{os.path.abspath(os.getcwd())}/{filename}.eps")
    requested_data = json.dumps({'img': img})
    response = requests.post(URL, requested_data)
    var.set(f"Prediction : {response.text}")
    
window = Tk()
var = StringVar()


# Configrations
window.title("Hand Digits Recognition")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)

# Canvas
canvas = Canvas(window, height=440, width=500)
canvas.place(x=0, y=0)
canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)

# Buttons
button_predict = Button(window, text ="Predict", width=10, height=3, command=predict_canvas)
button_predict.place(x=10, y=445)
label = Label(window, textvariable=var)
label.place(x=180, y=460)
button_reset = Button(window, text ="Reset", width=10, height=3, command=reset_canvas)
button_reset.place(x=390, y=445)

window.mainloop()