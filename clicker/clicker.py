import tkinter as tk

level = 1
coins = 0
hp = 50

root = tk.Tk()
root.title("CLICKER WARS")
root.geometry("600x800")
#root.iconbitmap("like.ico")
root.resizable(False, False)

lvl_1 = tk.PhotoImage(file="1.png")
lvl_2 = tk.PhotoImage(file="2.png")
lvl_3 = tk.PhotoImage(file="1.png")
lvl_4 = tk.PhotoImage(file="1.png")
lvl_5 = tk.PhotoImage(file="1.png")

def update():
    lvl_label.config(text=f"LVL: {level}")
    hp_label.config(text=f"HP: {hp}")
    coins_label.config(text=f"COINS: {coins}")

def death():
    global level
    level+=1
    monster_button.config(image=lvl_2)

def click():
    global hp
    global level
    hp-=1
    print(hp)
    if hp<=0:
        death()
    update()

title = tk.Label(root, font = ("Arial", 20, "bold"), text="CLICKER WARS", fg="blue")
title.pack()
lvl_label = tk.Label(root, font = ("Arial", 14), text=f"LVL: {level}")
lvl_label.pack()
coins_label = tk.Label(root, font = ("Arial", 14), text=f"COINS: {coins}", fg="gold",bg="black")
coins_label.pack()

monster_button = tk.Button(root, image=lvl_1, command=click)
monster_button.pack()

hp_label = tk.Label(root, font = ("Arial", 14), text=f"HP: {hp}", fg="red")
hp_label.pack()

root.mainloop()