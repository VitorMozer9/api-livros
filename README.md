# API de Livros em Flask

## 📖 Sobre o Projeto

Esta é uma API RESTful simples para gerenciar uma coleção de livros, desenvolvida como parte de um estudo prático sobre a criação de APIs com Python e a biblioteca Flask.

O projeto implementa as operações básicas de um **CRUD** (Create, Read, Update, Delete) em uma lista de livros armazenada em memória.

## 🚀 Funcionalidades

-   **Consultar** todos os livros da coleção.
-   **Consultar** um livro específico por seu `id`.
-   **Adicionar** um novo livro à coleção.
-   **Editar** as informações de um livro existente.
-   **Excluir** um livro da coleção (Endpoint não implementado no código-fonte atual, mas planejado).

## 🛠️ Como Executar o Projeto

1.  **Clone o repositório** (se estiver no GitHub):
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git)
    cd NOME-DO-SEU-REPOSITORIO
    ```

2.  **Crie um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências**:
    O único requisito é o Flask.
    ```bash
    pip install Flask
    ```

4.  **Execute a API**:
    ```bash
    python seu_arquivo.py
    ```
    A API estará rodando em `http://localhost:5000`.

## ⚙️ Endpoints da API

A URL base para todos os endpoints é `http://localhost:5000`.

| Verbo HTTP | Endpoint              | Descrição                                 | Exemplo de Corpo (Body)                           |
| :--------- | :-------------------- | :---------------------------------------- | :------------------------------------------------ |
| `GET`      | `/livros`             | Retorna a lista completa de livros.       | N/A                                               |
| `GET`      | `/livros/<id>`        | Retorna os dados de um livro específico.  | N/A                                               |
| `POST`     | `/livros`             | Adiciona um novo livro à lista.           | `{ "id": 4, "título": "...", "autor": "..." }`      |
| `PUT`      | `/livros/<id>`        | Altera os dados de um livro existente.    | `{ "título": "Novo Título", "autor": "Novo Autor" }` |
| `DELETE`   | `/livros/<id>`        | **(A ser implementado)** Deleta um livro. | N/A                                               |

---
