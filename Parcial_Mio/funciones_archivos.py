import datetime
import csv
import json
from datetime import datetime
from validaciones import *

def cargar_proyectos(nombre_archivo):
    proyectos = []
    with open(nombre_archivo, mode="r", newline="", encoding="utf-8") as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            fila["id"] = int(fila["id"])
            fila["Presupuesto"] = float(fila["Presupuesto"])
            fecha_inicio = datetime.strptime(fila["Fecha de inicio"], "%d-%m-%Y").strftime("%d/%m/%Y")
            fecha_fin = datetime.strptime(fila["Fecha de fin"], "%d-%m-%Y").strftime("%d/%m/%Y")
            fila["Fecha de inicio"] = fecha_inicio
            fila["Fecha de Fin"] = fecha_fin

            proyectos.append({
                "id": fila["id"],
                "Nombre": fila["Nombre del Proyecto"],
                "Descripción": fila["Descripcion"],
                "Fecha de Inicio": fecha_inicio,
                "Fecha de Fin": fecha_fin,
                "Presupuesto": fila["Presupuesto"],
                "Estado": fila["Estado"],
            })
    return proyectos

def guardar_proyectos(nombre_archivo, proyectos):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo_csv:
        campos = [
            "id",
            "Nombre del Proyecto",
            "Descripcion",
            "Fecha de inicio",
            "Fecha de Fin",
            "Presupuesto",
            "Estado",
        ]

        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor.writeheader()

        for proyecto in proyectos:
            fecha_inicio = datetime.strptime(proyecto["Fecha de Inicio"], "%d/%m/%Y")
            fecha_fin = datetime.strptime(proyecto["Fecha de Fin"], "%d/%m/%Y")
            escritor.writerow({
                "id": proyecto["id"],
                "Nombre del Proyecto": proyecto["Nombre"],
                "Descripcion": proyecto["Descripción"],
                "Fecha de inicio": fecha_inicio.strftime("%d-%m-%Y"),
                "Fecha de Fin": fecha_fin.strftime("%d-%m-%Y"),
                "Presupuesto": f"{proyecto['Presupuesto']:.2f}",
                "Estado": proyecto["Estado"],
            })

def guardar_reporte_presupuesto(proyectos_con_presupuesto_superior, presupuesto, numero_reporte):
    cantidad_proyectos = len(proyectos_con_presupuesto_superior)
    if cantidad_proyectos > 0:
        with open(
            f"Reporte_Presupuesto_{numero_reporte}.txt",
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:
            file.write(
                f"Reporte de proyectos con presupuesto mayor a ${presupuesto}:\n\n"
            )
            for proyecto in proyectos_con_presupuesto_superior:
                file.write(f"Nombre del Proyecto: {proyecto['Nombre']}\n")
                file.write(f"Descripción: {proyecto['Descripción']}\n")
                file.write(f"Presupuesto: ${proyecto['Presupuesto']:.2f}\n")
                file.write(f"Fecha de Inicio: {proyecto['Fecha de Inicio']}\n")
                file.write(f"Fecha de Fin: {proyecto['Fecha de Fin']}\n")
                file.write(f"Estado: {proyecto['Estado']}\n\n")
            file.write(f"Cantidad de proyectos encontrados: {cantidad_proyectos}")
        print(
            f"Se ha generado el reporte de proyectos con presupuesto mayor a ${presupuesto}."
        )
    else:
        print("No hay proyectos con presupuesto mayor al valor proporcionado.")

def guardar_reporte_nombre(proyectos_con_nombre, nombre, numero_reporte):
    cantidad_proyectos = len(proyectos_con_nombre)
    if cantidad_proyectos > 0:
        with open(f"Reporte_Nombre_{nombre}_{numero_reporte}.txt", mode="w", newline="", encoding="utf-8") as file:
            file.write(f"Reporte de proyectos que contienen '{nombre}' en el nombre:")
            for proyecto in proyectos_con_nombre:
                file.write(f"Nombre del Proyecto: {proyecto['Nombre']}\n")
                file.write(f"Descripción: {proyecto['Descripción']}\n")
                file.write(f"Presupuesto: ${proyecto['Presupuesto']:.2f}\n")
                file.write(f"Fecha de Inicio: {proyecto['Fecha de Inicio']}\n")
                file.write(f"Fecha de Fin: {proyecto['Fecha de Fin']}\n")
                file.write(f"Estado: {proyecto['Estado']}\n")
            file.write(f"Cantidad de proyectos encontrados: {cantidad_proyectos}")
        print(
            f"Se ha generado el reporte de proyectos con nombre que contiene '{nombre}'."
        )
    else:
        print(f"No hay proyectos que contengan '{nombre}' en el nombre.")
