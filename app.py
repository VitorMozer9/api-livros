# API - é um lugar para disponibilizar recursos e/ou funcionalidades 
# 1 - objetivo - API CRUD livros
# 2 - URL base - localhost.com
# 3 - EndPoints - Funcionalidades(verbos) 
#   - localhost/livros(GET)
#   - localhost/livros(POST) //incluir novos livros
#   - localhost/livros/id (GET)
#   - localhost/livros/id (PUT) //modificação(update)
#   - localhost/livros/id (DELETE)
# 4 - Quais recursos - Livros
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'título' : 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'J.R.R Tolkien'
    },
    {
        'id' : 2,
        'título' : 'Harry Potter e a Pedra Filosofal',
        'autor' : 'J.K Howling'
    },
    {
        'id' : 3,
        'título' : 'James Clear',
        'autor' : 'Hábitos Atômicos'
    }
]

#Oq eu preciso, conseguir consultar todos, consultar por id, incluir novos lovros, editar livros existentes e deletar 
@app.route('/livros', methods = ['GET'])
def obterLivros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obterLivrosPorId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editaLivroPorId(id):
    livroAlterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])

@app.route('/livros', methods = ['POST'])       
def incluiLivro():
    livroIncluso = request.get_json()
    livros.append(livroIncluso)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)


app.run(port=5000, host='localhost',debug=True)