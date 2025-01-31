pacientes = []

class Paciente:
    def __init__(self, id, nome, idade, altura, peso, dieta_id):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.dieta_id = dieta_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "peso": self.peso,
            "dieta_id": self.dieta_id
        }
