from flask import Flask, request, jsonify
import csv
import random
import os
app = Flask(__name__)

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
CSV_PATH= os.path.join(BASE_DIR, "palabras.csv")
#CSV PATH = palabras.csv"
#Leer CSV al iniciar la app
palabras = []
with open(CSV_PATH, "r", encoding="utf-8") as archivo:
    lector= csv.DictReader(archivo)
    for fila in lector:
        palabras.append({ 
            "palabra": fila["palabra"], 
            "categoria": fila["categoria"] 
        })

app = Flask(__name__)
# DB_PATH = "palabras.db"

@app.route("/") 
def home():
    return "Mi API de palabras con Flask - Funciona correctamente 😉"

#/palabras?cantidad=5
@app.route("/palabras")
def palabras_aleatorias():
    cantidad =int(request.args.get("cantidad", 2))
    seleccionadas =random.sample(palabras, min(cantidad, len(palabras)))
    return jsonify(seleccionadas)
@app.route("/categorias")
def listar_categorias():
    categorias = []
    for p in palabras:
        cat = p["categoria"].lower()
        if cat not in categorias:
            categorias.append(cat)
    return jsonify (sorted (categorias))

if __name__ == "__main__":
    app.run(debug=True)
