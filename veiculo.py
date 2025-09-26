from abc import ABC,abstractmethod
class VeiculMotorizado(ABC):
    def __init__(self,motor,placa,velocidade = 0):
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
    def desligar_motor(self):
        pass

class Motor:
    def __init__(self,tipo,potencia = 'Não Informada',taxa_aceleração = 10):
        self.tipo = tipo
        self.__ligado = False
        self.potencia = potencia
        self.taxa_aceleracao = taxa_aceleração

    def ligar(self):
        self.__ligado = True
        return (f'Motor {self.tipo} está ligado.')
    def get_status(self):
        return 'ligado' if self.__ligado else 'desligado'
    def desligar(self):
        self.__ligado = False
        return 'desligado' if not self.__ligado else 'ligado'
class Carro(VeiculMotorizado):
    def __init__(self,marca,modelo,placa):
        self.marca = marca
        self.modelo = modelo
        motor_do_carro = Motor('V8','450cv',20)
        super().__init__(motor_do_carro,placa)
        self.aviso_cinto = False

    def ligar_motor(self):
        print(self.motor.ligar())
        print(f' O {self.modelo} está ligado!')

    def acelerar(self):
        if self.motor.get_status() == 'ligado':
            self.velocidade += self.motor.taxa_aceleracao
            print(f'O {self.modelo} está acelerando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: O motor precisa estar ligado para acelerar')
        if self.velocidade >=30 and self.aviso_cinto == False:
            self.aviso_cinto = True
            print('Colocar o cinto de segurança')

    def frear(self):
        if self.motor.get_status() == 'ligado' and self.velocidade > 0:
            self.velocidade -= 10
            print(f'O {self.modelo} está freando!')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: A velocidade precisa ser maior que 0 para frear!')
        if self.velocidade < 30 and self.aviso_cinto:
            self.aviso_cinto = False
    def desligar_motor(self):
        if self.velocidade > 0:
            print(f'A velocidade precisa ser reduzida para poder ser desligado. Velocidade atual: {self.velocidade} km/h')
        elif self.motor.get_status() == 'desligado':
            print(f'O {self.modelo} já está desligado!')
        else:
            self.motor.desligar()
            print(f' O {self.modelo} foi desligado com sucesso!')

    def __str__(self):
        return f'''
------------
Veiculo: {self.marca} {self.modelo}
Placa: {self.placa}
Velocidade:{self.velocidade} km/h
Motor: {self.motor.tipo} {self.motor.potencia} 
-------- '''
class Moto(VeiculMotorizado):
    def __init__(self,marca,modelo,placa):
        self.marca = marca
        self.modelo = modelo
        motor_da_moto = Motor('250cc','20cv',12)
        super().__init__(motor_da_moto,placa)

    def ligar_motor(self):
        print(self.motor.ligar())
        print(f'A {self.modelo} (placa: {self.placa}) está ligada!')

    def acelerar(self):
        if self.motor.get_status() == 'ligado':
            self.velocidade += self.motor.taxa_aceleração
            print(f'A {self.modelo} está acelerando na pista')
            print(f'Velocidade atual: {self.velocidade} km/h')
        else:
            raise Exception('Erro: A moto precisa estár ligada para acelerar')

    def frear(self):
        if self.motor.get_status() == 'ligado' and self.velocidade >0:
            self.velocidade -= 5
            print(f'A {self.modelo} está freando!')
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

    def __str__(self):
        return f'''
------------
Veiculo: {self.marca} {self.modelo}
Placa: {self.placa}
Velocidade:{self.velocidade} km/h
Motor: {self.motor.tipo} {self.motor.potencia} 
 -------- '''
def testar_veiculo(veiculo):
    try:
        veiculo.ligar_motor()
        veiculo.acelerar()
        veiculo.acelerar()
        veiculo.frear()
        veiculo.frear()
        veiculo.acelerar()
        veiculo.acelerar()
        veiculo.desligar_motor()
    except Exception as e:
        print(f'Houve um problema: {e}')

meu_carro = Carro('Ford','Mustang','ABD1C24',)
minha_moto = Moto('Honda','CBR','ABE1F23')

testar_veiculo(meu_carro)
print('-'*20)
testar_veiculo(minha_moto)

print('-'*20)
carro_quebrado = Carro('Fiat', 'Uno','adasas')
try:
    carro_quebrado.ligar_motor()
    carro_quebrado.desligar_motor()
    carro_quebrado.acelerar()
except Exception as e:
    print(e)

print(meu_carro)
print(minha_moto)