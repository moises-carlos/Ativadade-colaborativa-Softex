
# Modificar código abaixo para:

# Obrigar um motor no veículo
# Obrigar uma placa no veículo
# Obrigar uma velocidade no veículo
# Obrigar funções frear e desligar(só desliga com carro parado)
# Implementar uma função de STR no veículo que fornece detalhes do veículo por texto
# Ter uma potência no motor
# Ter uma taxa de aceleração no motor (é o incremento de velocidade por aceleração)
# Ter uma solicitação de cinto de segurança havendo velocidade igual ou superior a 30 km/h


from abc import ABC, abstractmethod

# Interface: Define um contrato de comportamento
class VeiculoMotorizado(ABC):

    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    

# Composição: A classe Motor é parte da classe Veiculo
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__ligado = False # Atributo privado
        self.__movendo = False # Indica se o veiculo está em movimento

    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} ligado."
    
    def desligar(self):
        if not self.__movendo:
            self.__ligado = False
            return f"Motor {self.tipo} ligado."
        else: 
            raise Exception("Não é possível desligar o carro em movemnto.")
            

    def get_status(self):
        return "ligado" if self.__ligado else "desligado"
    
    def get_status_completo(self):
        return {"ligado": self.__ligado, "movendo": self.__movendo }
    
    def mover(self):
        if self.__ligado:
            self.__movendo = True
            return True
        return False

    def parar(self):
        self.__movendo = True

    
    
        
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
        status = self.motor.get_status_completo()
        if status["ligado"]:
            if self.motor.mover():
                print(f"O {self.modelo} começou a se mover!")
            else:
                raise Exception("Erro: O motor precisa estar ligado para acelerar.")


    def frear(self):
        status = self.motor.get_status_completo()
        if status["movendo"]:
            self.motor.parar()
            print(f"O {self.modelo} Parou de se mover.")
        else:
            print(f"O {self.modelo} já está parado.")

    def desligar(self):
        try:
            print(self.motor.desligar())
        except Exception as e:
            print(f"Erro: {e}")

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

    def frear(self):
        status = self.motor.get_status_completo()
        if status["movendo"]:
            self.motor.parar()
            print(f"O {self.modelo} está parando.")
        else:
            print(f"O {self.modelo} já está parado.")
        
    def desligar(self):
        try: 
            print(self.motor.desligar())
        except Exception as e:
            print(f"Error: {e}")
# Função que usa polimorfismo
def testar_veiculo(veiculo):
    try:
        veiculo.ligar_motor()
        veiculo.acelerar()
        veiculo.frear()
        veiculo.desligar()
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
