from abc import ABC, abstractmethod

class VeiculoMotorizado(ABC):
    def __init__(self, motor, placa, velocidade):
        self.motor = motor
        self.placa = placa
        self. velocidade = velocidade
    
    @abstractmethod
    def ligar_motor(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass
    @property
    def velocidade(self):
        return self.__velocidade
    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 30:
            print("AVISO: Por favor, verifique se todos estão com os cintos de segurança")
        self.__velocidade = valor

    def informacao(self):
        print(f'Motor: {self.motor}')
        print(f"Placa: {self.placa}")
        print(f"Velocidade: {self.velocidade}")

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
    def __init__(self, motor, placa, velocidade, marca, modelo):
        super().__init__(motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo


    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":
            self.motor.ligar()
        else:
            return "Carro já está ligado"

    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            self.velocidade += 10
            print(f"O {self.modelo} está acelerando em 10km")
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("O carro diminuiu em 5km")
        else:
            print(f"A velocidade do {self.modelo} já é zero")

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            self.motor.desligar()
        else:
            print(f"{self.modelo} precisa estar parado e ligado para ser desligado")

    '''def segurança(self):
        if self.velocidade >= 30:
            print("Por favor, verifique se todos estão com os cinto de segurança")'''
    
    def status(self):
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo}")
        if self.motor.get_status() == "Ligado":
            print("Seu carro está ligado")
        else:
            print("Seu carro está desligado")
        self.informacao()


class Moto(VeiculoMotorizado):
    def __init__(self, motor, placa, velocidade, marca, modelo):
        super().__init__(motor, placa, velocidade)
        self.marca = marca
        self.modelo = modelo


    def ligar_motor(self):
        if self.velocidade == 0 and self.motor.get_status() == "Desligado":
            self.motor.ligar()
        else:
            return "Moto já está ligado"
    
    def acelerar(self):
        if self.motor.get_status() == "Ligado":
            self.velocidade += 10
            return f"O {self.modelo} está acelerando"
        else:
            raise Exception("Erro: O motor precisa estar ligado para acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("A moto diminuiu em 5km")
        else:
            print(f"A velocidade do {self.modelo} já é zero")

    def desligar(self):
        if self.velocidade == 0 and self.motor.get_status() == "Ligado":
            self.motor.desligar()
        else:
            print(f"{self.modelo} precisa estar parado e ligado para ser desligado")
    def status(self):
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo}")
        if self.motor.get_status() == "Ligado":
            print("Sua moto está ligada")
        else:
            print("Sua moto está desligada")
        self.informacao()

    
carro1 = Carro()
carro1.ligar_motor()
carro1.acelerar()
carro1.informacao()
carro1.acelerar()
carro1.frear()
carro1.informacao()