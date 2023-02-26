import tkinter as tk
from threading import Timer

level = 1
coins = 0
hp = 50
attack = 1
attack_cost = 10
auto_attack = 0
auto_attack_cost = 10

root = tk.Tk()
root.title("CLICKER WARS")
root.geometry("600x800")
#root.iconbitmap("like.ico")
root.resizable(False, False)

M_images = [tk.PhotoImage(file="1.png"),tk.PhotoImage(file="2.png"),tk.PhotoImage(file="3.png"),tk.PhotoImage(file="4.png"),tk.PhotoImage(file="5.png")]

def update():
    lvl_label.config(text=f"LVL: {level}")
    hp_label.config(text=f"HP: {hp}")
    coins_label.config(text=f"COINS: {coins}")
    click_attack_btn.config(text=f"Current Attack = {attack}\nUpgrade Cost = {attack_cost}")
    auto_attack_btn.config(text=f"Current Auto Attack = {auto_attack}\nUpgrade Cost = {auto_attack_cost}")

def death():
    global level
    global hp
    global coins
    coins += 3 * level
    level+=1
    monster_button.config(image=M_images[level - 1])
    hp = 50 * level
    update()

def click():
    global hp
    global level
    global attack
    hp-=attack
    print(hp)
    if hp<=0:
        death()
    update()

def auto_click():
    global hp
    global level
    global auto_attack
    hp-=auto_attack
    print(hp)
    if hp<=0:
        death()
    update()
    Timer(1,auto_click).start()

def attack_upgrade():
    global coins
    global attack
    global attack_cost
    if coins >= attack_cost:
        coins -= attack_cost
        attack += 1
        attack_cost *= 2
    update()

def auto_attack_upgrade():
    global coins
    global auto_attack
    global auto_attack_cost
    if coins >= auto_attack_cost:
        coins -= attack_cost
        auto_attack += 1
        auto_attack_cost *= 2
    update()

title = tk.Label(root, font = ("Arial", 20, "bold"), text="CLICKER WARS", fg="blue")
title.pack()
lvl_label = tk.Label(root, font = ("Arial", 14), text=f"LVL: {level}")
lvl_label.pack()
coins_label = tk.Label(root, font = ("Arial", 14), text=f"COINS: {coins}", fg="gold",bg="black")
coins_label.pack()

monster_button = tk.Button(root, image=M_images[level-1], command=click)
monster_button.pack()

hp_label = tk.Label(root, font = ("Arial", 14), text=f"HP: {hp}", fg="red")
hp_label.pack()

click_attack_btn = tk.Button(root, font = ("Arial", 14, "bold"), text=f"Current Attack = {attack}\nUpgrade Cost = {attack_cost}", command=attack_upgrade)
click_attack_btn.pack()

auto_attack_btn = tk.Button(root, font = ("Arial", 14, "bold"), text=f"Current Auto Attack = {auto_attack}\nUpgrade Cost = {auto_attack_cost}",  command=auto_attack_upgrade)
auto_attack_btn.pack()

auto_click()

root.mainloop()