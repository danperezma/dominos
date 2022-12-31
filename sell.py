import tkinter as tk
from data import employees
#39k pesos mexicanos, adcionales o postres -> + de 20

label_color = '#FBFBFB'

prices = {
    200: 20,
    650: 10,
    1035: 5,
}
total_label_x, total_label_y = (570, 580)

def add(root, item, x, y, total, bg):
    # background1 = tk.Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    item.set(item.get() + 1)
    total.set(total.get() + prices[x])
    tk.Label(root, text = '    ', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = x, y = y)
    tk.Label(root, text = item.get(), bg = label_color, font = ('Cominc Sans MS', 25)).place(x = x, y = y)
    tk.Label(root, text = '                     ', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = total_label_x, y = total_label_y)
    tk.Label(root, text = f'$ {total.get()}', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = total_label_x, y = total_label_y)

def substract(root, item, x, y, total, bg):
    # background1 = tk.Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    if item.get() != 0:
        total.set(total.get() - prices[x])
    item.set(item.get() - 1)
    item.set(max(0, item.get()))
    tk.Label(root, text = '    ', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = x, y = y)
    tk.Label(root, text = item.get(), bg = label_color, font = ('Cominc Sans MS', 25)).place(x = x, y = y)
    tk.Label(root, text = '                    ', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = total_label_x, y = total_label_y)
    tk.Label(root, text = f'$ {total.get()}', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = total_label_x, y = total_label_y)


def finalizar_compra(root, pizzas, postres, adicional, total, seller):
    root.destroy()
    employees[seller]['total'] += total
    employees[seller]['aditionals'] += pizzas + postres + adicional
    from number import number
    number(seller)


def sell(seller):
    finalizar_button_color = '#047CAE'
    operation_button_color = '#DE2A39'

    root = tk.Tk()
    root.title = 'Dominos Pizza'
    root.geometry('1280x780+80+0')
    root.resizable(width=False, height=False)

    background = tk.PhotoImage(file='backgrounds/sell.png')
    background1 = tk.Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)

    pizzas = tk.IntVar()
    postres = tk.IntVar()
    adicional = tk.IntVar()
    total = tk.IntVar()

    # phone_number = tk.StringVar()
    pizza_label_x, pizza_label_y = (200,450)
    postre_label_x, postre_label_y = (650,450)
    adicional_label_x, adicional_label_y = (1035,450)


    pizzas_label = tk.Label(root, text = pizzas.get(), bg = label_color, font = ('Cominc Sans MS', 25)).place(x = pizza_label_x, y = pizza_label_y)
    postre_label = tk.Label(root, text = postres.get(), bg = label_color, font = ('Cominc Sans MS', 25)).place(x = postre_label_x, y = postre_label_y)
    adicional_label = tk.Label(root, text = adicional.get(), bg = label_color, font = ('Cominc Sans MS', 25)).place(x = adicional_label_x, y = adicional_label_y)
    total_label = tk.Label(root, text = f'${total.get()}', bg = label_color, font = ('Cominc Sans MS', 25)).place(x = total_label_x, y = total_label_y)


    pizza_add_x, pizza_add_y = (320, 445)
    postre_add_x, postre_add_y = (725, 435)
    adicional_add_x, adicional_add_y = (1110, 445)

    pizza_sub_x, pizza_sub_y = (55,440)
    postre_sub_x, postre_sub_y = (515,440)
    adicional_sub_x, adicional_sub_y = (905,440)

    # background1 = tk.Label(root, image=background).place(x=0, y=0, relwidth=1, relheight=1)
    # print(label)
    # Botones
    button_add_pizza = tk.Button(root, text = '+', cursor = 'hand2', bg=operation_button_color,width = 5,
                                 command = lambda : add(root, pizzas, pizza_label_x, pizza_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_add_pizza.place(x = pizza_add_x, y = pizza_add_y)

    button_add_postre = tk.Button(root, text = '+', cursor = 'hand2', bg=operation_button_color,width = 5,
                                  command = lambda : add(root, postres, postre_label_x, postre_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_add_postre.place(x = postre_add_x, y = postre_add_y)

    button_add_adicional = tk.Button(root, text = '+', cursor = 'hand2', bg=operation_button_color,width = 5,
                                     command = lambda : add(root, adicional, adicional_label_x, adicional_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_add_adicional.place(x = adicional_add_x, y = adicional_add_y)


    button_sub_pizza = tk.Button(root, text = '-', cursor = 'hand2', bg=operation_button_color,width = 5,
                                 command = lambda : substract(root, pizzas, pizza_label_x, pizza_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_sub_pizza.place(x = pizza_sub_x, y = pizza_sub_y)

    button_sub_postre = tk.Button(root, text = '-', cursor = 'hand2', bg=operation_button_color,width = 5,
                                  command = lambda : substract(root, postres, postre_label_x, postre_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_sub_postre.place(x = postre_sub_x, y = postre_sub_y)

    button_sub_adicional = tk.Button(root, text = '-', cursor = 'hand2', bg=operation_button_color,width = 5,
                                     command = lambda : substract(root, adicional, adicional_label_x, adicional_label_y, total, background), relief = 'flat', font=('Comic Sans MS', 20))
    button_sub_adicional.place(x = adicional_sub_x, y = adicional_sub_y)

    button_comprar = tk.Button(root, text='Finalizar Compra', cursor='hand2', bg=finalizar_button_color, width=20,
                              command=lambda: finalizar_compra(root, pizzas.get(), postres.get(), adicional.get(), total.get(), seller),
                              relief='flat', font=('Comic Sans MS', 20))
    button_comprar.place(x=450, y=680)

    root.mainloop()
