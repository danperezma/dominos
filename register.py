import tkinter as tk
from data import costumers
from sell import sell

def add_user(root, number, data, seller):
    root.destroy()
    costumers[number] = data
    sell(seller)

def register(number, seller):
    register_button_color = '#047CAE'

    root = tk.Tk()
    root.title = 'Dominos Pizza'
    root.geometry('1280x780+80+0')
    root.resizable(width=False, height=False)

    background = tk.PhotoImage(file='backgrounds/register.png')
    background1 = tk.Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)

    name = tk.StringVar()
    surname = tk.StringVar()
    avenue = tk.StringVar()
    exterior = tk.StringVar()
    postal_code = tk.StringVar()
    colony = tk.StringVar()

    # Botones
    button_access = tk.Button(root, text='Registrar', cursor='hand2', bg=register_button_color, width=20,
                              command= lambda : add_user(root, number, {
                                  'name': name.get(),
                                  'surname': surname.get(),
                                  'avenue': avenue.get(),
                                  'exterior' : exterior.get(),
                                  'postal_code': postal_code.get(),
                                  'colony': colony.get(),
                              }, seller), relief='flat', font=('Comic Sans MS', 20))
    # 780, 660
    button_access.place(x=430, y=665)

    # Inputs
    name_input = tk.Entry(root, textvar=name, width=30, relief='flat', font=('Comic Sans MS', 20))
    name_input.place(x=70, y=230)

    surname_input = tk.Entry(root, textvar=surname, width=30, relief='flat', font=('Comic Sans MS', 20))
    surname_input.place(x=70, y=430)

    avenue_input = tk.Entry(root, textvar=avenue, width=30, relief='flat', font=('Comic Sans MS', 20))
    avenue_input.place(x=680, y=155)

    exterior_input = tk.Entry(root, textvar=exterior, width=30, relief='flat', font=('Comic Sans MS', 20))
    exterior_input.place(x=680, y=295)

    postal_code_input = tk.Entry(root, textvar=postal_code, width=30, relief='flat', font=('Comic Sans MS', 20))
    postal_code_input.place(x=680, y=435)

    colony_input = tk.Entry(root, textvar=colony, width=30, relief='flat', font=('Comic Sans MS', 20))
    colony_input.place(x=680, y=545)

    root.mainloop()
