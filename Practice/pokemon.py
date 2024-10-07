import requests, tkinter, io, urllib.request

from PIL import Image, ImageTk
from tkinter import PhotoImage



def get_pokemon():
    # label.pack_forget()
    url = f'https://pokeapi.co/api/v2/pokemon/{enter_pokemon.get().lower()}'

    response = requests.get(url)

    print(response.json())

    pic = response.json()['sprites']['front_default']
    
    image = Image.open(urllib.request.urlopen(pic))
    photo = ImageTk.PhotoImage(image)

    label = tkinter.Label(root, image=photo)
    label.image = photo
    label.pack()




root = tkinter.Tk()
root.geometry("600x600")
root.title("Pokedex")

title = tkinter.Label(root, text="Pokedex")
title.pack()

enter_pokemon = tkinter.Entry(root)
enter_pokemon.pack()

button = tkinter.Button(root, text="Get Pokemon", command=get_pokemon)
button.pack()

label = tkinter.Label(root)

root.mainloop()