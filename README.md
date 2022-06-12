
# POC FastAPI

Apenas um teste na FastAPI

## Documentação da API

#### Retorna quantidade dos itens

```http
  GET /
```


#### Retorna um item

```http
  GET /vendas/${id_venda}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id_venda` | `int` | **Obrigatório**. A chave do item pra buscar a venda sua API |



