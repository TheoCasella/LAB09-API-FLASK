from flask import Flask, request

app = Flask(__name__)

mensagem = "Hello, World!"

@app.route('/api', methods=['GET'])
def get_msg():
    return {"conteudo": mensagem}

@app.route('/api', methods=['POST'])
def post_msg():
    global mensagem
    dados = request.get_json()
    mensagem = dados.get("texto")
    return {"aviso": "Mensagem criada!", "nova_mensagem": mensagem}, 201

@app.route('/api', methods=['PUT'])
def put_msg():
    global mensagem
    dados = request.get_json()
    mensagem = dados.get("texto")
    return {"aviso": "Mensagem atualizada!", "nova_mensagem": mensagem}

@app.route('/api', methods=['DELETE'])
def delete_msg():
    global mensagem
    mensagem = ""
    return {"aviso": "Mensagem apagada!"}

if __name__ == '__main__':
    app.run(debug=True)