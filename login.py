import tkinter as tk
from number import number
#Usuarios

passwords = {
    'spena': 'Elizabethspena',
    'user_rs1': 'Cristianuser_rs1',
    'useralsea': 'Nataliauseralsea',
    'vojeda': 'Diegovojeda',
    'vsalamanca': 'Dayanavsalamanca',
    'wsalamanca': 'Wilsonwsalamanca',
    'ydiaz': 'Tatianaydiaz',
    'ylara': 'Andreaylara',
}

def check(root, user, password):
    if user.get() in passwords.keys():
        if passwords[user.get()] == password.get():
            root.destroy()
            number(user.get())
def login():
    login_button_color = '#DE2A39'

    root = tk.Tk()
    root.title = 'Dominos Pizza'
    root.geometry('1280x780+80+0')
    root.resizable(width=False, height=False)

    background = tk.PhotoImage(file ='backgrounds/login.png')
    background1 = tk.Label(root, image = background).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    user = tk.StringVar()
    password = tk.StringVar()

    #Botones
    button_login = tk.Button(root, text = 'Login', cursor = 'hand2', bg = login_button_color, width = 12, command = lambda : check(root, user, password),
                             relief = 'flat', font = ('Comic Sans MS', 20))
    #780, 660
    button_login.place(x = 830, y = 620)

    #Inputs
    user_input = tk.Entry(root, textvar = user, width = 30, relief = 'flat', font = ('Comic Sans MS', 20))
    user_input.place(x = 710, y = 330)

    password_input = tk.Entry(root, textvar = password, width = 30, relief = 'flat', font = ('Comic Sans MS', 20), show = '*')
    password_input.place(x = 710, y = 495)

    root.mainloop()