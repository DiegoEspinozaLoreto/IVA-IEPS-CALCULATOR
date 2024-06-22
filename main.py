import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x700")
root.title("Lordy IVA y IEPS")

item_data_dict = {}
item_id = 0

# Diccionario para almacenar los frames de cada fila
rows_widgets = {}

def is_valid_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def eliminar(widget,id):
    widget.destroy()
    del item_data_dict[id]



def agregar(precio, hasIva, hasIeps):
    global item_id
    this_frame_id = item_id
    iva = 0
    ieps = 0
    if hasIva:
        iva = precio * 0.16
    if hasIeps:
        ieps = precio * 0.08

    item_data_dict[item_id] = [precio,iva,ieps]
    item_id += 1

    new_item_frame = customtkinter.CTkFrame(master=resultados_scroll)
    new_item_frame.grid_columnconfigure(0, weight=1, minsize=100)  # Precio
    new_item_frame.grid_columnconfigure(1, weight=1, minsize=100)  # IVA
    new_item_frame.grid_columnconfigure(2, weight=1, minsize=100)  # IEPS
    new_item_frame.grid_columnconfigure(3, weight=1, minsize=160)  # Botón Eliminar

    precio_label = customtkinter.CTkLabel(master=new_item_frame, text=f"${precio:.2f}")
    precio_label.grid(row=0, column=0, padx=10, pady=12, sticky="ew")

    iva_label = customtkinter.CTkLabel(master=new_item_frame, text=f"${iva:.2f}")
    iva_label.grid(row=0, column=1, padx=10, pady=12, sticky="ew")

    ieps_label = customtkinter.CTkLabel(master=new_item_frame, text=f"${ieps:.2f}")
    ieps_label.grid(row=0, column=2, padx=10, pady=12, sticky="ew")

    eliminar_button = customtkinter.CTkButton(master=new_item_frame, text="Eliminar", fg_color="red", width=120,
                                              command=lambda widget=new_item_frame, id = this_frame_id: eliminar(widget,id))
    eliminar_button.grid(row=0, column=3, padx=10, pady=12, sticky="ew")

    new_item_frame.pack(padx=10, pady=12)

    print(item_data_dict)


def totalizar():
    global item_data_dict
    precio_total = 0
    iva_total = 0
    ieps_total =0
    if len(item_data_dict)>0:
        for item in item_data_dict:
            this_data = item_data_dict[item]
            precio_total += this_data[0]
            iva_total += this_data[1]
            ieps_total += this_data[2]

    preciototal_label.configure(text=f"${precio_total:.2f}")

    ivatotal_label.configure(text=f"${iva_total:.2f}")

    iepstotal_label.configure(text=f"${ieps_total:.2f}")




def validar_y_agregar():
    precio_texto = priceEntry.get().strip()
    if precio_texto:
        if is_valid_number(precio_texto) and float(precio_texto) < 10000000 and float(precio_texto) > 0:
             agregar(float(precio_texto), checkbox_iva.get(), checkbox_ieps.get())
        else:
            error_label.configure(text="El precio ingresado no es válido.")
    else:
        error_label.configure(text="El campo de precio está vacío.")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill="both", expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

label = customtkinter.CTkLabel(master=frame, text="IVA y IEPS", font=("Roboto", 24))
label.grid(row=0, column=0, columnspan=4, padx=10, pady=12, sticky="nsew")

priceEntry = customtkinter.CTkEntry(master=frame, placeholder_text="Precio", validate="key")
priceEntry.grid(row=1, column=0, padx=10, pady=12)

checkbox_iva = customtkinter.CTkCheckBox(master=frame, text="IVA")
checkbox_iva.grid(row=1, column=1, padx=10, pady=12)

checkbox_ieps = customtkinter.CTkCheckBox(master=frame, text="IEPS")
checkbox_ieps.grid(row=1, column=2, padx=10, pady=12)

agregar_button = customtkinter.CTkButton(master=frame, text="Agregar", width=100, command=validar_y_agregar)
agregar_button.grid(row=1, column=3, padx=10, pady=12)

resultados_scroll = customtkinter.CTkScrollableFrame(master=frame, width=450, height=300)
resultados_scroll.grid(row=3, column=0, columnspan=4, padx=10, pady=12, sticky="nsew")


# Crear encabezados de la tabla
encabezado_frame = customtkinter.CTkFrame(master=resultados_scroll)
encabezado_frame.pack(padx=10, pady=12)

# Configurar columnas en encabezado_frame
encabezado_frame.grid_columnconfigure(0, weight=1, minsize=100)
encabezado_frame.grid_columnconfigure(1, weight=1, minsize=100)
encabezado_frame.grid_columnconfigure(2, weight=1, minsize=100)
encabezado_frame.grid_columnconfigure(3, weight=1, minsize=160)

precio_encabezado = customtkinter.CTkLabel(master=encabezado_frame, text="Precio")
precio_encabezado.grid(row=0, column=0, padx=10, pady=12, sticky="ew")

iva_encabezado = customtkinter.CTkLabel(master=encabezado_frame, text="IVA")
iva_encabezado.grid(row=0, column=1, padx=10, pady=12, sticky="ew")

ieps_encabezado = customtkinter.CTkLabel(master=encabezado_frame, text="IEPS")
ieps_encabezado.grid(row=0, column=2, padx=10, pady=12, sticky="ew")



# Crear encabezados de la totaizar
totalizar_frame = customtkinter.CTkFrame(master=frame,width=550, height=50)
totalizar_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=12)

totalizar_button = customtkinter.CTkButton(master=totalizar_frame, text="Totalizar", width=200, command=totalizar)
totalizar_button.grid(row=0, column=3, columnspan=4, padx=10, pady=12, sticky="nsew")

# Configurar columnas en encabezado_frame
totalizar_frame.grid_columnconfigure(0, weight=1, minsize=100)
totalizar_frame.grid_columnconfigure(1, weight=1, minsize=100)
totalizar_frame.grid_columnconfigure(2, weight=1, minsize=100)
totalizar_frame.grid_columnconfigure(3, weight=1, minsize=160)

precio_encabezado = customtkinter.CTkLabel(master=totalizar_frame, text="Precio total")
precio_encabezado.grid(row=0, column=0, padx=10, pady=12, sticky="ew")

iva_encabezado = customtkinter.CTkLabel(master=totalizar_frame, text="IVA total")
iva_encabezado.grid(row=0, column=1, padx=10, pady=12, sticky="ew")

ieps_encabezado = customtkinter.CTkLabel(master=totalizar_frame, text="IEPS total")
ieps_encabezado.grid(row=0, column=2, padx=10, pady=12, sticky="ew")

preciototal_label = customtkinter.CTkLabel(master=totalizar_frame, text=f"${0:.2f}")
preciototal_label.grid(row=6, column=0, padx=10, pady=12, sticky="ew")

ivatotal_label = customtkinter.CTkLabel(master=totalizar_frame, text=f"${0:.2f}")
ivatotal_label.grid(row=6, column=1, padx=10, pady=12, sticky="ew")

iepstotal_label = customtkinter.CTkLabel(master=totalizar_frame, text=f"${0:.2f}")
iepstotal_label.grid(row=6, column=2, padx=10, pady=12, sticky="ew")


error_frame = customtkinter.CTkFrame(master=frame, height=50)
error_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=12, sticky="ew")

# Configurar el contenido del error_frame
error_label = customtkinter.CTkLabel(master=error_frame, text="")
error_label.grid(row=0, column=0, padx=10, pady=12, sticky="ew")
error_label.configure(wraplength=450)

root.mainloop()
