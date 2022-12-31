import tkinter as tk
from sell import sell
from register import register
from data import costumers, employees

label_color = '#FBFBFB'
name_color = '#FDECEC'

def change(root, number, seller):
    root.destroy()
    if number in costumers.keys():
        sell(seller)
    else:
        register(number, seller)


def number(seller):
    access_button_color = '#047CAE'

    root = tk.Tk()
    root.title = 'Dominos Pizza'
    root.geometry('1280x780+80+0')
    root.resizable(width=False, height=False)

    background = tk.PhotoImage(file='backgrounds/number.png')
    background1 = tk.Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)

    phone_number = tk.StringVar()

    #labels
    total_label = tk.Label(root, text=employees[seller]['total'], bg=label_color, font=('Cominc Sans MS', 22)).place(x=985, y = 95)
    adicionales_label = tk.Label(root, text=employees[seller]['aditionals'], bg=label_color, font=('Cominc Sans MS', 22)).place(x=1130, y=158)
    name_label = tk.Label(root, text = f'Hola {employees[seller]["name"]}!', bg=name_color, font=('Cominc Sans MS', 22)).place(x=80, y=80)

    # Botones
    button_access = tk.Button(root, text='Acceder', cursor='hand2', bg=access_button_color, width=20, command= lambda : change(root, phone_number.get(), seller),
                             relief='flat', font=('Comic Sans MS', 20))
    # 780, 660
    button_access.place(x=450, y=560)

    # Inputs
    number_input = tk.Entry(root, textvar=phone_number, width=30, relief='flat', font=('Comic Sans MS', 20))
    number_input.place(x=380, y=440)


    root.mainloop()