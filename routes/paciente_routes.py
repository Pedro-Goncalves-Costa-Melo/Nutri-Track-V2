from flask import Blueprint, request, jsonify
from controllers.paciente_controller import *

paciente_bp = Blueprint('paciente_bp', __name__)

@paciente_bp.route('/pacientes', methods=['GET'])
def get_pacientes():
    return jsonify(listar_pacientes())

@paciente_bp.route('/pacientes', methods=['POST'])
def add_paciente():
    data = request.json
    novo_paciente = criar_paciente(data['nome'], data['idade'], data['altura'], data['peso'], data['dieta_id'])
    return jsonify(novo_paciente), 201

@paciente_bp.route('/pacientes/<int:id>', methods=['GET'])
def get_paciente(id):
    paciente = buscar_paciente(id)
    return jsonify(paciente) if paciente else ('Paciente não encontrado', 404)

@paciente_bp.route('/pacientes/<int:id>', methods=['PUT'])
def update_paciente(id):
    data = request.json
    paciente = atualizar_paciente(id, data['nome'], data['idade'], data['altura'], data['peso'], data['dieta_id'])
    return jsonify(paciente) if paciente else ('Paciente não encontrado', 404)

@paciente_bp.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    if deletar_paciente(id):
        return ('', 204)
    return ('Paciente não encontrado', 404)
