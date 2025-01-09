# importamos las librerias necesarias
import requests
import json

# definimos la url de la API donde se realizará la predicción
url = 'http://localhost:5000/predict' 

# datos para la prediccion de precios
# para un solo dato
data = {
    "SqFt": 1790,
    "Bedrooms": 1,
    "Bathrooms": 1,
    "Offers": 1,
    "Brick":"Yes",
    "Neighborhood":"North",
}
'''
# para enviar más de un dato, definimos una lista con varios registros
data = [
    {
        "SqFt": 1790,
        "Bedrooms": 1,
        "Bathrooms": 1,
        "Offers": 1,
        "Brick": "Yes",
        "Neighborhood": "North",
    },
    {
        "SqFt": 2030,
        "Bedrooms": 4,
        "Bathrooms": 2,
        "Offers": 3,
        "Brick": "No",
        "Neighborhood": "West",
    },
    {
        "SqFt": 1740,
        "Bedrooms": 3,
        "Bathrooms": 2,
        "Offers": 1,
        "Brick": "Yes",
        "Neighborhood": "East",
    }
]
'''

# enviamos los datos a la API utilizando una solicitud POST
response = requests.post(url, json=data)

# verificamos si la respuesta de la API fue exitosa (código 200)
if response.status_code == 200:
    # si la respuesta es exitosa, imprimimos la predicción recibida
    print(f"Predicción de precio: {response.json()['prediction']}")
else:
    # si hay un error, imprimimos el mensaje de error
    print(f"Error en la predicción: {response.json()['error']}")
