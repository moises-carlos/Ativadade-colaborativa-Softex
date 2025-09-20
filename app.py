from abc import ABC, abstractmethod

# Interface: Define um contrato de comportamento
class VeiculoMotorizado(ABC):
    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

# Composição: A classe Motor é parte da classe Veiculo
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__ligado = False # Atributo privado

    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} ligado."

    def get_status(self):
        return "ligado" if self.__ligado else "desligado"

# Herança e Polimorfismo: Carro implementa a interface VeiculoMotorizado
class Carro(VeiculoMotorizado):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Composição: O objeto Motor é criado dentro do Carro
        self.motor = Motor("V8")
    
    def ligar_motor(self):
        # Encapsulamento: Acessando o método do objeto Motor
        print(self.motor.ligar())
    
    def acelerar(self):
        if self.motor.get_status() == "ligado":
            print(f"O {self.modelo} está acelerando!")
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")

# Herança e Polimorfismo: Moto implementa a interface VeiculoMotorizado
class Moto(VeiculoMotorizado):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("250cc")
        
    def ligar_motor(self):
        print(self.motor.ligar())

    def acelerar(self):
        if self.motor.get_status() == "ligado":
            print(f"A {self.modelo} está acelerando na pista!")
        else:
            raise Exception("Erro: A moto precisa estar ligada para acelerar.")

# Função que usa polimorfismo
def testar_veiculo(veiculo):
    try:
        veiculo.ligar_motor()
        veiculo.acelerar()
    except Exception as e:
        print(f"Houve um problema: {e}")

# Exemplo de uso
meu_carro = Carro("Ford", "Mustang")
minha_moto = Moto("Honda", "CBR")

testar_veiculo(meu_carro)
print("-" * 20)
testar_veiculo(minha_moto)

# Exemplo de erro (acelerar sem ligar o motor)
print("-" * 20)
carro_quebrado = Carro("Fiat", "Uno")
try:
    carro_quebrado.acelerar()
except Exception as e:
    print(e)
