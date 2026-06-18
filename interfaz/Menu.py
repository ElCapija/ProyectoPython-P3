import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from tkinter import Menu as TkMenu
from tkcalendar import DateEntry
from negocio.Cuenta import Cuenta
from negocio.Movimiento import Movimiento

def abrir_menu(numero_cuenta):

    cuenta_actual = numero_cuenta

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
        light_image=Image.open("Imagenes/Imagen_Banco.png"),
        dark_image=Image.open("Imagenes/Imagen_Banco.png"),
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

    # BARRA DE MENÚ
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

    #Deshabilitar opciones hasta seleccionar cajero
    barra_menu.entryconfig("Cuenta", state="disabled")
    barra_menu.entryconfig("Movimientos", state="disabled")
    barra_menu.entryconfig("Pago de Servicios", state="disabled")

    # PANEL DE CONTENIDO
    contenido = ctk.CTkFrame(
        menu_principal,
        fg_color="#F5F5F5",
    )

    contenido.pack(fill="both", expand=True)

    cajero_actual = ""
    cuenta_actual = numero_cuenta

    def limpiar_contenido():
        for widget in contenido.winfo_children():
            widget.destroy()


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

        ctk.CTkLabel(
            contenido,
            text=f"Cajero seleccionado: {cajero_actual}",
            font=("Arial", 18)
        ).pack(pady=10)


    def iniciar_menu(cajero):

        nonlocal cajero_actual
        cajero_actual = cajero

        barra_menu.entryconfig("Cuenta", state="normal")
        barra_menu.entryconfig("Movimientos", state="normal")
        barra_menu.entryconfig("Pago de Servicios", state="normal")

        mostrar_inicio()

    def mostrar_comprobante(mov):

        ventana = ctk.CTkToplevel()

        ventana.title("Comprobante")

        ventana.geometry("400x350")

        texto = f"""
        COMPROBANTE
        Movimiento: {mov.get_id_movimiento()}
        Fecha:
        {mov.get_fecha()}
        Cajero:
        {mov.get_codigo_cajero()}
        Tipo:
        {mov.get_tipo()}
        Servicio:
        {mov.get_servicio()}
        Monto:
        ₡{mov.get_monto()}
        Saldo anterior:
        ₡{mov.get_saldo_anterior()}
        Saldo actual:
        ₡{mov.get_saldo_resultante()}
        """

        ctk.CTkLabel(
            ventana,
            text=texto,
            justify="left",
            font=("Consolas",14)
        ).pack(padx=20, pady=20)

    # SELECCIÓN DE CAJERO
    def seleccionar_cajero():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Seleccione un Cajero",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=40)

        ctk.CTkButton(
            contenido,
            text="Cajero 1",
            width=250,
            command=lambda: iniciar_menu("001")
        ).pack(pady=10)
        ctk.CTkButton(
            contenido,
            text="Cajero 2",
            width=250,
            command=lambda: iniciar_menu("002")
        ).pack(pady=10)

        ctk.CTkButton(
            contenido,
            text="Cajero 3",
            width=250,
            command=lambda: iniciar_menu("003")
        ).pack(pady=10)

    # CONSULTAR SALDO
    def consultar_saldo():

        limpiar_contenido()

        cuenta = Cuenta(cuenta_actual, None)

        exito, saldo = cuenta.consultar_saldo()

        titulo = ctk.CTkLabel(
            contenido,
            text="Consultar Saldo",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        if exito:

            saldo_label = ctk.CTkLabel(
                contenido,
                text=f"Saldo actual: ₡{saldo}",
                font=("Arial", 18)
            )

        else:

            saldo_label = ctk.CTkLabel(
                contenido,
                text=f"Error: {saldo}",
                font=("Arial", 18)
            )

        saldo_label.pack(pady=10)

    # DEPOSITAR
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

        def confirmar_deposito():

            monto_deposito = monto.get()

            if monto_deposito == "":

                messagebox.showerror("Error", "Ingrese un monto")
                return

            cuenta = Cuenta(cuenta_actual, None)
            print(cajero_actual)
            exito, mensaje = cuenta.depositar(
                cajero_actual,
                float(monto_deposito)
            )

            if exito:

                messagebox.showinfo("Éxito", "Depósito realizado correctamente")

            else:

                messagebox.showerror("Error", mensaje)

            exito2, mov = cuenta.ultimo_movimiento()

            if exito2:

                mostrar_comprobante(mov)

        ctk.CTkButton(
            contenido,
            text="Confirmar",
            command=confirmar_deposito
        ).pack(pady=20)

    # RETIRAR
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

        def confirmar_retiro():

            monto_retiro = monto.get()

            if monto_retiro == "":

                messagebox.showerror("Error", "Ingrese un monto")
                return


            cuenta = Cuenta(cuenta_actual, None)

            exito, mensaje = cuenta.retirar(
                cajero_actual,
                float(monto_retiro)
            )


            if exito:

                messagebox.showinfo("Éxito", "Retiro realizado correctamente")

            else:
                messagebox.showerror("Error", mensaje)

        ctk.CTkButton(
            contenido,
            text="Confirmar",
            command=confirmar_retiro
        ).pack(pady=20)

    # HISTORIAL DE MOVIMIENTOS
    def historial():

        limpiar_contenido()

        titulo = ctk.CTkLabel(
            contenido,
            text="Historial de Movimientos",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        ctk.CTkLabel(
            contenido,
            text="Fecha inicio"
        ).pack(pady=5)

        fecha_inicio = DateEntry(
            contenido,
            date_pattern='yyyy-mm-dd'
        )

        fecha_inicio.pack(pady=5)

        ctk.CTkLabel(
            contenido,
            text="Fecha fin"
        ).pack(pady=5)

        fecha_fin = DateEntry(
            contenido,
            date_pattern='yyyy-mm-dd'
        )

        fecha_fin.pack(pady=5)

        frame_resultados = ctk.CTkScrollableFrame(
            contenido,
            width=700,
            height=300
        )

        def buscar_historial():

            inicio = fecha_inicio.get()
            fin = fecha_fin.get()

            cuenta = Cuenta(cuenta_actual, None)

            exito, movimientos = cuenta.historial_movimientos(
                inicio,
                fin
            )

            # Limpia resultados anteriores
            for widget in frame_resultados.winfo_children():

                widget.destroy()

            if exito:

                if len(movimientos) == 0:

                    ctk.CTkLabel(
                        frame_resultados,
                        text="No hay movimientos en ese rango de fechas."
                    ).pack(pady=10)

                    return

                for mov in movimientos:

                    texto = (
                        f"ID: {mov.get_id_movimiento()}\n"
                        f"Cajero: {mov.get_codigo_cajero()}\n"
                        f"Tipo: {mov.get_tipo()}\n"
                        f"Monto: ₡{mov.get_monto()}\n"
                        f"Saldo anterior: ₡{mov.get_saldo_anterior()}\n"
                        f"Saldo resultante: ₡{mov.get_saldo_resultante()}\n"
                        f"Fecha: {mov.get_fecha()}"
                    )

                    tarjeta = ctk.CTkFrame(frame_resultados)

                    tarjeta.pack(
                        fill="x",
                        padx=10,
                        pady=8
                    )


                    ctk.CTkLabel(
                        tarjeta,
                        text=texto,
                        justify="left",
                        anchor="w"
                    ).pack(
                        padx=10,
                        pady=10,
                        anchor="w"
                    )

            else:

                messagebox.showerror(
                    "Error",
                    movimientos
                )

        ctk.CTkButton(
            contenido,
            text="Buscar",
            command=buscar_historial
        ).pack(pady=10)

        frame_resultados.pack(
            pady=20,
            fill="both",
            expand=True
        )

    def pagar_servicio(servicio):

        limpiar_contenido()

        titulo = ctk.CTkLabel(contenido, text=f"Pago de {servicio}", font=("Arial",24,"bold"))
        titulo.pack(pady=20)

        monto = ctk.CTkEntry(contenido, placeholder_text="Monto a pagar", width=250)
        monto.pack(pady=10)

        def confirmar_pago():
            monto_pago = monto.get()
            if monto_pago=="":

                messagebox.showerror("Error","Ingrese un monto")
                return
            cuenta = Cuenta(cuenta_actual, None)
            exito,mensaje = cuenta.pagar_servicio(cajero_actual, servicio, float(monto_pago))
            if exito:
                messagebox.showinfo("Éxito", f"Pago de {servicio} realizado correctamente")
            else:

                messagebox.showerror("Error",mensaje)
        ctk.CTkButton(contenido, text="Confirmar", command=confirmar_pago).pack(pady=20)

    def pago_agua():

        pagar_servicio("Agua")


    def pago_electricidad():

        pagar_servicio("Luz")


    def pago_internet():

        pagar_servicio("Internet")


    def pago_telefono():

        pagar_servicio("Telefono")
        
    # OPCIONES DEL MENÚ
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

    seleccionar_cajero()
    if __name__ == "__main__":
        abrir_menu()