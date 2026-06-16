from tkinter import messagebox
from PIL import Image
from pathlib import Path
import customtkinter as ctk

app = ctk.CTk()
app.geometry("900x500")

# Panel izquierdo
panel_izq = ctk.CTkFrame(
    app,
    fg_color="#8A1E1E"  # Rojo
)
# El método pack() se utiliza para organizar los widgets en el contenedor. En este caso, se indica que el panel izquierdo se coloque en el lado izquierdo del contenedor principal (app) y que ocupe todo el espacio disponible tanto horizontal como verticalmente (fill="both", expand=True).
panel_izq.pack(side="left", fill="both", expand=True)


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

logo_label.place(x= 80, y=150)

# Panel derecho
panel_der = ctk.CTkFrame(
    app,
    fg_color="#FFFFFF"  # Blanco
)
# El método pack() se utiliza para organizar los widgets en el contenedor. En este caso, se indica que el panel derecho se coloque en el lado derecho del contenedor principal (app) y que ocupe todo el espacio disponible tanto horizontal como verticalmente (fill="both", expand=True).
panel_der.pack(side="right", fill="both", expand=True)

# Título en el panel izquierdo
label_izq = ctk.CTkLabel(
    panel_izq,
    text="Bienvenido a al Banco Universitario de Costa Rica",
    font=("Times New Roman", 18, "bold"), # Fuente personalizada, con tamaño y estilo
    text_color="#FFFFFF"  # Blanco
)
# Posiciona el título en el centro del panel izquierdo
label_izq.place(x = 35, y = 150) 

# Panel de login en el panel derecho
panel_login = ctk.CTkFrame(
    panel_der,
    fg_color="#C4C2C2",  # Blanco
    width=400,
    height=250
)
# El método place() se utiliza para posicionar el panel de login en el centro del panel derecho. Se especifica relx=0.5 y rely=0.5 para centrarlo tanto horizontal como verticalmente, y anchor="center" para que el punto de anclaje sea el centro del panel de login.
panel_login.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)
panel_login.pack_propagate(False)

Titulo_login = ctk.CTkLabel(
    panel_login,
    text="Iniciar Sesión",
    font=("Times New Roman", 18, "bold"), # Fuente personalizada, con tamaño y estilo
    text_color="#000000"  # Negro
)
Titulo_login.pack(pady=10)

Num_Cuenta = ctk.CTkEntry(
    panel_login,
    placeholder_text="Número de Cuenta",
    fg_color="#FFFFFF",  # Blanco
    border_color="#81E0FD",
    text_color="#000000",
    width=250,
    height=29,
)
Num_Cuenta.pack(pady=10) #

Contraseña = ctk.CTkEntry(
    panel_login,
    placeholder_text="Contraseña",
    fg_color="#FFFFFF",  # Blanco
    border_color="#81E0FD",
    text_color="#000000",
    show="*",
    width=250,
    height=29,
)
Contraseña.pack(pady=10)

Salir = ctk.CTkButton(
    panel_der,
    text="Salir",
    fg_color="#8A1E1E",  # Rojo
    text_color="#FFFFFF",  # Blanco
    hover_color="#A82323",
    command=app.destroy
)
Salir.pack(
    side="bottom",
    pady=60
)
def iniciar_sesion():
    numero_cuenta = Num_Cuenta.get()
    contraseña = Contraseña.get()

    if not numero_cuenta or not contraseña:
            messagebox.showerror(
            title="Error",
            message="Por favor, ingresa su número de cuenta y contraseña."
        )
    return

Iniciar_Sesion = ctk.CTkButton(
    panel_login,
    text="Iniciar Sesión",
    fg_color="#8A1E1E",  # Rojo
    text_color="#FFFFFF",  # Blanco
    command=iniciar_sesion,
    height= 35
)
Iniciar_Sesion.pack(pady=30)

app.mainloop() # Inicia el bucle principal de la aplicación, lo que permite que la ventana se muestre y responda a eventos.
    

