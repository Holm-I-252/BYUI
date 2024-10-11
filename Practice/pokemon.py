import requests, tkinter, io, urllib.request

from PIL import Image, ImageTk
from tkinter import PhotoImage


pokemon_present = False

def get_pokemon():
    global pokemon_present, label, type_label, hp_label, attack_label, defense_label, special_attack_label, special_defense_label, speed_label, weight_label, base_stats

    if pokemon_present:
        label.pack_forget()
        type_label.pack_forget()
        hp_label.pack_forget()
        attack_label.pack_forget()
        defense_label.pack_forget()
        special_attack_label.pack_forget()
        special_defense_label.pack_forget()
        speed_label.pack_forget()
        weight_label.pack_forget()
        base_stats.pack_forget()

    #Get data from pokeapi

    url = f'https://pokeapi.co/api/v2/pokemon/{enter_pokemon.get().lower()}'

    response = requests.get(url)

    print(response.json())

    #get sprite image and display it

    pic = response.json()['sprites']['front_default']
    
    image = Image.open(urllib.request.urlopen(pic))
    photo = ImageTk.PhotoImage(image)

    label = tkinter.Label(root, image=photo)
    label.image = photo
    label.pack()

    #display type

    if len(response.json()['types']) > 1:
        type_label = tkinter.Label(root, text=f"Type: {response.json()['types'][0]['type']['name'].capitalize()} & {response.json()['types'][1]['type']['name'].capitalize()}")
    else:
        type_label = tkinter.Label(root, text=f"Type: {response.json()['types'][0]['type']['name'].capitalize()}")
    type_label.pack()

    base_stats = tkinter.Label(root, text="Base Stats:")
    base_stats.pack()

    #display hp

    hp_label = tkinter.Label(root, text=f"HP: {response.json()['stats'][0]['base_stat']}")
    hp_label.pack()

    #display attack

    attack_label = tkinter.Label(root, text=f"Attack: {response.json()['stats'][1]['base_stat']}")
    attack_label.pack()

    #display defense

    defense_label = tkinter.Label(root, text=f"Defense: {response.json()['stats'][2]['base_stat']}")
    defense_label.pack()

    #display special attack

    special_attack_label = tkinter.Label(root, text=f"Special Attack: {response.json()['stats'][3]['base_stat']}")
    special_attack_label.pack()

    #display special defense

    special_defense_label = tkinter.Label(root, text=f"Special Defense: {response.json()['stats'][4]['base_stat']}")
    special_defense_label.pack()

    #display speed

    speed_label = tkinter.Label(root, text=f"Speed: {response.json()['stats'][5]['base_stat']}")
    speed_label.pack()

    #display weight

    weight_label = tkinter.Label(root, text=f"Weight: {response.json()['weight']} hectograms")

    pokemon_present = True





root = tkinter.Tk()
root.geometry("600x600")
root.title("Pokedex")

label = tkinter.Label(root)

title = tkinter.Label(root, text="Pokedex")
title.pack()

enter_pokemon = tkinter.Entry(root)
enter_pokemon.pack()

button = tkinter.Button(root, text="Get Pokemon", command=get_pokemon)
button.pack()

label = tkinter.Label(root)
type_label = tkinter.Label(root)
base_stats = tkinter.Label(root)
hp_label = tkinter.Label(root)
attack_label = tkinter.Label(root)
defense_label = tkinter.Label(root)
special_attack_label = tkinter.Label(root)
special_defense_label = tkinter.Label(root)
speed_label = tkinter.Label(root)
weight_label = tkinter.Label(root)

root.mainloop()