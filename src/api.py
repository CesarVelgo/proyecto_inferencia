# importamos las librerias necesarias
import pandas as pd
from flask import Flask, request, jsonify
import joblib
import xgboost as xgb

# cargamos el modelo, el escalador y las columnas procesadas desde los archivos guardados
model = joblib.load('../models/xgboost_model.joblib')
scaler = joblib.load('../models/scaler.joblib')
columns_for_encoding = joblib.load('../models/columns_for_encoding.joblib')

# inicializamos la aplicación Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # obtenemos los datos de la solicitud en formato JSON
        data = request.get_json()

        # verificamos si los datos son una lista o un solo registro
        if isinstance(data, list):
            df = pd.DataFrame(data)  # convertimos a DataFrame si es una lista de registros
        else:
            df = pd.DataFrame([data])  # si es un solo registro, lo convertimos a lista

        # imprimimos las columnas recibidas para verificar
        print("\n")
        print("="*50)
        print("Columnas recibidas en la consulta:")
        print("-"*50)
        print(df.columns.tolist())

        # convertimos las columnas categóricas 'Brick' y 'Neighborhood' a tipo categoría si están presentes
        if 'Brick' in df.columns:
            df['Brick'] = df['Brick'].astype('category')
        if 'Neighborhood' in df.columns:
            df['Neighborhood'] = df['Neighborhood'].astype('category')

        # convertimos las columnas categóricas en variables dummy (variables binarias)
        df = pd.get_dummies(df, columns=['Brick', 'Neighborhood'], drop_first=True)

        # imprimimos las columnas después de la codificación para verificar
        print("\n")
        print("="*50)
        print("Columnas después de la codificación:")
        print("-"*50)
        print(df.columns.tolist())

        print("\n")
        print("="*50)
        # agregamos las columnas faltantes con valores False (para que coincidan con las del modelo)
        print("Columna faltante: Añadiendo con False.")
        print("-"*50)
        for col in columns_for_encoding:
            if col not in df.columns:
                print(f"{col}")
                df[col] = False  # añadimos la columna faltante con valor False

        # imprimimos las columnas después de agregar las columnas faltantes
        print("\n")
        print("="*50)
        print("Columnas después de agregar las columnas faltantes:")
        print("-"*50)
        print(df.columns.tolist())
                
        # reordenamos las columnas para que coincidan con el orden esperado por el modelo
        df = df[columns_for_encoding]

        # imprimimos las columnas finales antes de la predicción
        print("\n")
        print("="*50)
        print("Columnas finales para la predicción:")
        print("-"*50)
        print(df.columns.tolist())
        print("\n")
        # normalizamos las características numéricas utilizando el escalador
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
        df[numeric_columns] = scaler.transform(df[numeric_columns])

        # realizamos la predicción con el modelo
        predictions = model.predict(df)
        predictions = predictions.tolist()  # convertimos la predicción a lista para devolverla en JSON

        # devolvemos las predicciones como respuesta en formato JSON
        return jsonify({'prediction': predictions})

    except Exception as e:
        # en caso de error, devolvemos el mensaje de error en formato JSON
        return jsonify({'error': str(e)}), 400

# iniciamos la aplicación Flask en modo debug
if __name__ == '__main__':
    app.run(debug=True)
