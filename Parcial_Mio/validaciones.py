

# ● Si se alcanza el límite de 50 proyectos activos, se deberá notificar al usuario.

def contar_proyectos_activos(lista: list):
    contador = 0

    for i in range(len(lista)):

        if(lista[i]["Estado"] == "Activo"):
            contador +=1
            if(contador <= 50):
                print("Hay 50 proyectos activos, elimina alguno para continuar.")
                break

# 1
# Validaciones:
# ● Nombre del Proyecto: Debe contener solo caracteres alfabéticos y no pueden contener números ni caracteres especiales.

def validar_ingreso_letras(nombre_proyecto):
    retorno = True
    
    for i in range(len(nombre_proyecto)):
        if(nombre_proyecto[i].isalpha() == False):
            retorno = False
            break

    return retorno

# ● Descripción: Debe ser un texto alfanumérico de no más de 200 caracteres.

def validar_ingreso_alfanumerico(descripcion_proyecto):
    retorno = True
    
    for i in range(len(descripcion_proyecto)):
        if(descripcion_proyecto[i].isalnum() == False):
            retorno = False
            break

    return retorno

# ● Presupuesto: Debe ser un valor numérico entero no menor a $500000.

def validar_ingreso_entero(presupuesto : int):
    retorno = True

    for i in range(len(presupuesto)):
        if(presupuesto[i].isdigit() == False):
            retorno = False
            break

    return retorno


# ● Fecha de Inicio y Fecha de Fin: Deben ser fechas válidas en el formato "DD/MM/AAAA".

def validar_el_formato_de_las_fechas(fecha):
    retorno = True

    partes_fechas = fecha.split("/")
    if(len(partes_fechas) != 3):
        retorno = False

    elif(partes_fechas[0].isdigit() == False or partes_fechas[1].isdigit() == False or partes_fechas[2].isdigit() == False):
        retorno = False

    elif(len(partes_fechas[0]) != 2 or len(partes_fechas[1]) != 2 or len(partes_fechas[2]) != 4):
        retorno = False

    return retorno

def validar_formato_fecha(fecha):
    contador = 0
    retorno = False

    for i in range(len(fecha)):
        if(fecha[i] == "/"):
            contador += 1

    if(contador == 2 and validar_el_formato_de_las_fechas(fecha) == True): 
        retorno = True

    return retorno  
        
# ● El estado debe de iniciar como ‘Activo’, pudiendo ser también ‘Cancelado’ o ‘Finalizado’

def comprobar_estado_del_proyecto(estado):
    retorno = True

    if(estado != "Activo" and estado != "Cancelado" and estado != "Finalizado"):
        retorno = False
        
    return retorno