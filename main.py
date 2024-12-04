import random
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Listbox, END


def generuj_cisla():
    global nahodne_cisla, zoradene_cisla, filtrovat_cisla
    nahodne_cisla = [random.randint(1, 55) for _ in range(45)]
    zoradene_cisla = sorted(nahodne_cisla)
    filtrovat_cisla = [cislo for cislo in zoradene_cisla if cislo <= 30]

    listbox.delete(0, END)  
    for cislo in filtrovat_cisla:
        listbox.insert(END, cislo)  


def zobraz_graf():
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(nahodne_cisla)), nahodne_cisla, color='skyblue')
    plt.title('Hodnoty pred zoradením')
    plt.xlabel('Index')
    plt.ylabel('Hodnoty')
    plt.show()


root = Tk()
root.title("Generovanie čísel a graf")
root.geometry("400x300")


Label(root, text="Čísla menšie alebo rovné 30:", font=("Arial", 12)).pack()


listbox = Listbox(root, font=("Arial", 10), height=10)
listbox.pack()


Button(root, text="Generovať čísla", command=generuj_cisla, font=("Arial", 12)).pack(pady=10)


Button(root, text="Zobraziť graf", command=zobraz_graf, font=("Arial", 12)).pack()


root.mainloop()
