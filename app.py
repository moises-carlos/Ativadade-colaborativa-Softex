
# Modificar código abaixo para:

# Obrigar um motor no veículo --
# Obrigar uma placa no veículo--
# Obrigar uma velocidade no veículo --
# Obrigar funções frear e desligar(só desliga com carro parado) --
# Ter uma potência no motor 
# Ter uma taxa de aceleração no motor (é o incremento de velocidade por aceleração)
# Ter uma solicitação de cinto de segurança havendo velocidade igual ou superior a 30 km/h


from abc import ABC, abstractmethod

# Interface: Define um contrato de comportamento
class VeiculoMotorizado(ABC):
    def __init__(self,motor, placa, velocidade = 0):
        self.motor = motor
        self.placa = placa
        self.velocidade = velocidade
        

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
    def __init__(self, tipo, potencia, taxa_aceleracao):
        self.tipo = tipo
        self.potencia = potencia
        self.taxa_aceleracao = taxa_aceleracao
        self.__ligado = False
        self.__movendo = False

    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} ligado."

    def desligar(self, velocidade):
        if velocidade > 0:
            raise Exception("Não é possível desligar o motor em movimento")
        self.__ligado = False
        return f"Motor {self.tipo} desligado."

    def mover(self):
        if self.__ligado:
            self.__movendo = True
            return True
        return False

    def parar(self):
        self.__movendo = False

    def get_status(self):
        return "ligado" if self.__ligado else "desligado"

    def get_status_completo(self):
        return {"ligado": self.__ligado, "movendo": self.__movendo}
    
    
        
# Herança e Polimorfismo: Carro implementa a interface VeiculoMotorizado
class Carro(VeiculoMotorizado):

    def __init__(self, marca, modelo,motor, placa, velocidade = 0):
        super().__init__(motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo
      
    def ligar_motor(self):
        print(self.motor.ligar())
        
    
    def acelerar(self):
        if self.motor.get_status() == "ligado":
            self.velocidade += self.motor.taxa_aceleracao
            self.motor.mover()
            print(f"A {self.modelo} acelerou para {self.velocidade} km/h.")
        else:
            raise Exception("Erro: A moto precisa estar ligada para acelerar.")


    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            if self.velocidade <= 0:
                self.velocidade = 0
                self.motor.parar()
            print(f"O {self.modelo} reduziu a velocidade para {self.velocidade} km/h.")
        else:
            print(f"O {self.modelo} já está parado.")

    def desligar(self):
        try:
            print(self.motor.desligar(self.velocidade))
        except Exception as e:
            print(f"Erro: {e}")
            
    def __str__(self):
        return f"""
Marca: {self.marca}
Modelo: {self.modelo}
Motor: {self.motor.tipo} {self.motor.potencia}
Placa: {self.placa}
Velocidade: {self.velocidade} km/h
"""

# Herança e Polimorfismo: Moto implementa a interface VeiculoMotorizado
class Moto(VeiculoMotorizado):
    def __init__(self, marca, modelo, motor, placa, velocidade = 0):
        super().__init__(motor,placa,velocidade,)
        self.marca = marca
        self.modelo = modelo
        
    def ligar_motor(self):
        print(self.motor.ligar())

    def acelerar(self):
        if self.motor.get_status() == "ligado":
            self.velocidade += self.motor.taxa_aceleracao
            self.motor.mover()
            print(f"O {self.modelo} acelerou para {self.velocidade} km/h.")
        else:
            raise Exception("Erro: A moto precisa estar ligada para acelerar.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            if self.velocidade <= 0:
                self.velocidade = 0
                self.motor.parar()
            print(f"O {self.modelo} reduziu a velocidade para {self.velocidade} km/h.")
        else:
            print(f"O {self.modelo} já está parado.")
        
    def desligar(self):
        try: 
            print(self.motor.desligar(self.velocidade))
        except Exception as e:
            print(f"Error: {e}")
            

    def __str__(self):
        return f"""
Marca: {self.marca}
Modelo: {self.modelo}
Motor: {self.motor.tipo} {self.motor.potencia}
Placa: {self.placa}
Velocidade: {self.velocidade} km/h
""" 
    
def testar_veiculo(veiculo):
    try:
        veiculo.ligar_motor()
        veiculo.acelerar()
        veiculo.acelerar()
        veiculo.frear()
        veiculo.desligar()
    except Exception as e:
        print(f"Houve um problema: {e}")
        


motor_carro = Motor("V8", "450cv", 20)
meu_carro = Carro("Ford", "Mustang", motor_carro, "ABC4312")

motor_moto = Motor("2T", "20cv", 12)
minha_moto = Moto("Honda", "CBR", motor_moto, "ABC23ADF")

print("-" * 20)
testar_veiculo(meu_carro)
print("-" * 20)
testar_veiculo(minha_moto)

# Exemplo de erro (acelerar sem ligar o motor)
print("-" * 20)

motor_carro2 = Motor("V12", "300cv", 0)
carro_quebrado = Carro("Fiat", "Uno", motor_carro2, "ADSDDSACD")
try:
    carro_quebrado.acelerar()
except Exception as e:
    print("Não foi possivel iniciar o carro")
    
    
    
print(str(meu_carro))
print(str(minha_moto))