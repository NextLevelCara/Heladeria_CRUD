import funciones as f
contadorTicket = 0

f.menuPrincipal()
opcion = f.opcionEntero()
while opcion != 3:
    if opcion == 1:
        f.preguntaCobrarRecipientes()
        opc2 = f.opcionSiNo()
        while opc2 == 1:
            f.menuRecipientes()
            opc3 = int(input("Ingrese el recipiente deseado: "))
            f.calcular_posicion_recipiente(opc3)
            posicion = f.calcular_posicion_recipiente(opc3)
            opc4 = int(input("Ingrese la cantidad de recipientes a llevar: "))
            f.rankear_recipientes(posicion,opc4)
            f.agregar_fila_ticket()
            f.agregar_envase_y_cantidad_ticket(contadorTicket,posicion,opc4)
            contadorTicket = contadorTicket + 1
            f.preguntaCobrarOtroRecipiente()
            opc2 = f.opcionSiNo()
        if opc2 == 0:
            contadorTicket = 0
            f.imprimir_ticket()
            f.condicion_sumar_ventas()
            f.elegir_y_rankear_sabores()
            f.resetear_ticket()
        f.venta_final()
    if opcion == 2:
        f.menu_administracion()
        opc5 = f.opcionEntero()
        while opc5 != 4:
            if opc5 == 1:
                f.mostrar_ventas()
            if opc5 == 2:
                rank = f.ordenar_rank_envases()
                f.mostrar_rank_envases(rank)
            if opc5 == 3:
                rank1 = f.ordenar_rank_sabores()
                f.mostrar_rank_sabores(rank1)
            f.menu_administracion()
            opc5 = f.opcionEntero()
    f.menuPrincipal()
    opcion = f.opcionEntero()
f.salir()