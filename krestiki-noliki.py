import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Крестики-нолики')
buttons, buttons_inds = {}, {}
count = 0


def row_win(x):
    if buttons_inds[x*3]['text'] != '' and buttons_inds[x*3]['text'] == buttons_inds[x*3 + 1]['text'] and buttons_inds[x*3 + 1]['text'] == buttons_inds[x*3 + 2]['text']:
        if buttons_inds[x*3]['text'] == 'X':
            messagebox.showinfo("Крестики-нолики", "Крестики выиграли!")
        else:
            messagebox.showinfo("Крестики-нолики", "Нолики выиграли!")
        restart()
        return True


def column_win(x):
    if buttons_inds[x]['text'] != '' and buttons_inds[x]['text'] == buttons_inds[x + 3]['text'] and buttons_inds[x + 3]['text'] == buttons_inds[x + 6]['text']:
        if buttons_inds[x]['text'] == 'X':
            messagebox.showinfo("Крестики-нолики", "Крестики выиграли!")
        else:
            messagebox.showinfo("Крестики-нолики", "Нолики выиграли!")
        restart()
        return True


def diagonal_win():
    if buttons_inds[0]['text'] != '' and buttons_inds[0]['text'] == buttons_inds[4]['text'] and buttons_inds[4]['text'] == buttons_inds[8]['text']:
        if buttons_inds[0]['text'] == 'X':
            messagebox.showinfo("Крестики-нолики", "Крестики выиграли!")
        else:
            messagebox.showinfo("Крестики-нолики", "Нолики выиграли!")
        restart()
        return True
    if buttons_inds[2]['text'] != '' and buttons_inds[2]['text'] == buttons_inds[4]['text'] and buttons_inds[4]['text'] == buttons_inds[6]['text']:
        if buttons_inds[2]['text'] == 'X':
            messagebox.showinfo("Крестики-нолики", "Крестики выиграли!")
        else:
            messagebox.showinfo("Крестики-нолики", "Нолики выиграли!")
        restart()
        return True


def draw():
    ct = 0
    for i in range(9):
        if buttons_inds[i]['text'] != '':
            ct += 1
    if ct == 9:
        return True
    else:
        return False


def check_win():
    for i in range(3):
        if row_win(i):
            return
        if column_win(i):
            return
    if diagonal_win():
        return
    if draw():
        messagebox.showinfo("Крестики-нолики", "Ничья!")
        restart()
        return


def button_pressed(button):
    global count
    if button['text'] == '':
        if count % 2 == 0:
            button['text'] = 'X'
        else:
            button['text'] = 'O'
        count += 1
    check_win()


def restart():
    global buttons, buttons_inds
    global count
    count = 0
    for i in range(9):
        box = tk.Button(height=3, width=6, text='')
        buttons_inds[i] = box
        buttons[id(box)] = box
        box['command'] = lambda x=id(box): button_pressed(buttons[x])
        box.grid(row=i // 3, column=i % 3)


restart()
root.mainloop()
