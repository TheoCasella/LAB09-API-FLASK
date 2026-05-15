from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

mensagem = "Hello, World!"

@app.get('/api')
def get_msg():
    return {"conteudo": mensagem}

@app.post('/api')
def post_msg():
    global mensagem
    dados = Request.get_json()
    mensagem = dados.get("texto")
    return {"aviso": "Mensagem criada!", "nova_mensagem": mensagem}, 201

@app.put('/api')
def put_msg():
    global mensagem
    dados = Request.get_json()
    mensagem = dados.get("texto")
    return {"aviso": "Mensagem atualizada!", "nova_mensagem": mensagem}

@app.delete('/api')
def delete_msg():
    global mensagem
    mensagem = ""
    return {"aviso": "Mensagem apagada!"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)