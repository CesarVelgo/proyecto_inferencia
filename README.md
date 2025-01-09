Proyecto Final Despliegue de Proyecto en la Nube, 
consulta de una API mediante la ejecucion de api.py desde el servidor en la nube 
y la consulta se realiza desde consulta.py, en la cual se debe especdificar la ruta del servidor y definir los datos para poder obtener las predicciones. 

Los datos se envian en formato JSON y el resultado tambien se obtiene en el mismo formato.

data = {
    "SqFt": 1790,
    "Bedrooms": 1,
    "Bathrooms": 1,
    "Offers": 1,
    "Brick":"Yes",
    "Neighborhood":"North",
}

Se permite la consulta de mas de un dato. agregamos una lista con varios registros  
en el archivo consulta.py 

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
