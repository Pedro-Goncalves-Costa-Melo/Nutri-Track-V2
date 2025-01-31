from flask import Blueprint, request, jsonify
from controllers.dieta_controller import *

dieta_bp = Blueprint('dieta_bp', __name__)

@dieta_bp.route('/dietas', methods=['GET'])
def get_dietas():
    return jsonify(listar_dietas())

@dieta_bp.route('/dietas', methods=['POST'])
def add_dieta():
    data = request.json
    nova_dieta = criar_dieta(data['nome'], data['descricao'])
    return jsonify(nova_dieta), 201

@dieta_bp.route('/dietas/<int:id>', methods=['GET'])
def get_dieta(id):
    dieta = buscar_dieta(id)
    return jsonify(dieta) if dieta else ('Dieta não encontrada', 404)

@dieta_bp.route('/dietas/<int:id>', methods=['PUT'])
def update_dieta(id):
    data = request.json
    dieta = atualizar_dieta(id, data['nome'], data['descricao'])
    return jsonify(dieta) if dieta else ('Dieta não encontrada', 404)

@dieta_bp.route('/dietas/<int:id>', methods=['DELETE'])
def delete_dieta(id):
    if deletar_dieta(id):
        return ('', 204)
    return ('Dieta não encontrada', 404)
