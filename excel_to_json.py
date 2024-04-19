import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Ruta principal
@app.route('/', methods=['GET'])
def home():
    return 'Servidor en funcionamiento'

# Ruta para obtener los datos del archivo Excel en formato JSON
@app.route('/datos', methods=['GET'])
def obtener_datos():
    # Cargar el archivo Excel
    ruta_archivo = 'datos.xlsx'
    datos_excel = pd.read_excel(ruta_archivo)

    # Convertir los datos a formato JSON
    datos_json = datos_excel.to_json(orient='records')

    # Devolver los datos en formato JSON
    return jsonify(datos_json)

if __name__ == '__main__':
    app.run(debug=True)