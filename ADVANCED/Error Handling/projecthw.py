import tkinter as tk
import json
import urllib.request
import requests

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)
    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image

def get_url():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTA1MWQ3ZTAtMmYxYS00ZWZjLWE0MDQtZWRkNzg0NGRkNmE1IiwidHlwZSI6ImFwaV90b2tlbiJ9.l0KPYD5Ty-Y41cX_O1_0_0zoX_4poKpNzCCAZNkvAJI"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['items'][0]['image_resource_url']


def render_image():
    try:
        error_label.place_forget()
        image_url = get_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title('AI Image Generator')
window.geometry('500x350')

error_label = tk.Label(window, text="Please write")

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

image_label = tk.Label(window)
image_label.place(x=125, y=70)

button = tk.Button(window, text='Create', height=1, command=render_image)
button.place(x=300, y=18)

window.mainloop()
