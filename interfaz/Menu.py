from tkinter import Menu
import customtkinter as ctk

app = ctk.CTk()
app.geometry("900x500")

menu_bar = Menu(app)

app.config(menu=menu_bar)

cuenta_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Cuenta", menu=cuenta_menu)

cuenta_menu.add_command(label="Consultar Saldo")
cuenta_menu.add_command(label="Ver Información")

movimientos_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Movimientos", menu=movimientos_menu)

movimientos_menu.add_command(label="Depositar")
movimientos_menu.add_command(label="Retirar")
movimientos_menu.add_command(label="Transferir")

app.mainloop()