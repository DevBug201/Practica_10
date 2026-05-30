from clientes import clientes
from utilidades import pedir_numero

pedidos = []


class LineaPedido:
    """Representa una línea de producto dentro de un pedido."""

    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        """Devuelve el importe de esta línea. Lanza ValueError si cantidad es 0."""
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        return self.precio * self.cantidad


class Pedido:
    """Representa un pedido asociado a un cliente."""

    def __init__(self, cliente):
        self.cliente = cliente
        self.lineas = []
        self.estado = "pendiente"

    def agregar_linea(self, linea):
        """Añade una LineaPedido al pedido."""
        self.lineas.append(linea)

    def total_con_descuento(self):
        """Devuelve el total del pedido aplicando descuento."""
        subtotal = calcular_total_lineas(self.lineas)
        descuento = calcular_descuento(subtotal)
        return subtotal - descuento


def calcular_total_lineas(lineas):
    """Suma los subtotales de todas las líneas."""
    return sum(linea.subtotal() for linea in lineas)


def calcular_descuento(subtotal):
    """Devuelve el descuento según el subtotal: 15% si >=200, 10% si >=100."""
    if subtotal >= 200:
        return subtotal * 0.15
    elif subtotal >= 100:
        return subtotal * 0.10
    return 0


def menu_pedidos():
    fin = False
    while not fin:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    for i, c in enumerate(clientes, start=1):
        print(str(i) + ". " + c.nombre)

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    pedido = Pedido(clientes[numero_cliente - 1])
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            pedido.agregar_linea(LineaPedido(producto, precio, cantidad))
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedidos.append(pedido)
    print("Pedido creado")


def ver_pedidos():
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        for i, p in enumerate(pedidos, start=1):
            total = p.total_con_descuento()
            print(
                str(i) + ". Cliente: " + p.cliente.nombre +
                " | Estado: " + p.estado +
                " | Total: " + str(round(total, 2)) + " €"
            )


def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    subtotal = calcular_total_lineas(p.lineas)
    descuento = calcular_descuento(subtotal)
    iva = (subtotal - descuento) * 0.21
    total = subtotal - descuento + iva

    print("Subtotal: " + str(round(subtotal, 2)))
    print("Descuento: " + str(round(descuento, 2)))
    print("IVA: " + str(round(iva, 2)))
    print("TOTAL: " + str(round(total, 2)))
