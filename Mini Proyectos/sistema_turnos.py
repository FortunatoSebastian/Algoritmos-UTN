# import tkinter as tk
# from tkcalendar import DateEntry

# ventana = tk.Tk()
# ventana.title("Turnos Online")
# ventana.geometry("800x500")
# ventana.configure(bg="#2c6a9f")

# panel = tk.Frame(ventana, bg="white", padx=20, pady=20)
# panel.place(relx=0.5, rely=0.5, anchor="center", width=740, height=380)

# tk.Label(
#     panel,
#     text="ⓘ  Información",
#     font=("Arial", 11, "bold"),
#     bg="white",
#     fg="#2a6496"
# ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

# tk.Label(
#     panel,
#     text="Seleccione el Tipo de Trámite",
#     font=("Arial", 9),
#     bg="white"
# ).grid(row=2, column=0, columnspan=2, sticky="w")

# var_tramite = tk.StringVar()
# var_tramite.set("Libreta Sanitaria") 

# tramites = ["Libreta Sanitaria", "Certificado de Salud", "Habilitación Comercial"]

# op_tramite = tk.OptionMenu(panel, var_tramite, *tramites)

# op_tramite.config(width=35, anchor="w", bg="white")

# op_tramite.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(2, 10))


# tk.Label(
#     panel,
#     text="Tipo de Documento",
#     font=("Arial", 9),
#     bg="white"
# ).grid(row=4, column=0, columnspan=2, sticky="w")

# var_doc = tk.StringVar()
# var_doc.set("DNI")

# op_doc = tk.OptionMenu(panel, var_doc, "DNI", "Pasaporte", "Cédula")
# op_doc.config(width=20, anchor="w", bg="white")
# op_doc.grid(row=5, column=0, sticky="w", pady=(2, 10))

# ventana.mainloop()


# ══════════════════════════════════════════════════════
#  SISTEMA DE TURNOS - Etapa 1: El Formulario
# ══════════════════════════════════════════════════════
#
#  Antes de ejecutar, instalá tkcalendar:
#  pip install tkcalendar
#
# ══════════════════════════════════════════════════════

import tkinter as tk
from tkcalendar import DateEntry   # Para el selector de fecha


# ─────────────────────────────────────────
#  VENTANA PRINCIPAL
# ─────────────────────────────────────────

ventana = tk.Tk()
ventana.title("Turnos Online - Lomas de Zamora")
ventana.geometry("800x500")
ventana.configure(bg="#2a6496")   # Fondo azul como en la imagen


# ─────────────────────────────────────────
#  PANEL BLANCO (Frame principal)
# ─────────────────────────────────────────

# Este Frame es el rectángulo blanco del medio
panel = tk.Frame(ventana, bg="white", padx=20, pady=20)
panel.place(relx=0.5, rely=0.5, anchor="center", width=740, height=380)
# place() nos permite posicionar con coordenadas exactas
# relx=0.5, rely=0.5 → centro de la ventana
# anchor="center" → el punto de referencia es el centro del Frame


# ─────────────────────────────────────────
#  COLUMNA IZQUIERDA
# ─────────────────────────────────────────

# --- Título sección izquierda ---
tk.Label(
    panel,
    text="ⓘ  Información",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#2a6496"
).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

# --- Texto informativo ---
tk.Label(
    panel,
    text=f("Turnos disponibles desde:\n30/03/2026 14:15\nhasta el día:\n01/04/2026 15:00"),
    font=("Arial", 9),
    bg="white",
    fg="#555",
    justify="left"          # El texto de varias líneas se alinea a la izquierda
).grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 15))

# --- Tipo de Trámite ---
tk.Label(
    panel,
    text="Seleccione el Tipo de Trámite",
    font=("Arial", 9),
    bg="white"
).grid(row=2, column=0, columnspan=2, sticky="w")

# StringVar guarda el valor del dropdown
var_tramite = tk.StringVar()
var_tramite.set("Libreta Sanitaria")   # Valor por defecto

tramites = ["Libreta Sanitaria", "Certificado de Salud", "Habilitación Comercial"]

op_tramite = tk.OptionMenu(panel, var_tramite, *tramites)
op_tramite.config(width=35, anchor="w", bg="white")
op_tramite.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(2, 10))

# --- Tipo de Documento ---
tk.Label(
    panel,
    text="Tipo de Documento",
    font=("Arial", 9),
    bg="white"
).grid(row=4, column=0, columnspan=2, sticky="w")

var_doc = tk.StringVar()
var_doc.set("DNI")

op_doc = tk.OptionMenu(panel, var_doc, "DNI", "Pasaporte", "Cédula")
op_doc.config(width=20, anchor="w", bg="white")
op_doc.grid(row=5, column=0, sticky="w", pady=(2, 10))

# --- Apellido y Nombre ---
tk.Label(
    panel,
    text="Apellido(s) y Nombre(s)",
    font=("Arial", 9),
    bg="white"
).grid(row=6, column=0, columnspan=2, sticky="w")

entry_nombre = tk.Entry(panel, width=45, font=("Arial", 10))
entry_nombre.insert(0, "Ej: Strauss Emilia")   # Texto de ejemplo (placeholder)
entry_nombre.config(fg="gray")
entry_nombre.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(2, 5))


# ─────────────────────────────────────────
#  COLUMNA DERECHA
# ─────────────────────────────────────────

# Separador visual entre columnas
tk.Frame(panel, bg="#ddd", width=1).grid(row=0, column=2, rowspan=10, sticky="ns", padx=15)

# --- Título sección derecha ---
tk.Label(
    panel,
    text="📅  Día y Horario",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#2a6496"
).grid(row=0, column=3, columnspan=2, sticky="w", pady=(0, 10))

# --- Selector de fecha ---
fecha = DateEntry(
    panel,
    width=25,
    date_pattern="dd/mm/yyyy",
    font=("Arial", 10),
    background="#2a6496",
    foreground="white"
)
fecha.grid(row=1, column=3, columnspan=2, sticky="w", pady=(0, 10))

# --- Horario ---
tk.Label(
    panel,
    text="Horario",
    font=("Arial", 9),
    bg="white"
).grid(row=2, column=3, columnspan=2, sticky="w")

var_horario = tk.StringVar()
var_horario.set("Seleccioná el horario")

horarios = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]

op_horario = tk.OptionMenu(panel, var_horario, *horarios)
op_horario.config(width=25, anchor="w", bg="white")
op_horario.grid(row=3, column=3, columnspan=2, sticky="w", pady=(2, 10))

# --- Mail ---
tk.Label(
    panel,
    text="Completá tu mail",
    font=("Arial", 9),
    bg="white"
).grid(row=4, column=3, columnspan=2, sticky="w")

entry_mail = tk.Entry(panel, width=35, font=("Arial", 10))
entry_mail.insert(0, "Ej: emiliastrauss@gmail.com")
entry_mail.config(fg="gray")
entry_mail.grid(row=5, column=3, columnspan=2, sticky="ew", pady=(2, 10))

# --- Número de documento ---
tk.Label(
    panel,
    text="Número",
    font=("Arial", 9),
    bg="white"
).grid(row=6, column=3, columnspan=2, sticky="w")

entry_numero = tk.Entry(panel, width=35, font=("Arial", 10))
entry_numero.insert(0, "Ej: 21254897")
entry_numero.config(fg="gray")
entry_numero.grid(row=7, column=3, columnspan=2, sticky="ew", pady=(2, 10))

# --- Teléfono ---
tk.Label(
    panel,
    text="Teléfono de contacto",
    font=("Arial", 9),
    bg="white"
).grid(row=8, column=3, columnspan=2, sticky="w")

entry_tel = tk.Entry(panel, width=35, font=("Arial", 10))
entry_tel.insert(0, "Ej: 1134256723")
entry_tel.config(fg="gray")
entry_tel.grid(row=9, column=3, columnspan=2, sticky="ew", pady=(2, 10))


# ─────────────────────────────────────────
#  BOTONES
# ─────────────────────────────────────────

def volver():
    print("Volver presionado")   # En la Etapa 2 esto va a limpiar el formulario

def confirmar():
    # En la Etapa 2 acá vamos a validar y guardar el turno
    print("Turno confirmado!")
    print("Nombre:", entry_nombre.get())
    print("Trámite:", var_tramite.get())
    print("Fecha:", fecha.get_date())
    print("Horario:", var_horario.get())

# Frame para los botones (así los agrupamos juntos a la derecha)
frame_botones = tk.Frame(panel, bg="white")
frame_botones.grid(row=10, column=3, columnspan=2, sticky="e", pady=(15, 0))

btn_volver = tk.Button(
    frame_botones,
    text="Volver",
    font=("Arial", 10),
    bg="white",
    fg="#2a6496",
    relief="solid",       # Borde visible
    padx=15,
    pady=5,
    cursor="hand2",
    command=volver
)
btn_volver.pack(side="left", padx=5)   # side="left" los pone uno al lado del otro

btn_confirmar = tk.Button(
    frame_botones,
    text="Confirmar Turno",
    font=("Arial", 10),
    bg="#2a6496",
    fg="white",
    relief="flat",
    padx=15,
    pady=5,
    cursor="hand2",
    command=confirmar
)
btn_confirmar.pack(side="left")


# ─────────────────────────────────────────
#  INICIAR
# ─────────────────────────────────────────

ventana.mainloop()
