from abc import ABC, abstractmethod

class VeiculoMotorizado(ABC):
    def __init__(self, motor, placa, velocidade):
        self.motor = motor
        self.placa = placa
        self._velocidade = velocidade

    
    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

    def informacao(self):
        print(f'Motor: {self.motor.get_status()}')
        print(f"Placa: {self.placa}")
        print(f"Velocidade: {self.velocidade}km/h")


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__ligado = False

    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} está ligado"
    
    def get_status(self):
        if self.__ligado == True:
            return "Ligado"
        else:
            return "Desligado"
    
    def desligar(self):
        self.__ligado = False
        return f"Motor {self.tipo} está desligado"


class Carro(VeiculoMotorizado):
    def __init__(self, placa, velocidade, marca, modelo):
        self.motor = Motor("V8")
        super().__init__(self.motor, placa, velocidade) 
        self.marca = marca
        self.modelo = modelo
    
    @property
    def velocidade(self):
        return self._velocidade
    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 30:
            print("AVISO: Por favor, verifique se todos estão com os cintos de segurança")
        self._velocidade = valor

    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":

            return self.motor.ligar()
        elif self.velocidade != 0:
            return "O carro precisa estar parado para ligar o motor."
        else:
            return "Carro já está ligado."

    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            self.velocidade += 10
            return f"O {self.modelo} está acelerando em 10km. Velocidade atual: {self.velocidade}km/h"
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            return f"O carro diminuiu em 5km. Velocidade atual: {self.velocidade}km/h"
        else:
            return f"A velocidade do {self.modelo} já é zero"

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            return self.motor.desligar()
        else:
            return f"{self.modelo} precisa estar parado e ligado para ser desligado"

    def status(self):
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo}")
        if self.motor.get_status() == "Ligado":
            print("Seu carro está ligado")
        else:
            print("Seu carro está desligado")
        self.informacao()


class Moto(VeiculoMotorizado):

    def __init__(self, placa, velocidade, marca, modelo):
        self.motor = Motor("Tetracilíndrico")
        super().__init__(self.motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo

    @property #Gambiara para o codigo funcionar 
    def velocidade(self):
        return self._velocidade
    @velocidade.setter
    def velocidade(self, valor):
        '''if valor >= 50:
            print("AVISO: Por favor, verifique se todos estão com os cintos de segurança")'''
        self._velocidade = valor

    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":
            return self.motor.ligar()
        else:
            return "Moto já está ligado"
    
    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            self.velocidade += 10 
            return f"A moto está acelerando em 10km"
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5 
            return "A moto diminuiu em 5km"
        else:
            return f"A velocidade do {self.modelo} já é zero"

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            return self.motor.desligar()
        else:
            return f"{self.modelo} precisa estar parado e ligado para ser desligado"
            
    def status(self):
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo}")
        if self.motor.get_status() == "Ligado":
            print("Sua moto está ligada")
        else:
            print("Sua moto está desligada")
        self.informacao()

print("___Teste Carro___")
carro1 = Carro("XBV-4517", 0, "Ford", "Mustang")
carro1.ligar_motor()
carro1.acelerar()
carro1.informacao()
carro1.acelerar()
carro1.frear()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.informacao()

print("___Teste Moto___")
moto1 = Moto("LKJ-2136", 0, "Kawasaki", "Ninja ZX-10R")
moto1.ligar_motor()
moto1.acelerar()
moto1.informacao()
moto1.acelerar()
moto1.frear()
moto1.acelerar()
moto1.acelerar()
moto1.acelerar()
moto1.acelerar()
moto1.acelerar()
moto1.acelerar()
moto1.informacao()
