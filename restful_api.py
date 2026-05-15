from flask import Flask

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return {
        "mensagem": "Hello, World!",
        "status": "sucesso"
    }

if __name__ == '__main__':
    app.run(debug=True)