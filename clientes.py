import re

clientes = []


class Cliente:
    """Representa un cliente del sistema."""

    def __init__(self, nombre, email, telefono=""):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def es_valido(self):
        """Devuelve True si el cliente tiene nombre y email válidos."""
        return validar_nombre(self.nombre) and validar_email(self.email)


def validar_nombre(nombre):
    """Devuelve True si el nombre no está vacío."""
    return nombre.strip() != ""


def validar_email(email):
    """Devuelve True si el email tiene formato válido."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def menu_clientes():
    terminar = False
    while not terminar:
        print("\n--- CLIENTES ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            terminar = True
        else:
            print("No existe esa opción")


def crear_cliente():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    cliente = Cliente(nombre, email, telefono)
    if not cliente.es_valido():
        print("Datos incorrectos")
    else:
        clientes.append(cliente)
        print("Cliente añadido")


def listar_clientes():
    print("\nLISTADO DE CLIENTES")
    if len(clientes) == 0:
        print("No hay clientes")
    else:
        for i, c in enumerate(clientes, start=1):
            print(str(i) + ". " + c.nombre + " - " + c.telefono + " - " + c.email)


def buscar_cliente():
    texto = input("Texto a buscar: ")
    encontrado = False
    for c in clientes:
        if texto.lower() in c.nombre.lower() or texto in c.telefono or texto.lower() in c.email.lower():
            print(c.nombre + " - " + c.telefono + " - " + c.email)
            encontrado = True
    if not encontrado:
        print("No se encontraron clientes")