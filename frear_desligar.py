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
    def __init__(self, motor,velocidade = 0):
        if not isinstance(motor, Motor):
            raise TypeError("Um veículo deve ter um objeto do tipo Motor.")
        self.motor = motor
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
    def desligar_motor(self):
        pass


# Composição: A classe Motor é parte da classe Veiculo
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__ligado = False  # Atributo privado

    def ligar(self):
        self.__ligado = True
        return f"Motor {self.tipo} ligado."

    def get_status(self):
        return "ligado" if self.__ligado else "desligado"
    def desligar(self):
        self.__ligado = False
        return 'desligado' if not self.__ligado else 'ligado'

# Herança e Polimorfismo: Carro implementa a interface VeiculoMotorizado
class Carro(VeiculoMotorizado):
    def __init__(self, marca, modelo, motor):
        super().__init__(motor)
        self.marca = marca
        self.modelo = modelo
        # Composição: O objeto Motor é criado dentro do Carro

    def ligar_motor(self):
        # Encapsulamento: Acessando o método do objeto Motor
        print(self.motor.ligar())

    def acelerar(self):
        if self.motor.get_status() == 'ligado':
            self.velocidade += 15
            print(f'O {self.modelo} está acelerando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: O motor precisa estar ligado para acelerar')

    def frear(self):
        if self.motor.get_status() == 'ligado' and self.velocidade > 0:
            self.velocidade -= 15
            print(f'O {self.modelo} está freando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: A velocidade precisa ser maior que 0 para frear!')

    def desligar_motor(self):
        if self.velocidade > 0:
            print(
                f'A velocidade precisa ser reduzida para poder ser desligado. Velocidade atual: {self.velocidade} km/h')
        elif self.motor.get_status() == 'desligado':
            print(f'O {self.modelo} já está desligado!')
        else:
            self.motor.desligar()
            print(f' O {self.modelo} foi desligado com sucesso!')


# Herança e Polimorfismo: Moto implementa a interface VeiculoMotorizado
class Moto(VeiculoMotorizado):
    def __init__(self, marca, modelo, motor):
        super().__init__(motor)
        self.marca = marca
        self.modelo = modelo

    def ligar_motor(self):
        print(self.motor.ligar())


    def acelerar(self):
        if self.motor.get_status() == 'ligado':
            self.velocidade += 15
            print(f'O {self.modelo} está acelerando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: O motor precisa estar ligado para acelerar')


    def frear(self):
        if self.motor.get_status() == 'ligado' and self.velocidade > 0:
            self.velocidade -= 15
            print(f'O {self.modelo} está freando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: A velocidade precisa ser maior que 0 para frear!')


    def desligar_motor(self):
        if self.velocidade > 0:
            print(f'A velocidade precisa ser reduzida para poder ser desligado. Velocidade atual: {self.velocidade} km/h')
        elif self.motor.get_status() == 'desligado':
            print(f'O {self.modelo} já está desligado!')
        else:
            self.motor.desligar()
            print(f' O {self.modelo} foi desligado com sucesso!')

    # Função que usa polimorfismo


def testar_veiculo(veiculo):
    try:
        veiculo.ligar_motor()
        veiculo.acelerar()
        veiculo.frear()
        veiculo.desligar_motor()
    except Exception as e:
        print(f"Houve um problema: {e}")


# exemplo de uso

# criando motores

motor_gasolina = Motor(tipo="Gasolina")
motor_flex = Motor(tipo="Flex")
motor_eletrico = Motor(tipo="Elétrico")
motor_hibrido = Motor(tipo="Híbrido")

# criando veículos
minha_moto_eletrica = Moto(motor=motor_eletrico, marca="Yamaha", modelo="Neos")
meu_carro_eletrico = Carro(motor=motor_eletrico, marca="Volvo", modelo="EX30")
meu_carro_hibrido = Carro(motor=motor_hibrido, marca="Haval", modelo="GWM")
meu_carro_gasolina = Carro(motor=motor_gasolina, marca="Renault", modelo="Duster")
meu_carro_flex = Carro(motor=motor_flex, marca="Toyota", modelo="Corola")

# se não instanciar Motor haverá erro
# meu_carro_flex2 = Carro(marca="Toyota", modelo="Corola")

testar_veiculo(minha_moto_eletrica)
testar_veiculo(meu_carro_flex)
"""
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
"""