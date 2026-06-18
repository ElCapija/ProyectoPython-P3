from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from interfaz import Menu
from datos.Conexion import Conexion

# ==========================
# VENTANA PRINCIPAL
# ==========================
app = ctk.CTk()
app.geometry("900x500")
app.title("Banco Universitario")

# PANEL IZQUIERDO
panel_izq = ctk.CTkFrame(
    app,
    fg_color="#8A1E1E"
)
panel_izq.pack(side="left", fill="both", expand=True)

# Logo
logo = ctk.CTkImage(
    light_image=Image.open("Imagenes/Imagen_Banco.png"),
    dark_image=Image.open("Imagenes/Imagen_Banco.png"),
    size=(300, 200)
)
logo_label = ctk.CTkLabel(
    panel_izq,
    image=logo,
    text=""
)
logo_label.place(x=80, y=180)

# Texto de bienvenida
label_izq = ctk.CTkLabel(
    panel_izq,
    text="Bienvenido al Banco Universitario de Costa Rica",
    font=("Times New Roman", 18, "bold"),
    text_color="#FFFFFF"
)

label_izq.place(x=35, y=120)


# PANEL DERECHO
panel_der = ctk.CTkFrame(
    app,
    fg_color="#FFFFFF"
)

panel_der.pack(
    side="right",
    fill="both",
    expand=True
)

# PANEL LOGIN
panel_login = ctk.CTkFrame(
    panel_der,
    fg_color="#C4C2C2",
    width=400,
    height=250,
    corner_radius=15
)

panel_login.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

panel_login.pack_propagate(False)

# TÍTULO LOGIN
Titulo_login = ctk.CTkLabel(
    panel_login,
    text="Iniciar Sesión",
    font=("Times New Roman", 18, "bold"),
    text_color="#000000"
)

Titulo_login.pack(pady=10)

# NÚMERO DE CUENTA
Num_Cuenta = ctk.CTkEntry(
    panel_login,
    placeholder_text="Número de Cuenta",
    fg_color="#FFFFFF",
    border_color="#81E0FD",
    text_color="#000000",
    width=250,
    height=29
)

Num_Cuenta.pack(pady=10)

# CONTRASEÑA
Contraseña = ctk.CTkEntry(
    panel_login,
    placeholder_text="Contraseña",
    fg_color="#FFFFFF",
    border_color="#81E0FD",
    text_color="#000000",
    show="*",
    width=250,
    height=29
)

Contraseña.pack(pady=10)

# FUNCIÓN LOGIN
def iniciar_sesion():

    numero_cuenta = Num_Cuenta.get().strip()
    contraseña = Contraseña.get().strip()

    if not numero_cuenta or not contraseña:
        messagebox.showerror("Error", "Ingrese todos los datos")
        return

    conexiond = Conexion.conectar(
    numero_cuenta,
    contraseña
)
    if conexiond is not None:
        messagebox.showinfo("Éxito", "Inicio de sesión correcto")
        app.withdraw()
        Menu.abrir_menu(numero_cuenta)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# BOTÓN INICIAR SESIÓN
Iniciar_Sesion = ctk.CTkButton(
    panel_login,
    text="Iniciar Sesión",
    fg_color="#8A1E1E",
    text_color="#FFFFFF",
    hover_color="#A82323",
    command=iniciar_sesion,
    height=35
)

Iniciar_Sesion.pack(pady=20)

# BOTÓN SALIR
Salir = ctk.CTkButton(
    panel_der,
    text="Salir",
    fg_color="#8A1E1E",
    text_color="#FFFFFF",
    hover_color="#A82323",
    command=app.destroy
)

Salir.pack(
    side="bottom",
    pady=60
)

# EJECUTAR APP
app.mainloop()