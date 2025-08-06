
from abc import ABC, abstractmethod
import uuid

# -------------------------------------------------
# 1) Interface                                   🡇
# -------------------------------------------------
#Interface (classe abstrata): define um contrato para logar_entrada().
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
        return self._id #retorna o id armazenado


class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
         print(f"[LOG] {evento}") # vai imprimir no formato  [LOG] <mensagem> 


# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
#superclasse para Passageiro e Funcionario
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
#classe usada em coomposição com Passageiro (se não existir passageiro, não existe bagagem)
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg
    def __str__(self):
        return f"{self.descricao} – {self.peso} kg"


# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
#recebe a herença de Pessoa e tem composição com Bagagem
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
#tem herença múltipla: Pessoa + IdentificavelMixin + Interface Logavel (implementação)
class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, nome: str, cpf: str, cargo: str, matricula: str):
        Pessoa.__init__(self,nome, cpf) #chama o construtor da classe pessoa
        IdentificavelMixin.__init__(self) #herda as coisas de IdentificavelMixin
        self.cargo = cargo
        self.matricula = matricula

    def exibir_dados(self): #imprime nome, cargo, matrícula e ID
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Matrícula: {self.matricula}")
        print(f"ID: {self.get_id()}")

    def logar_entrada(self):
        print(f"{self.nome} (Funcionário) entrou no sistema.")



# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
#tem composição com voo (o voo precisa de uma aeronave)
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
#tem agregação de Passageiros e Tripulantes (já que eles vão estar no voo) e composição com MiniAeroave (um voo não existe sem uma aeronave)
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
        if funcionario in self.tripulacao:  #verifica se o funcionário já está na lista de tripulação
            print("Tripulante já adicionado.")
        else:
            self.tripulacao.append(funcionario)  #adiciona o funcionário à lista de tripulação

    def listar_passageiros(self):
        for p in self.passageiros: #vai passar por cada elemento da lista de passageiros e impreimir eles
            print(f"- {p}")

    def listar_tripulacao(self):
        for t in self.tripulacao:  #percorre cada membro da tripulação
            print(f"- {t}")       #imprime o nome (ou representação) do tripulante
    
    def __str__(self): #vai definir como o objeto vai ser representado como uma string
        return f"Voo {self.numero_voo} de {self.origem} para {self.destino} – {self.aeronave.resumo_voo()}" 

# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
#classe que agrega Voo (as companhias aéreas precisam que voos, mas continuam existindo sem eles)
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
#tem herença múltipla: usa mixin e implementa a interface Logavel (implementação)
class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome: str):
        super().__init__()
        self.nome = nome 

    def logar_entrada(self):
        print(f"\n{self.nome} (Auditor) entrou no sistema.")

    def auditar_voo(self, voo: Voo):
        print(f"\nAuditoria do voo {voo.numero_voo}")
        if len(voo.passageiros) > voo.aeronave.capacidade:
            print("Excesso de passageiros.")
        else:
            print("Capacidade adequada!")

        if len(voo.tripulacao) ==  0:
            print("Nenhum tripulante a bordo.")
        else:
            print("Mínimo de tripulantes adequado.")
    
    def __str__(self): 
        return f"Auditor {self.nome} (ID: {self.get_id()})"
            

# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":

   # Criando companhias
    kat = CompanhiaAerea("Kat")
    helo = CompanhiaAerea("Helo")
    
    # Criando aeronaves
    aeronave1 = MiniAeronave("ATR 72", 8)
    aeronave2 = MiniAeronave("SCR 54", 12)

    # Criando passageiros
    p1 = Passageiro("Helloísa", "123.456.789-00")
    p2 = Passageiro("Katielly", "321.654.987-55")
    p3 = Passageiro("Memetrios", "032.021.065-00")

    # Criando funcionários
    f1 = Funcionario("Ytalo", "125.145.198-77", "Comissário", "Y335")  
    f2 = Funcionario("João Felipe", "445.778.112-33", "Piloto", "J775")
    
    # Criando auditores
    a1 = Auditor("Vivi")
    a2 = Auditor("Vitória")

    # Criando voos e adicionando às companhias
    voo1 = Voo("V001", "Fortaleza", "Recife", aeronave1)
    voo2 = Voo("V002", "Natal", "João Pessoa", aeronave2)
    kat.adicionar_voo(voo1)
    kat.adicionar_voo(voo2)

    voo3 = Voo("V003", "São Paulo", "Rio de Janeiro", aeronave1)
    voo4 = Voo("V004", "Brasília", "Salvador", aeronave2)
    helo.adicionar_voo(voo3)
    helo.adicionar_voo(voo4)

    
    #adicionando passageiros aos voos
    voo1.adicionar_passageiro(p1)
    voo1.adicionar_passageiro(p2)
    voo2.adicionar_passageiro(p3)

    #adicionando trupulantes aos voos
    voo1.adicionar_tripulante(f1)
    voo1.adicionar_tripulante(f2)


    #adicionando bagagens
    p1.adicionar_bagagem(Bagagem("Mochila", 4.5))
    p1.adicionar_bagagem(Bagagem("Mala grande", 15.0))
    
    p2.adicionar_bagagem(Bagagem("Bolsa", 3.0))

    print("--------------------------------")
    print("SISTEMA DE GERENCIAMENTO DE VOOS")
    print("--------------------------------")

    print("\nDADOS DOS FUNCINÁRIOS:")
    f1.exibir_dados()
    print()
    f2.exibir_dados()

    #lstando bagagens dos passageiros
    print("\nBAGAGENS DE HELLOÍSA:")
    p1.listar_bagagens()

    print("\nBAGAGENS DE KATIELLY:")
    p2.listar_bagagens()
    
    #listando passageiros e tripulação dos voos
    print("\nPASSAGEIROS DO VOO 1:")
    voo1.listar_passageiros()

    print("\nTRIPULAÇÃO DO VOO 1:")
    voo1.listar_tripulacao()

    print("\nPASSAGEIROS DO VOO 2:")
    voo2.listar_passageiros()

    print("\nTRIPULAÇÃO DO VOO 2:")
    voo2.listar_tripulacao()

    
    #auditorias
    print("\nAUDITORIAS DOS VOOS:")
    a1.logar_entrada()
    a1.auditar_voo(voo1)

    a2.logar_entrada()
    a2.auditar_voo(voo2)


    #listando voos por companhia
    print("\nVOOS DA COMPANHIA KAT:")
    kat.listar_voos()

    print("\nVOOS DA COMPANHIA HELO:")
    helo.listar_voos()

    #buscando voos
    print("\nBUSCAR VOOS:")
    print(kat.buscar_voo("V001"))
    
