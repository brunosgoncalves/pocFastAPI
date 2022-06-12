"""
reader = https://www.uvicorn.org/
para iniciar o dev:
    python -m uvicorn main:app --reload
"""


from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unittario": 4, "quanidade": 5},
    2: {"item": "garrafa 2L", "preco_unittario": 15, "quanidade": 5},
    3: {"item": "garrafa 750 ml", "preco_unittario": 10, "quanidade": 5},
    4: {"item": "lata mini", "preco_unittario": 2, "quanidade": 5},
}

#decorator @
@app.get("/")
def home():
    return {"Vendas": len(vendas)}


"""Usar sempre Tipagem para ser mais eficientes e tambem pelo Fastapi valida automaticamente"""
@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro":"Id Venda Inexistente"}


