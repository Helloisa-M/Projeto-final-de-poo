
from abc import ABC, abstractmethod
import uuid

# ----------------------------------------------
# 1) Interface                                   🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass


# -------------------------------------------------
# 2) Mixins                                      🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self):
        self._id = str(uuid.uuid4()) #gera um id e armazena ele como string

    def get_id(self):
        return self._id() #retorna o id armazenado


class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
         print(f"[LOG] {evento}") # vai imprimir no formato  [LOG] <mensagem> 


# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome #armazenando nome como um atributo protegido
        self._cpf = cpf #armazenando cpf como um atributo protegido

    @property
    def nome(self):
        return self._nome #vai retornar o nome
    def __str__(self):
        return f"{self._nome} ({self._cpf})" #vai retornar o nome e cpf da pessoa no seguinte formato: "Maria (123.456.789-00)"


# -------------------------------------------------
# 4) Bagagem — classe simples                    🡇
# -------------------------------------------------
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg
    def __str__(self):
        return f"{self.descricao} – {self.peso} kg"


# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf) #chama o construtor da classe pessoa (que é a classe mãe)
        self.bagagens = [] #lista vazia de bagagens

    def adicionar_bagagem(self, bagagem: Bagagem):
        self.bagagens.append(bagagem) #adicina uma bagagem na lista de bagagens

    def listar_bagagens(self):
        for bagagem in self.bagagens: #pra cada bagagem na lista de bagagens
            print(f"-- {bagagem}") #imprime cada bagagem na lista
        


# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------
# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, matricula
# - Métodos:
#   • exibir_dados() → imprime nome, cargo, matrícula e ID
#   • logar_entrada() → registra no log 
''' def logar_entrada(self):
         print(f"{self.nome} (Funcionário) entrou no sistema.") '''


# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        # TODO: armazenar modelo e capacidade
        pass
    def resumo_voo(self):
        # TODO: retornar string com modelo e capacidade
        pass


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------
# TODO: Implementar a classe Voo
# - Atributos: numero_voo, origem, destino, aeronave
# - Listas: passageiros, tripulacao
# - Métodos:
#   • adicionar_passageiro()  (verificar duplicidade e capacidade)
#   • adicionar_tripulante()
#   • listar_passageiros()
#   • listar_tripulacao()


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        # TODO: validar nome (≥ 3 letras) e criar lista vazia de voos
        pass
    @property
    def nome(self):
        # TODO: retornar nome
        pass
    @nome.setter
    def nome(self, novo_nome: str):
        # TODO: validar + atualizar nome
        pass
    def adicionar_voo(self, voo):
        # TODO: adicionar voo à lista
        pass
    def buscar_voo(self, numero: str):
        # TODO: retornar voo ou None
        pass
    def listar_voos(self):
        # TODO: imprimir todos os voos
        pass


# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_voo(voo) → verifica:
#       ▸ passageiros ≤ capacidade
#       ▸ existe ao menos 1 tripulante
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"


# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":
    """
    TODO:
      • Criar 2 companhias, 2 voos cada, passageiros, funcionários e auditor.
      • Adicionar bagagens, listar passageiros, auditar voos.
      • Mostrar saídas no console para validar implementações.
    """
    pass