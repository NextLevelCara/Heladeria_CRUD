recipientes = [["r01",0,"cono-chico ",20,2],["r02",0,"cono-medio ",35,2],["r03",0,"cono-grande",40,3],["r04",0,"cuarto-kilo",45,3],["r05",0,"medio-kilo ",80,4],["r06",0,"1-kilo     ",135,4]]
sabores = [["s01",0,"crema-americana"],["s02",0,"dulce-de-leche"],["s03",0,"ddl-granizado"],["s04",0,"tramontana"],["s05",0,"chocolate"],["s06",0,"choco-amargo"],["s07",0,"choco-c-almendras"],["s08",0,"mousse-choco"],["s09",0,"mascarpone"],["s10",0,"frutos-rojos"],["s11",0,"frutilla-c-crema"],["s12",0,"cereza-crema"],["s13",0,"limon"],["s14",0,"sambayon"],["s15",0,"tiramisu"]]
ticket = [] # [ [cantidad, [recipiente], precio total] , [cantidad, [recipiente], precio total] ]
ventas = []
rankRecipientes = []
rankSabores = []

def menuPrincipal():
    menu = """🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦
🍦         CRUD HELADERIA           🍦
🍦 1. Vista ventas                  🍦
🍦 2. Vista administración          🍦
🍦 3. Salir                         🍦
🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦"""
    print(menu)

def opcionEntero():
    opcion = int(input("Ingrese la opcion deseada: "))
    print("")
    return opcion

def opcionSiNo():
    opcion = input("Ingrese la opcion deseada: ").lower()
    print("")
    if opcion == "n":
        return 0
    if opcion == "s":
        return 1

def menuRecipientes():
    menu = """🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨
🍨   RECIPIENTES  DISPONIBLES   🍨
🍨 1. Cono chico.               🍨
🍨 2. Cono mediano.             🍨
🍨 3. Cono grande.              🍨
🍨 4. 1/4 kg.                   🍨
🍨 5. 1/2 kg.                   🍨
🍨 6. 1 kg.                     🍨
🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨"""
    print(menu)

def preguntaCobrarRecipientes():
    pregunta = "Desea cobrar recipientes? (s/n) "
    print(pregunta)

def ingresarCantidadRecipientes(): 
    pregunta = "Cantidad de recipientes a llevar."
    print(pregunta)

def preguntaCobrarOtroRecipiente():
    pregunta = "Desea cobrar otro recipientes? (s/n) "
    print(pregunta)

def calcular_posicion_recipiente(int):
    posicion = int - 1
    return posicion

def agregar_fila_ticket():
    ticket.append([])

def agregar_envase_y_cantidad_ticket(cont,posicion,cantidad):
    ticket[cont].append(cantidad)
    ticket[cont].append(recipientes[posicion])
    precioUnitario = recipientes[posicion][3]
    precioTotal = precioUnitario*cantidad
    ticket[cont].append(precioTotal)

def calcular_total_ticket():
    totalAPagar = 0
    for i in range(len(ticket)):
        totalAPagar = totalAPagar + ticket[i][2]
    return totalAPagar

def imprimir_ticket():
    print("----- Ticket de compra -----")
    for i in range(len(ticket)):
        print("X",ticket[i][0],"   ",ticket[i][1][2],"   $",ticket[i][2])
    print("TOTAL A PAGAR          $",calcular_total_ticket())
    print("----------------------------\n")

def resetear_ticket():
    ticket.clear()

def menuSabores():
    menu = """🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨
🍨                 SABORES DISPONIBLES                🍨
🍨 1. Crema americana           9. Mascarpone         🍨
🍨 2. Dulce de leche           10. Frutos rojos       🍨
🍨 3. Dulce de leche granizado 11. Frutilla con crema 🍨
🍨 4. Tramontana               12. Cereza a la crema  🍨
🍨 5. Chocolate                13. Limon              🍨
🍨 6. Chocolate amargo         14. Sambayón           🍨
🍨 7. Chocolate con almendras  15. Tiramisú           🍨
🍨 8. Mousse de chocolate                             🍨
🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨🍨\n"""
    print(menu)    

def elegir_y_rankear_sabores():
    for i in range(len(ticket)):
        cantidadRecipientes = ticket[i][0]
        cantidadSabores = ticket[i][1][4]
        for z in range(cantidadRecipientes):
            menuSabores()
            print("Ingresar los sabores del recipiente",ticket[i][1][2],"(pueden ser hasta",cantidadSabores,"sabores distintos)")
            for x in range(cantidadSabores):
                saboresElegidos = int(input("Sabor de helado elegido: "))
                sabor = saboresElegidos - 1
                sumador = sabores[sabor][1]
                suma = sumador + 1
                sabores[sabor][1] = suma
            print("")

def rankear_recipientes(posicion,cantidad):
    sumador = recipientes[posicion][1]
    suma = sumador + cantidad
    recipientes[posicion][1] = suma

def elemento_1_recipiente(elem):
    return elem[1]

def ordenar_rank_envases():
    rankRecipientes = sorted(recipientes, key=elemento_1_recipiente, reverse=True)
    return rankRecipientes

def texto_envases_preRank():
    print("RANK Recipientes (de los mas vendidos a los menos vendidos):")
    print("---------------------------------")
    print("Cantidad | ID | Nombre del envase")

def mostrar_rank_envases(lista):
    texto_envases_preRank()
    for i in range(len(lista)):
        print("   ",lista[i][1],"   ",lista[i][0]," ",lista[i][2])
    print("---------------------------------")
    print("")

def ordenar_rank_sabores():
    rankSabores = sorted(sabores, key=elemento_1_recipiente, reverse=True)
    return rankSabores

def texto_sabores_preRank():
    print("RANK Sabores (de los mas vendidos a los menos vendidos):")
    print("---------------------------------")
    print("Cantidad | ID | Nombre del envase")

def mostrar_rank_sabores(lista):
    texto_sabores_preRank()
    for i in range(len(lista)):
        print("   ",lista[i][1],"   ",lista[i][0]," ",lista[i][2])
    print("---------------------------------")
    print("")

def sumar_ventas():
    ventas.append(1)
    return ventas

def condicion_sumar_ventas():
    contenido = len(ticket)
    if contenido >= 1:
        sumar_ventas()

def mostrar_ventas():
    ventasTotales = sum(ventas)
    print("La cantidad total de ventas fue de",ventasTotales,"\n")

def menu_administracion():
    menu = """🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧
🍧       MENU ADMINISTRACIÓN        🍧
🍧 1. Mostrar total de ventas.      🍧
🍧 2. Ranking de envases vendidos.  🍧
🍧 3. Ranking de sabores vendidos.  🍧
🍧 4. Salir                         🍧
🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧🍧"""
    print(menu)

def salir():
    print("🍨 Gracias por utilizar el software 🍨")

def venta_final():
    print("Venta finalizada ~\n")