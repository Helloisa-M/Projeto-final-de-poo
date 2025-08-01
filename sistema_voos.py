
from abc import ABC, abstractmethod
import uuid

# -------------------------------------------------
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
class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, nome: str, cpf: str, cargo: str, matricula: str):
        Pessoa.__init__(nome, cpf) #chama o construtor da classe pessoa
        IdentificavelMixin.__init__(self) #herda as coisas de IdentificavelMixin
        self.cargo = cargo
        self.matricula = matricula

    def exibir_dados(self): #imprime nome, cargo, matrícula e ID
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.nome}")
        print(f"Matrícula: {self.nome}")
        print(f"Nome: {self.nome}")

    def logar_entrada(self):
        print(f"{self.nome} (Funcionário) entrou no sistema.")



# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo #armazenando o modelo
        self.capacidade = capacidade #armazenando a capacidade

    def resumo_voo(self):
        return f"Aeronave modelo {self.modelo} - Capacidade {self.capacidade}" #retorna uma string com o modelo e capacidade da aeronave


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
class Voo:
    def __init__(self, numero_voo: str, origem: str, destino: str, aeronave: MiniAeronave): #aeronave: MiniAeronave quer dizer que aeronave deve se comportar como um objeto de MiniAeronave (relação de composição)
        #armazena os atributos e cria as listas
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.aeronave = aeronave
        self.passageiros = []
        self.tripulacao = []

    def adicionar_passageiro(self, passageiro: Passageiro): #passageiro: Passageiro quer dizer que passageiro deve se comportar como um objeto da classe Passageiro
        if passageiro in self.passageiros: #verifica se o passageiro específico já está na lista de passageiros
            print("O passageiro já está no voo")
        elif len(self.passageiros) < self.aeronave.capacidade: #verifica se a quantidade de passageiros está menor do que a capacidade máxima da aeronave
            self.passageiros.append(passageiro) #se a condição for verdadeira, o passageiro pode ser adicionado
        else: #se a condição não for verdadeira, o passageiro não vai ser colocado no voo pois a capacidade já vai ter sido atingida
            print("A capacidade máxima da aeronave foi atingida")
        

    def adicionar_tripulante(self, funcionario: Funcionario):
        pass

    def listar_passageiros(self):
        for p in self.passageiros: #vai passar por cada elemento da lista de passageiros e impreimir eles
            print(f"- {p}")

    def listar_tripulacao():
        pass


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        if len(nome) >= 3:
            self._nome = nome  #armazena nome se válido
        else:
            self._nome = "SemNome"  #usa nome padrão se inválido
        self._voos = []  #cria lista vazia de voos

    @property #permite acessar o atributo protegido
    def nome(self):
        return self._nome  #retorna o nome

    @nome.setter #permite acessar o atributo protegido e fazer modificações
    def nome(self, novo_nome: str):
        if len(novo_nome) >= 3: #se o novo nome tiver 3 ou mais letras, ele é válido
            self._nome = novo_nome  #atualiza nome se válido

    def adicionar_voo(self, voo):
        self._voos.append(voo)  #adiciona voo na lista

    def buscar_voo(self, numero: str):
        for voo in self._voos: #para cada voo na lista de voos
            if voo.numero_voo == numero: #verifica se o número buscado pelo usuário é o número de algúm voo dentro da lista
                return voo #retorna o voo se a condição for verdadeira
        return None #caso a condição não seja verdadeira, vai retornar None

    def listar_voos(self): 
        for voo in self._voos: #para cada voo na lista de voos
            print(voo)  #imprime cada voo



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
