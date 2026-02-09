from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupaca
from conta_Ivestimento import ContaInvestimetno

conta1 = ContaInvestimetno(123,'isaias',1200)
conta2 = ContaPoupaca(321,'isaias',1200)
conta3 = ContaCorrente(213,'isaias',1200)

conta1.sacar(1100)
conta2.sacar(1100)
conta3.sacar(1100)

print(vars(conta1))
print(vars(conta2))
print(vars(conta3))


