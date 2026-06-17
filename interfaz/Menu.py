import customtkinter as ctk
from PIL import Image
from tkinter import Menu as TkMenu
from tkcalendar import DateEntry

def abrir_menu():

    ctk.set_appearance_mode("light")

    menu_principal = ctk.CTkToplevel()
    menu_principal.geometry("1000x600")
    menu_principal.title("Banco Universitario")

    header = ctk.CTkFrame(
    menu_principal,
    height=90,
    fg_color="#8A1E1E",
)

    header.pack(fill="x")

    logo = ctk.CTkImage(
        light_image=Image.open("../Imagenes/Imagen_Banco.png"),
        dark_image=Image.open("../Imagenes/Imagen_Banco.png"),
        size=(60, 60)
    )

    logo_label = ctk.CTkLabel(
        header,
        image=logo,
        text=""
    )

    logo_label.pack(side="left", padx=15, pady=10)

    titulo_banco = ctk.CTkLabel(
        header,
        text="Banco Universitario de Costa Rica",
        font=("Arial", 24, "bold"),
        text_color="white"
    )

    titulo_banco.pack(side="left", padx=10)

    # ==========================
    # BARRA DE MENÚ
    # ==========================

    barra_menu = TkMenu(menu_principal)

    menu_principal.config(menu=barra_menu)

    # Cuenta
    cuenta_menu = TkMenu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Cuenta", menu=cuenta_menu)

    # Movimientos
    movimientos_menu = TkMenu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Movimientos", menu=movimientos_menu)

    # Pago de servicios
    servicios_menu = TkMenu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Pago de Servicios", menu=servicios_menu)

    # Sistema
    sistema_menu = TkMenu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Sistema", menu=sistema_menu)

    # ==========================
    # PANEL DE CONTENIDO
    # ==========================

    contenido = ctk.CTkFrame(
        menu_principal,
        fg_color="#F5F5F5"
    )

    contenido.pack(fill="both", expand=True)

    def limpiar_contenido():
        for widget in contenido.winfo_children():
            widget.destroy()

    # ==========================
    # PANTALLA INICIO
    # ==========================

    # ==========================
# PANTALLA INICIO
# ==========================

    def mostrar_inicio():

        limpiar_contenido()

    titulo = ctk.CTkLabel(
        contenido,
        text="Bienvenido al Sistema Bancario",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=80)

    subtitulo = ctk.CTkLabel(
        contenido,
        text="Seleccione una opción del menú superior para comenzar.",
        font=("Arial", 18)
    )
    subtitulo.pack()
    # ==========================
    # CONSULTAR SALDO
    # ==========================

    def consultar_saldo():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Consultar Saldo",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        saldo = ctk.CTkLabel(
            contenido,
            text="Saldo actual: ₡0",
            font=("Arial", 18)
        )

        saldo.pack(pady=10)

    # ==========================
    # DEPOSITAR
    # ==========================

    def depositar():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Depósito",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        monto = ctk.CTkEntry(
            contenido,
            placeholder_text="Monto a depositar",
            width=250
        )

        monto.pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Confirmar"
        ).pack(pady=20)

    # ==========================
    # RETIRAR
    # ==========================

    def retirar():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Retiro",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        monto = ctk.CTkEntry(
            contenido,
            placeholder_text="Monto a retirar",
            width=250
        )

        monto.pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Confirmar"
        ).pack(pady=20)

    # ==========================
    # HISTORIAL
    # ==========================

    def historial():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Historial de Movimientos",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

        try:

            ctk.CTkLabel(
                contenido,
                text="Fecha inicio"
            ).pack()

            fecha_inicio = DateEntry(
                contenido,
                width=20,
                date_pattern="dd/mm/yyyy"
            )
            fecha_inicio.pack(pady=10)

            ctk.CTkLabel(
                contenido,
                text="Fecha final"
            ).pack()

            fecha_fin = DateEntry(
                contenido,
                width=20,
                date_pattern="dd/mm/yyyy"
            )
            fecha_fin.pack(pady=10)

            resultado = ctk.CTkTextbox(
                contenido,
                width=700,
                height=250,
                fg_color="white",
                text_color="black",
                border_color="#8A1E1E",
                border_width=2
            )
            resultado.pack(pady=20)

            def buscar():

                fecha1 = fecha_inicio.get()
                fecha2 = fecha_fin.get()

                resultado.delete("1.0", "end")

                resultado.insert(
                    "1.0",
                    f"Buscando movimientos desde {fecha1} hasta {fecha2}\n\n"
                    "Aquí aparecerán los resultados de SQL Server."
                )

                ctk.CTkButton(
                    contenido,
                    text="Buscar",
                    command=buscar,
                    fg_color="#8A1E1E",
                    hover_color="#A82323",
                    text_color="white"
                ).pack(pady=15)

        except Exception as e:

            error = ctk.CTkLabel(
                contenido,
                text=f"Error cargando DateEntry:\n{e}",
                text_color="red"
            )
            error.pack(pady=20)

            print("ERROR DATEENTRY:", e)


    # ==========================
    # PAGO DE AGUA
    # ==========================

    def pago_agua():

        limpiar_contenido()

        ctk.CTkLabel(
            contenido,
            text="Pago de Agua",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Número de abonado",
            width=250
        ).pack(pady=10)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Monto",
            width=250
        ).pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Pagar"
        ).pack(pady=20)

    # ==========================
    # PAGO DE ELECTRICIDAD
    # ==========================

    def pago_electricidad():

        limpiar_contenido()

        ctk.CTkLabel(
            contenido,
            text="Pago de Electricidad",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Número de contrato",
            width=250
        ).pack(pady=10)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Monto",
            width=250
        ).pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Pagar"
        ).pack(pady=20)

    # ==========================
    # PAGO DE INTERNET
    # ==========================

    def pago_internet():

        limpiar_contenido()

        ctk.CTkLabel(
            contenido,
            text="Pago de Internet",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Número de cliente",
            width=250
        ).pack(pady=10)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Monto",
            width=250
        ).pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Pagar"
        ).pack(pady=20)

    # ==========================
    # PAGO DE TELÉFONO
    # ==========================

    def pago_telefono():

        limpiar_contenido()

        ctk.CTkLabel(
            contenido,
            text="Pago de Teléfono",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Número telefónico",
            width=250
        ).pack(pady=10)

        ctk.CTkEntry(
            contenido,
            placeholder_text="Monto",
            width=250
        ).pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Pagar"
        ).pack(pady=20)

    # ==========================
    # OPCIONES DEL MENÚ
    # ==========================

    cuenta_menu.add_command(
        label="Consultar saldo",
        command=consultar_saldo
    )

    movimientos_menu.add_command(
        label="Depositar",
        command=depositar
    )

    movimientos_menu.add_command(
        label="Retirar",
        command=retirar
    )

    movimientos_menu.add_command(
        label="Historial",
        command=historial
    )

    servicios_menu.add_command(
        label="Agua",
        command=pago_agua
    )

    servicios_menu.add_command(
        label="Electricidad",
        command=pago_electricidad
    )

    servicios_menu.add_command(
        label="Internet",
        command=pago_internet
    )

    servicios_menu.add_command(
        label="Teléfono",
        command=pago_telefono
    )

    sistema_menu.add_command(
        label="Salir del sistema",
        command=menu_principal.destroy
    )

    mostrar_inicio()

    if __name__ == "__main__":
        abrir_menu()