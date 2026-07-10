
arreglos = {
    'FLO01': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO02': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO03': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO04': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO05': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO06': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
}

bodega = {
    'FLO01': [15990, 8],
    'FLO02': [29990, 3],
    'FLO03': [9990, 12],
    'FLO04': [24990, 5],
    'FLO05': [19990, 0],
    'FLO06': [22990, 6]
}


def unidades_tipo(tipo_buscado):
    total_unidades = 0
    tipo_buscado = tipo_buscado.lower()
    for codigo, datos in arreglos.items():
        if datos[1].lower() == tipo_buscado:
            total_unidades += bodega[codigo][1]
    print(f"El total de unidades disponibles es: {total_unidades}")


def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos_bodega in bodega.items():
        precio = datos_bodega[0]
        unidades = datos_bodega[1]
        if p_min <= precio <= p_max and unidades > 0:
            nombre_arreglo = arreglos[codigo][0]
            resultados.append(f"{nombre_arreglo}--{codigo}")
            
    if resultados:
        resultados.sort()
        for res in resultados:
            print(res)
    else:
        print("No hay arreglos en ese rango de precios")


def buscar_codigo(codigo):
    return codigo.upper() in [k.upper() for k in bodega.keys()]

def actualizar_precio(codigo, nuevo_price):
    for k in bodega.keys():
        if k.upper() == codigo.upper():
            bodega[k][0] = nuevo_price
            return True
    return False

def validar_texto(texto):
    return texto.strip() != ""

def validar_tamano(tamano):
    return tamano.upper() in ['S', 'M', 'L']

def validar_tarjeta(opcion):
    return opcion.lower() in ['s', 'n']

def validar_precio(num):
    return num > 0

def validar_unidades(num):
    return num >= 0

def agregar_arreglo(codigo, nombre, tipo, color, tamano, incluye_tarjeta, temporada, precio, unidades):
    if buscar_codigo(codigo):
        return False

    cod_upper = codigo.upper()
    arreglos[cod_upper] = [nombre, tipo, color, tamano.upper(), incluye_tarjeta, temporada]
    bodega[cod_upper] = [precio, unidades]
    return True

def eliminar_arreglo(codigo):
    if not buscar_codigo(codigo):
        return False
    
    clave_eliminar = ""
    for k in bodega.keys():
        if k.upper() == codigo.upper():
            clave_eliminar = k
            
    if clave_eliminar != "":
        del arreglos[clave_eliminar]
        del bodega[clave_eliminar]
        return True
    return False

def leer_opcion():
    opcion_valida = False
    opcion = 0
    while not opcion_valida:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    return opcion

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("====================================")

def iniciar_programa():
    ejecutando = True
    while ejecutando:
        mostrar_menu()
        opc = leer_opcion()
        
        if opc == 1:
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo)
            
        elif opc == 2:
            rango_valido = False
            while not rango_valido:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max)
                        rango_valido = True
                    else:
                        print("Debe ingresar valores enteros válidos (mínimo menor o igual al máximo).")
                except ValueError:
                    print("Debe ingresar valores enteros.")
                    
        elif opc == 3:
            continuar_opcion3 = True
            while continuar_opcion3:
                cod = input("Ingrese el código del arreglo: ")
                try:
                    nuevo_p = int(input("Ingrese el nuevo precio: "))
                    if validar_precio(nuevo_p):
                        if actualizar_precio(cod, nuevo_p):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                        
                        resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                        if resp != 's':
                            continuar_opcion3 = False
                    else:
                        print("El precio debe ser un número entero mayor que cero.")
                except ValueError:
                    print("Debe ingresar un valor entero válido para el precio.")
                    
        elif opc == 4:
            print("\n=== Agregar nuevo arreglo ===")
            cod = input("Codigo: ")
            nom = input("Nombre: ")
            tip = input("Tipo: ")
            col = input("Color principal: ")
            tam = input("Tamaño (S/M/L): ")
            tar = input("Incluye tarjeta? s/n: ")
            tem = input("Temporada: ")
            
            try:
                pre = int(input("Precio: "))
                uni = int(input("Unidades en bodega: "))
                
               
                v_cod = (not buscar_codigo(cod)) and validar_texto(cod)
                v_nom = validar_texto(nom)
                v_tip = validar_texto(tip)
                v_col = validar_texto(col)
                v_tam = validar_tamano(tam)
                v_tar = validar_tarjeta(tar)
                v_tem = validar_texto(tem)
                v_pre = validar_precio(pre)
                v_uni = validar_unidades(uni)
                
                if v_cod and v_nom and v_tip and v_col and v_tam and v_tar and v_tem and v_pre and v_uni:
                    tarjeta_bool = True if tar.lower() == 's' else False
                    if agregar_arreglo(cod, nom, tip, col, tam, tarjeta_bool, tem, pre, uni):
                        print("Arreglo agregado")
                    else:
                        print("El codigo ya existe")
                else:
                    print("Error: Uno o más datos no cumplen con las restricciones de validación. Registro rechazado.")
            except ValueError:
                print("Error: El precio y las unidades deben ser números enteros numéricos.")
                
        elif opc == 5:
            print("\n=== Eliminar arreglo ===")
            cod_eliminar = input("Ingrese el codigo del arreglo que desea eliminar: ")
            if eliminar_arreglo(cod_eliminar):
                print("Arreglo eliminado con wxito de ambos diccionarios")
            else:
                print("El codigo no existe")
                
        elif opc == 6:
            print("Programa finalizado")
            ejecutando = False

iniciar_programa()