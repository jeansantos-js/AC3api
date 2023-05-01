from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota 1
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        # Lógica para retornar todos os usuários
        return jsonify({'users': []})
    elif request.method == 'POST':
        # Lógica para criar um novo usuário
        return jsonify({'message': 'Usuário criado com sucesso!'})
    elif request.method == 'DELETE':
        # Lógica para deletar todos os usuários
        return jsonify({'message': 'Todos os usuários foram deletados com sucesso!'})

# Rota 2
@app.route('/users/<int:user_id>', methods=['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        # Lógica para retornar um usuário específico
        return jsonify({'user': {'id': user_id, 'name': 'João'}})
    elif request.method == 'POST':
        # Lógica para atualizar um usuário específico
        return jsonify({'message': 'Usuário atualizado com sucesso!'})
    elif request.method == 'DELETE':
        # Lógica para deletar um usuário específico
        return jsonify({'message': f'O usuário com ID {user_id} foi deletado com sucesso!'})

# Rota 3
@app.route('/products', methods=['GET', 'POST', 'DELETE'])
def products():
    if request.method == 'GET':
        # Lógica para retornar todos os produtos
        return jsonify({'products': []})
    elif request.method == 'POST':
        # Lógica para criar um novo produto
        return jsonify({'message': 'Produto criado com sucesso!'})
    elif request.method == 'DELETE':
        # Lógica para deletar todos os produtos
        return jsonify({'message': 'Todos os produtos foram deletados com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)