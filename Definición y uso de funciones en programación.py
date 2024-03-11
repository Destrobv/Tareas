def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad en base a los datos proporcionados.

    Args:
    datos (dict): Un diccionario que contiene los datos de temperatura de múltiples ciudades y semanas.
                  El formato del diccionario debe ser:
                  {
                      'ciudad1': [temp1_semana1, temp1_semana2, ..., temp1_semanaN],
                      'ciudad2': [temp2_semana1, temp2_semana2, ..., temp2_semanaN],
                      ...
                      'ciudadN': [tempN_semana1, tempN_semana2, ..., tempN_semanaN]
                  }

    Returns:
    dict: Un diccionario que contiene la temperatura promedio de cada ciudad.
          El formato del diccionario devuelto es:
          {
              'ciudad1': temperatura_promedio_ciudad1,
              'ciudad2': temperatura_promedio_ciudad2,
              ...
              'ciudadN': temperatura_promedio_ciudadN
          }
    """
    temperatura_promedio_por_ciudad = {}

    for ciudad, temperaturas in datos.items():
        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        temperatura_promedio_por_ciudad[ciudad] = temperatura_promedio

    return temperatura_promedio_por_ciudad



datos_de_temperatura = {
    'Ciudad A': [25, 28, 30, 27],
    'Ciudad B': [22, 21, 23, 24],
    'Ciudad C': [19, 20, 18, 17]
}

resultado = calcular_temperatura_promedio(datos_de_temperatura)

print("Temperatura promedio por ciudad:")
for ciudad, temp_promedio in resultado.items():
    print(f"{ciudad}: {temp_promedio}")


