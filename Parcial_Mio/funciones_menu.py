import csv, os, json
from datetime import * 
from validaciones import * 
numero_reporte = 1

# 1. Al iniciar el programa, se deberá leer el archivo Proyectos.csv para tener la lista de proyectos
# actualizada.

archivo_csv = "Parcial_Mio\Proyectos.csv" 

def leer_archivo_csv(ruta_archivo):
    lista_proyectos = []

    with open(archivo_csv, 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            lista_proyectos.append(fila)

    return lista_proyectos

def ingresar_nuevo_proyecto_al_csv(nuevo_proyecto):
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")

    datos.append(nuevo_proyecto)

    with open("Parcial_Mio\Proyectos.csv", mode="w", newline="", encoding="utf-8") as archivo:
  
        escritor_csv = csv.DictWriter(archivo, fieldnames = datos[0].keys())
        escritor_csv.writeheader()
        escritor_csv.writerows(datos)

def menu():
    lista = leer_archivo_csv(archivo_csv)
    while(True):
        print(
            "Menu Parcial\n1.Ingresar Proyecto"
                "\n2.Modificar Proyecto"
                "\n3.Cancelar Proyecto"
                "\n4.Cambiar estado de los proyectos finalizados"
                "\n5.Mostrar todos los proyectos"
                "\n6.Calcular presupuesto promedio"
                "\n7.Buscar Proyecto por nombre"
                "\n8.Ordenar Proyecto"
                "\n9.Retomar Proyecto"
                "\n10.Ingresar presupuesto y generar reporte de los mayores al ingresado."
                "\n11.Ingresar el nombre de un proyecto y generar un reporte"
                "\n12.Salir"
                "\n13.Calcular el/los proyectos activos con mayor presupuesto iniciados en invierno"
                "\n14.Mostrar el promedio de presupuesto de todos los proyectos finalizados que hayan durado más de 2 años"
                )
        opcion = int(input("Su opcion: "))
        if opcion == 1:
            ingresar_nuevo_proyecto_al_csv(ingresar_proyecto())
            print("El proyecto ha sido ingresado con exito.")
        elif opcion == 2:
            if(modificar_proyecto() == True):
                print("Se ha modificado el proyecto.")
            else:
                print("Reingrese un Id valido de la lista para modificar.")
        elif opcion == 3:
            if(cancelar_proyecto(lista) == True):
                    print("Se cambio el estado del proyecto a cancelado correctamente!\n")
            else:
                print("Reingrese un Id valido para cancelar")
        elif opcion == 4:
            if(comprobar_proyecto(lista) == True):
                    print("Se cambio el estado de los proyectos que finalizaron.")
            else:
                print("Ya estaba Finalizado")
            
        elif opcion == 5:
            datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")
            mostrar_proyectos(datos)
        elif opcion == 6:
            print(calcular_presupuesto_promedio(lista))
        elif opcion == 7:
            mostrar_proyectos(lista) 
            print(buscar_proyecto_por_nombre())
            print("\n")
        elif opcion == 8:
            opcion = imprimir_sub_menu_para_ordenar_mostrar()
            while(opcion != 10):
                match(opcion):
                    case "1":                     
                        print("LISTA ORDENADA POR NOMBRE DE MANERA ASCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_nombre(datos,True))
                            
                    case "2":
                        print("LISTA ORDENADA POR NOMBRE DE MANERA DESCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_nombre(datos,False))
                                                           
                    case "3":
                        print("LISTA ORDENADA POR PRESUPUESTO DE MANERA ASCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_presupuesto(datos,True))                       
                            
                    case "4":
                        print("LISTA ORDENADA POR PRESUPUESTO DE MANERA DESCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_presupuesto(datos,False))
                                                      
                    case "5":
                        print("LISTA ORDENADA POR FECHA DE INICIO DE MANERA ASCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_fecha_de_inicio(datos,True))
                          
                    case "6":
                        print("LISTA ORDENADA POR FECHA DE INICIO DE MANERA DESCENDENTE\n")
                        datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv") 
                        mostrar_proyectos(ordenar_proyectos_por_fecha_de_inicio(datos,False))                        
                            
                    case "7":
                        print("Saliendo del menu de ordenar...\n")
                        break                                  
                    case _:
                            print("Ingrese una opcion valida del 1 al 7\n")
                opcion = imprimir_sub_menu_para_ordenar_mostrar()
        elif opcion == 9:
            dar_de_alta_proyecto()
        elif opcion == 10:
            presupuesto_minimo = input("Ingrese el presupuesto mínimo para filtrar proyectos: ")
            while(validar_ingreso_entero(presupuesto_minimo) == False):
                presupuesto_minimo = input("Reingrese el presupuesto mínimo para filtrar proyectos: ")

            presupuesto_minimo = float(presupuesto_minimo)
            presupuestos_mayores_encontrados = encontrar_presupuestos_mayor(presupuesto_minimo)

            generar_reporte_por_presupuesto(presupuestos_mayores_encontrados,"cantidad_reportes_presupuestos.txt")
            print("Se genero el reporte de los presupuestos.\n")
        elif opcion == 11:
            datos = leer_archivo_csv("Proyectos.csv")
            mostrar_proyectos(datos)
            nombre_proyecto = input("Ingrese el nombre del proyecto a encontrar para reportar: ").strip().lower()
            nombres_proyectos_encontrados = encontrar_proyecto_por_nombre(nombre_proyecto)
            generar_reporte_por_nombre(nombres_proyectos_encontrados,"cantidad_reportes_nombre.txt")
            print("Se genero el reporte de los nombres.\n")
        elif opcion == 12:
            if(escribir_json_finalizados() == True):
                print("Se guardo los proyectos ya finalizados en el Json.\n")
            else:
                print("No hay proyectos que guardar en este momento")
            print("Saliendo...")
        elif opcion == 13:
            proyectos_activos_con_mayor_presupuesto_invierno(lista)
        elif opcion == 14:
            promedio_presupuesto_proyectos_finalizados_duracion_mayor_2_anios(lista)
            break
        else:
            print("Opcion invalida ingrese números entre 1-14")

def imprimir_sub_menu_para_ordenar_mostrar():
    opcion = input("\nINGRESE UNA OPCION DEL MENU ORDENAR\n"
            "1.Por nombre (Ascendente): \n"
            "2.Por nombre (Descendente): \n"
            "3.Por presupuesto (Ascendente): \n"
            "4.Por presupuesto (Descendente): \n"
            "5.Por fecha de inicio (Ascendente): \n"
            "6.Por fecha de inicio (Descendente): \n"
            "7.Salir\n")
    
    return opcion
    
def modificar_dato(id, clave, nuevo_dato):
    datos = leer_archivo_csv("Parcial_Mio/Proyectos.csv")

    for i in datos:
        if(i["Id"] == id):
            i[clave] = nuevo_dato
    with open("Parcial_Mio/Proyectos.csv", mode="w", newline="", encoding="utf-8") as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=datos[0].keys())
        escritor_csv.writeheader()
        escritor_csv.writerows(datos)

# 1. Ingresar proyecto: Pedirá los datos necesarios y dará de alta a un nuevo proyecto, asignando
# un ID autoincremental.

def ingresar_proyecto():
    
    bandera_presupuesto = False
    bandera_fecha = False
    archivo_a_leer = leer_archivo_csv(archivo_csv)
    
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    while validar_ingreso_letras(nombre_proyecto) == False:
        nombre_proyecto = input("Reingrese un nombre correcto: ")
    
    descripcion_proyecto = input("Ingrese la descripcion del proyecto: ")
    while(validar_ingreso_alfanumerico(descripcion_proyecto) == False or len(descripcion_proyecto) <= 6 or len(descripcion_proyecto) > 200):   
        descripcion_proyecto = input("Reingrese una descripcion valida, mayor a 6 caracteres y menor a 200.: ")

    while (bandera_presupuesto == False):
        
        presupuesto_proyecto = input("Ingrese un presupuesto del proyecto: ")
        while validar_ingreso_entero(presupuesto_proyecto) == False:
            presupuesto_proyecto = input("Reingrese un presupuesto correcto que sea del tipo numerico: ")
    
        presupuesto_proyecto = int(presupuesto_proyecto)
        
        while presupuesto_proyecto < 500000:
            presupuesto_proyecto = input("Reingrese un presupuesto mayor que 500.000$: ")
            
            while validar_ingreso_entero(presupuesto_proyecto) == False:
                presupuesto_proyecto = input("Reingrese un presupuesto correcto que sea del tipo numerico: ")
            
            presupuesto_proyecto = int(presupuesto_proyecto)
            
        bandera_presupuesto = True
                
    while(bandera_fecha == False):
        fecha_inicio = input("Ingrese fecha de inicio del proyecto: ")
        while(validar_formato_fecha(fecha_inicio) == False):
            fecha_inicio = input("Reingrese una fecha de inicio valida en formato (DD/MM/AAAA): ")
            
        fecha_fin = input("Ingrese fecha de fin del proyecto: ")
        while(validar_formato_fecha(fecha_fin) == False):
            fecha_fin = input("Reingrese una fecha de fin valida en formato (DD/MM/AAAA): ")

        while(fecha_inicio >= fecha_fin):
            fecha_fin = input("Reingrese la fecha de fin del proyecto mayor a la de inicio: ")
            while(validar_formato_fecha(fecha_fin) == False):
                fecha_fin = input("Reingrese una fecha de fin valida en formato (DD/MM/AAAA): ")
                
        bandera_fecha = True

    estado_proyecto = input("Ingrese el estado del proyecto: ").capitalize()
    while (comprobar_estado_del_proyecto(estado_proyecto)) == False:
        estado_proyecto = input("Reingrese un estado correcto: ").capitalize()
        
    ultimo_id = int(archivo_a_leer[-1]["Id"]) 

    nuevo_proyecto = {"Id":ultimo_id + 1,"Nombre del proyecto":nombre_proyecto,"Descripcion":descripcion_proyecto,
                    "Presupuesto":presupuesto_proyecto,"Fecha de inicio":fecha_inicio,"Fecha de fin":fecha_fin,
                    "Estado":estado_proyecto}

    return nuevo_proyecto
        
# 2. Modificar proyecto: Permitirá alterar cualquier dato del proyecto excepto su ID. Se usará el ID
# para identificar al proyecto a modificar. Se mostrará un submenú para seleccionar qué datos
# modificar. Se indicará si se realizaron modificaciones o no.

def imprimir_sub_menu_de_modificar_proyecto():
    opcion = input("\nINGRESE UNA OPCION DEL MENU\n"
            "1.Nombre del Proyecto: \n"
            "2.Descripción: \n"
            "3.Presupuesto: \n"
            "4.Fecha de Inicio: \n"
            "5.Fecha de Fin: \n"
            "6.Estado: \n"
            "7.Salir\n")
    
    return opcion
    
def modificar_proyecto():
    retorno = False
    bandera_presupuesto = False
    datos = leer_archivo_csv("Proyectos.csv")
    mostrar_proyectos(datos)
    Id = input("Ingrese el ID que desea modificar: ")

    for i in range(len(datos)):
        if(datos[i]["Id"] == Id):
            retorno = True
            opcion = imprimir_sub_menu_de_modificar_proyecto()

            while(opcion != 10):
                match(opcion):
                    case "1":
                        nuevo_nombre = input("Ingrese el nuevo nombre del proyecto a modificar: ")
                        while(validar_ingreso_letras(nuevo_nombre) == False or len(nuevo_nombre) > 30):  
                            nuevo_nombre = input("Reingrese un nombre valido, menor o igual a 30 caracteres: ")

                        modificar_dato(Id,"Nombre del proyecto",nuevo_nombre)
                        print("Se modifico correctamente el nombre del proyecto")      

                    case "2":
                        nueva_descripcion = input("Ingrese una nueva descripcion para el proyecto a modificar: ")
                        while(validar_ingreso_alfanumerico(nueva_descripcion) == False or len(nueva_descripcion) < 5 or len(nueva_descripcion) > 200):               
                            nueva_descripcion = input("Reingrese una descripcion valida, mayor a 6 caracteres y menor a 200: ")
            
                        modificar_dato(Id,"Descripcion",nueva_descripcion)
                        print("Se modifico correctamente la descripcion del proyecto")

                    case "3":
                        while(bandera_presupuesto == False):
                                
                            nuevo_presupuesto = input("Ingrese el nuevo presupuesto para el proyecto a modificar: ")
                            while(validar_ingreso_entero(nuevo_presupuesto) == False):
                                nuevo_presupuesto = input("Reingrese un presupuesto valido que sea del tipo numerico: ")

                            nuevo_presupuesto = float(nuevo_presupuesto)

                            while(nuevo_presupuesto < 500000):
                                nuevo_presupuesto = input("Reingrese un presupuesto valido, mayor a $500000: ")

                                while(validar_ingreso_entero(nuevo_presupuesto) == False):
                                    nuevo_presupuesto = input("Reingrese un presupuesto valido que sea del tipo numerico: ")

                                nuevo_presupuesto = float(nuevo_presupuesto)

                            bandera_presupuesto = True

                        modificar_dato(Id,"Presupuesto",nuevo_presupuesto)
                        print("Se modifico correctamente el presupuesto del proyecto")

                    case "4":
                        nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio para el proyecto a modificar: ")
                        while(validar_formato_fecha(nueva_fecha_inicio) == False):
                            nueva_fecha_inicio = input("Reingrese una fecha de inicio valida (DD/MM/AAAA): ")

                        modificar_dato(Id,"Fecha de inicio",nueva_fecha_inicio)  
                        print("Se modifico correctamente la fecha de inicio del proyecto!!")     

                    case "5":
                        nueva_fecha_fin = input("Ingrese la nueva fecha de fin para el proyecto a modificar: ")
                        while(validar_formato_fecha(nueva_fecha_fin) == False):
                            nueva_fecha_fin = input("Reingrese una fecha de fin valida (DD/MM/AAAA): ")

                        for i in range(len(datos)):
                            if(Id == datos[i]["Id"]):
                                fecha_inicio = datetime.datetime.strptime(datos[i]["Fecha de inicio"],"%d/%m/%Y").date()                        
                                print(fecha_inicio)  

                                while(validar_formato_fecha(nueva_fecha_fin) == False):
                                        nueva_fecha_fin = input("Reingrese una fecha de fin del valida (DD/MM/AAAA): ")   
                                fecha_final = datetime.datetime.strptime(nueva_fecha_fin,"%d/%m/%Y").date()   

                                while(fecha_inicio >= fecha_final):                 
                                    nueva_fecha_fin = input("Reingrese fecha de fin del proyecto mayor a la de inicio: ")

                                    while(validar_formato_fecha(nueva_fecha_fin) == False):
                                        nueva_fecha_fin = input("Reingrese una fecha de fin del valida (DD/MM/AAAA): ")   
                                    break
                        modificar_dato(Id,"Fecha de fin",nueva_fecha_fin)  
                        print("Se modifico correctamente la fecha de fin del proyecto")

                    case "6":
                        nuevo_estado_proyecto = input("Ingrese el estado del proyecto: ").capitalize()
                        while(comprobar_estado_del_proyecto(nuevo_estado_proyecto) == False):
                            nuevo_estado_proyecto = input("Reingrese un estado valido (Activo,Cancelado,Finalizado):").capitalize()

                        modificar_dato(Id,"Estado",nuevo_estado_proyecto)
                        print("Se modifico correctamente el estado del proyecto")     
                        
                    case "7": 
                            print("Saliendo del menu modificar...\n")
                            break
                    case _:
                        print("Reingrese una opcion valida del 1 al 7")
                
                opcion = imprimir_sub_menu_de_modificar_proyecto()

    return retorno

# 3. Cancelar proyecto: Cancelará un proyecto de la lista original. Se pedirá el ID del proyecto a
# cancelar.

def cancelar_proyecto(lista_proyectos):
    retorno = False
    id = input("Ingrese el id del proyecto a cancelar: ")
    if not lista_proyectos:
        retorno = False
    else:
        for i in range(len(lista_proyectos)):
            if(lista_proyectos[i]["Id"] == id):
                lista_proyectos[i]["Estado"] = "Cancelado"
                print(lista_proyectos[i])
                retorno = True
                break
            else:
                retorno = "No hay ningun proyecto con ese id"
    return retorno

# 4. Comprobar proyectos: Cambiará el estado de todos los proyectos cuya fecha de finalización
# ya haya sucedido.

def comprobar_proyecto(lista_proyectos): 
    retorno = False
    fecha_actual = datetime.today().date()  
    
    for i in range(len(lista_proyectos)):
        fecha_fin = datetime.strptime(lista_proyectos[i]["Fecha de fin"], "%d/%m/%Y").date()
        
        if fecha_fin < fecha_actual:
            lista_proyectos[i]["Estado"] = "Finalizado"
            print(lista_proyectos[i])
            retorno = True
            
    return retorno
    
# 5. Mostrar todos: Imprimirá por consola la información de todos los proyectos en formato de
# tabla:
# | Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |
# | Innovación AI | Desarrollo de IA | $1,000,000 | 01/01/2024 | 01/01/2025 | Activo |
# | Rediseño Web | Nueva página web | $300,000 | 15/02/2024 | 30/06/2024 | Cancelado |

def mostrar_proyectos(lista_proyectos):
    encabezado = "| id | Nombre del Proyecto | Descripcion | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n"
    separador = "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    mensaje = encabezado + separador

    for proyecto in lista_proyectos:
        id = proyecto["Id"]
        nombre = proyecto["Nombre del proyecto"]
        descripcion = proyecto["Descripcion"]
        presupuesto = proyecto["Presupuesto"]
        fecha_inicio = proyecto["Fecha de inicio"]
        fecha_fin = proyecto["Fecha de fin"]
        estado = proyecto["Estado"]
        
        formato = f"| {id} | {nombre} | {descripcion} | {presupuesto} | {fecha_inicio} | {fecha_fin} | {estado} |\n"
        mensaje += formato
    mensaje += separador 
    print(mensaje)
        
# 6. Calcular presupuesto promedio: Calculará e imprimirá el presupuesto promedio de todos los
# proyectos.

def calcular_presupuesto_promedio(lista_proyectos):
    acumulador = 0
    mensaje = ""
    for i in range(len(lista_proyectos)):
        auxiliar = lista_proyectos[i]["Presupuesto"]
        auxiliar = float(auxiliar)
        acumulador += auxiliar
    promedio = acumulador / len(lista_proyectos)
    mensaje += f"El promedio de presupuestos es: {promedio}"
    return mensaje
    
# 7. Buscar proyecto por nombre: Permitirá al usuario buscar y mostrar la información de un
# proyecto específico ingresando su nombre.

def buscar_proyecto_por_nombre():
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")
    nombre = input("Ingrese el nombre de un proyecto a buscar: ").lower()
    
    if(len(datos) < 1):
        retorno = False

    else: 
        for i in range(len(datos)):
            nombre_auxiliar = datos[i]["Nombre del proyecto"]
            nombre_auxiliar = nombre_auxiliar.lower()
        
            if(nombre_auxiliar == nombre):
                retorno = datos[i]
                break
            else:
                retorno = "No hay ningun proyecto con ese nombre"
    return retorno

# 8. Ordenar proyectos: Ofrecerá la opción de ordenar y mostrar la lista de proyectos por nombre,
# presupuesto, o fecha de inicio de forma ascendente o descendente.

def ordenar_proyectos_por_nombre(lista,orden):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(orden == True):
                if(lista[i]["Nombre del proyecto"] > lista[j]["Nombre del proyecto"]):
                    aux_nombre = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_nombre 

            else:
                if(lista[i]["Nombre del proyecto"] < lista[j]["Nombre del proyecto"]):
                    aux_nombre = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_nombre
                    
    return lista

def ordenar_proyectos_por_presupuesto(lista, orden):    
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(orden == True):
                if(float(lista[i]["Presupuesto"]) > float(lista[j]["Presupuesto"])):

                    aux_presupuesto = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_presupuesto

            else:
                if(float(lista[i]["Presupuesto"]) < float(lista[j]["Presupuesto"])):

                    aux_presupuesto = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_presupuesto
    return lista

def ordenar_proyectos_por_fecha_de_inicio(lista, orden):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(orden == True):
                if((datetime.strptime(lista[i]["Fecha de inicio"],"%d/%m/%Y").date()) > 
                (datetime.strptime(lista[j]["Fecha de inicio"],"%d/%m/%Y").date())):
                    aux_fecha_inicio = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_fecha_inicio

            else:
                if((datetime.strptime(lista[i]["Fecha de inicio"],"%d/%m/%Y").date()) < 
                (datetime.strptime(lista[j]["Fecha de inicio"],"%d/%m/%Y").date())):
                    aux_fecha_inicio = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_fecha_inicio
    return lista

# 9. Retomar proyecto: Vuelve a dar de alta un proyecto Cancelado, comprobando anteriormente
# que cumpla todos los requisitos para esto.

def dar_de_alta_proyecto():
    retorno = False
    fecha_actual = datetime.today().date()
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")
   
    if(len(datos) < 1):
        print("No hay proyectos para dar de alta")

    else:
        mostrar_proyectos(datos)
        id = input("Ingrese el id del proyecto a dar de alta: ")
        for i in datos:
            if(i["Id"] == id):
                fecha_final = datetime.strptime(i["Fecha de fin"],"%d/%m/%Y").date()
       
                if(i["Estado"] == "Cancelado" and (fecha_actual < fecha_final)):
                    modificar_dato(id,"Estado","Activo")         
                    retorno = True
                    break 
            else:
                retorno = False
                
    return retorno

# 10. La opción 10 del menú, le solicitará al usuario que ingrese un presupuesto. El programa
# deberá generar un reporte con todos los proyectos que superen ese presupuesto. Una función
# se encargará de realizar dicha acción, la misma deberá guardar el reporte en un archivo de
# texto indicando el número de reporte (el programa deberá recordar este dato de alguna
# forma), la fecha de solicitud del reporte, la cantidad de proyectos que coinciden con el criterio
# y el listado

def encontrar_presupuestos_mayor(presupuesto_proyecto):
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")
    presupuestos_mayor = []

    for i in datos:
        if(float(i["Presupuesto"]) > presupuesto_proyecto):
            presupuestos_mayor.append(i)
    return presupuestos_mayor

def generar_reporte_por_presupuesto(presupuesto,numero_reporte_del_archivo = "cantidad_de_reportes_presupuestos.txt"):
    if(os.path.exists(numero_reporte_del_archivo)):
        with open(numero_reporte_del_archivo, "r") as archivo:
            numero_reporte = int(archivo.read().strip())
    else:
        numero_reporte = 0

    numero_reporte += 1
    with open(numero_reporte_del_archivo, "w") as archivo:
        
        archivo.write(str(numero_reporte))
    nombre_archivo_reporte = f"Reporte_{numero_reporte}_presupuesto.txt"
    fecha_solicitud = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    reporte = {
        "Detalle de los proyectos": presupuesto,
        "Cantidad_de_proyectos": len(presupuesto),
        "Numero_reporte": numero_reporte,
        "Fecha_de_solicitud": fecha_solicitud
    }

    with open(nombre_archivo_reporte, "w") as archivo:
        archivo.write(json.dumps(reporte, indent=4))

# 11. La opción 11 del menú, le solicitará al usuario el nombre de un proyecto. Realizar un informe
# con las mismas características que el punto anterior

def encontrar_proyecto_por_nombre(nombre_proyecto):
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")
    nombres_proyectos = []

    for i in datos:
        i["Nombre del proyecto"] = i["Nombre del proyecto"].lower()
        if(i["Nombre del proyecto"] == nombre_proyecto):
            nombres_proyectos.append(i)
            
    return nombres_proyectos 

def generar_reporte_por_nombre(nombre,numero_reporte_del_archivo ="cantidad_de_reportes_nombre.txt"):
    if(os.path.exists(numero_reporte_del_archivo)):
        with open(numero_reporte_del_archivo, "r") as archivo:
            numero_reporte = int(archivo.read().strip())         
    else:
        numero_reporte = 0
    numero_reporte += 1
    with open(numero_reporte_del_archivo, "w") as archivo: 
        archivo.write(str(numero_reporte))
    nombre_archivo_reporte = f"Reporte_{numero_reporte}_nombre.txt"
    fecha_solicitud = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    reporte = {
        "Detalle de los proyectos": nombre,
        "Numero_de_reporte": numero_reporte,
        "Fecha_de_solicitud": fecha_solicitud,
        "Cantidad_de_proyectos": len(nombre)
    }

    with open(nombre_archivo_reporte, "w") as archivo:
        archivo.write(json.dumps(reporte, indent=4))

# 12. Salir: Terminará la ejecución del programa

# 2. Al finalizar el programa (puede ser en la opción salir) se deberá actualizar el archivo
# Proyectos.csv, con los datos de los proyectos.

# 3. Los proyectos que hayan sido terminados deberán guardarse en un archivo Json, llamado
# “ProyectosFinalizados.json”

def escribir_json_finalizados():
    retorno = False
    lista = []
    datos = leer_archivo_csv("Parcial_Mio\Proyectos.csv")

    for i in range(1,len(datos)):
        if(datos[i]["Estado"] == "Finalizado"):
            lista.append(datos[i])
        retorno = True
                    
    with open("ProyectosFinalizados.json", "w") as archivo:              
        json.dump(lista, archivo, indent=4)

    return retorno


#PARTE 2

#G. Calcular el/los proyectos activos con mayor presupuesto iniciados en invierno. En caso de
#que no haya indicar error
        

def proyectos_activos_con_mayor_presupuesto_invierno(proyectos):
    proyectos_invierno = [
        p for p in proyectos
        if p["Estado"] == "Activo" and datetime.strptime(p["Fecha de inicio"], "%d/%m/%Y").month in [6, 7, 8]
    ]
    
    if not proyectos_invierno:
        print("No hay proyectos activos iniciados en invierno.")
        return
    
    mayor_presupuesto = max(proyectos_invierno, key=lambda p: float(p["Presupuesto"]))
    
    print("Proyecto activo con mayor presupuesto iniciado en invierno:")
    for clave, valor in mayor_presupuesto.items():
        print(f"{clave}: {valor}")

#M. Mostrar el promedio de presupuesto de todos los proyectos finalizados que hayan durado
#más de 2 años. En caso de que no haya indicar error

def promedio_presupuesto_proyectos_finalizados_duracion_mayor_2_anios(proyectos):
    proyectos_finalizados = []
    
    # Filtrar proyectos finalizados con duración mayor a 2 años
    for proyecto in proyectos:
        if proyecto["Estado"] == "Finalizado":
            fecha_inicio = datetime.strptime(proyecto["Fecha de inicio"], "%d/%m/%Y")
            fecha_fin = datetime.strptime(proyecto["Fecha de fin"], "%d/%m/%Y")
            duracion = (fecha_fin - fecha_inicio).days
            
            if duracion > 2 * 365:
                proyectos_finalizados.append(proyecto)
    
    if proyectos_finalizados:
        total_presupuestos = 0
        for proyecto in proyectos_finalizados:
            total_presupuestos += float(proyecto["Presupuesto"])
        
        promedio_presupuesto = total_presupuestos / len(proyectos_finalizados)
        print(f"Promedio de presupuesto de proyectos finalizados con duración mayor a 2 años: {promedio_presupuesto:.2f}")
    else:
        print("No hay proyectos finalizados con duración mayor a 2 años.")