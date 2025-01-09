# importamos las librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# cargamos el dataset desde un archivo CSV
df = pd.read_csv('../data/house-prices.csv')

# imprimimos las columnas del dataframe para ver qué tenemos
print("\n")
print("="*50)
print("Columnas en el DataFrame:")
print("-"*50)
print(df.columns)

# eliminamos la columna 'Home' si está presente en el dataset, ya que no es necesaria
df = df.drop(['Home'], axis=1, errors='ignore')  # usamos 'ignore' por si la columna no existe

# identificamos las columnas numéricas y categóricas en el dataframe
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

# convertimos las columnas categóricas en variables dummy (variables binarias)
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# imprimimos las columnas después de la codificación para verificar el cambio
print("\n")
print("="*50)
print("Columnas después de la codificación:")
print("-"*50)
print(df.columns)

# separamos las características (X) y la variable objetivo (y)
X = df.drop('Price', axis=1)  # todas las columnas excepto 'Price'
y = df['Price']  # la columna objetivo 'Price'

# actualizamos las columnas numéricas después de realizar la codificación
numeric_columns = X.select_dtypes(include=['int64', 'float64']).columns

# normalizamos las características numéricas para que tengan media 0 y desviación estándar 1
scaler = StandardScaler()
X[numeric_columns] = scaler.fit_transform(X[numeric_columns])

# dividimos el dataset en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# creamos y entrenamos el modelo XGBoost para regresión
model = xgb.XGBRegressor(eval_metric='rmse')
model.fit(X_train, y_train)

# guardamos el modelo entrenado, el escalador y las columnas de codificación para usarlos en el futuro
joblib.dump(model, '../models/xgboost_model.joblib')
joblib.dump(scaler, '../models/scaler.joblib')

# guardamos las columnas que se usaron para la codificación de las características
columns_for_encoding = X_train.columns.tolist()
joblib.dump(columns_for_encoding, '../models/columns_for_encoding.joblib')


# imprimimos un mensaje indicando que el modelo y los artefactos fueron guardados exitosamente
print("\n")
print("-"*55)
print("|  Modelo, escalador y columnas guardadas con éxito.  |")
print("-"*55)
print("\n")