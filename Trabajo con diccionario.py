#diccionario
informacion_personal = {
    "nombre": "josue",
    "edad": 20,
    "ciudad": "shell",
    "profesion": "desconocida"
}

print(informacion_personal)

#Modificar cuidad
informacion_personal["ciudad"] = "quito"
print(informacion_personal)

#agregar profesion
informacion_personal["profesion"] = "Ingeniero"
print(informacion_personal)


if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123456789"

informacion_personal.pop("edad")
print(informacion_personal)