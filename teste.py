from cliente import Cliente
from conta import Conta
from datas import Data

vini = Cliente("Vinicius")  # cria classe Cliente
print(vini.nome)  # imprime usando o @property
vini.nome = "Vini"  # muda o valor usando o @setter
print(vini.nome)  # imprime novamente via @property
print("-----------------------------------")

conta1 = Conta(123, "Panai", 100.0, 1000.0)
print(f'O limite da conta da {conta1.titular} é de {conta1.limite} com saldo atual de {conta1.saldo}')
print("-----------------------------------")

conta1.extrato()  # função extrato
print("-----------------------------------")

conta1.deposita(200.0)  # usando função deposita
conta1.extrato()
print("-----------------------------------")

conta1.saca(20.0)  # usando função saca
conta1.extrato()
print("-----------------------------------")

data = Data(1, 1, 2021)
data.formatada()  # função para formatar a data em dd/mm/aaaa, esse último tem que ser inserido os 4 dígitos ;_;
nova_data = Data(15, 3, 1989)
nova_data.formatada()
print("-----------------------------------")
