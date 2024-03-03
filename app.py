from flask import Flask, jsonify 

app = Flask(__name__) 

animales = ['Leon', 'Caballo', 'Perro','Elefante',]

@app.route('/animales', methods=['GET']) 
def obtener_animales():
    return jsonify(animales)

if __name__ == '__main__': 
    app.run(debug=True)