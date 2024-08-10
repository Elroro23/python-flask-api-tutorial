#1)Instalamos los paquetes necesarios para que python funcione y verificamos las versiones:
#python --version
#pipenv --version
#2)Creamos un nuevo entorno virtual:
#pipenv install --python 3
#3)Instalamos el paquete de flask:
#pipenv install flask
#4)Creamos una carpeta(src) en la raiz del proyecto y dentro un archivo(app.py)
#5)Importamos Flask, jsonify y request(cuando esperas recibir información):
from flask import Flask, jsonify, request
app = Flask(__name__)

'''@app.route('/todos', methods=['GET'])
def hello_world():
    return '<h1>Hello!</h1>'''
#6)Ejecutamos el servidor. nueva terminal(pipenv run python src/app.py)
todos = [
    {'label': 'Sample Todo 1', 'done': False}, #Agregamos nuestros datos a una variable.
    ]
@app.route('/todos', methods=['GET']) #Especificamos el "endpoint", método y lo que retornará el servidor(función):

def get_todos():
    return jsonify(todos)#Convertimos nuestros datos a "Json".
    
#POST:
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json #Body del POST.
    print('Incoming request with the following body', request_body)#Console.log + body
    todos.append(request_body)#Agregamos los nuevos datos(request_body) al final del array "todos" con el método append.
    return jsonify(todos)

#DELETE:
#<int:position>:Indicamos la posición de un elemento a eliminar
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is the position to delete:', position)
    todos.pop(position)#Definimos la posición del elemento y lo eliminamos con .pop().
    return jsonify(todos) #Retornamos el array sin el elemento eliminado

#Ultimo paso)Definimos el puerto(normalmente 3000):
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)