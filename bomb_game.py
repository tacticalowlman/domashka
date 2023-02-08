import tkinter as tk

bomb = 100
score = 0
press_return = True

root = tk.Tk()

root.title("Игра")
root.geometry("600x600+500+400")
root.iconbitmap("icon2.ico")
fuse_label = tk.Label(root, text=f'Fuse: {bomb}', font=('Comic Sans Ms', 14))
fuse_label.pack()

score_label = tk.Label(root, text=f'Score: {score}', font=('Comic Sans Ms', 14))
score_label.pack()
img_1 = tk.PhotoImage(file='bomb1.gif')
img_2 = tk.PhotoImage(file='bomb2.gif')
img_3 = tk.PhotoImage(file='bomb3.gif')
img_4 = tk.PhotoImage(file='bomb4.gif')
bomb_label = tk.Label(image=img_1)
bomb_label.pack()

def click():
	pass

def start():
	pass

click_button = tk.Button(root, text='Нажми меня', bg='black', fg='white',
						 width=15, font=('Comic Sans MS', 14), command=click)
click_button.pack()
root.bind('<Return>', start)

root.mainloop()
