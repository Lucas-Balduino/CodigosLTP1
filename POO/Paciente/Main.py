from PacienteClass import Paciente

paciente1 = Paciente('Lucas', 19, '12345678901')

paciente1.nome = 'Rodrigo'
print(paciente1.nome)

paciente1._idade = 30
print(paciente1._idade)

# paciente1.__cpf = '1231231231232' - Cria um novo atributocom o mesmo nome para poder alterar, o __cpf nao foi alterado, '__' previne a alteracao
#print(paciente1.__cpf) - Error
#print(paciente1._Paciente__cpf) - Forma de acessar o Atributo privado(Errado)

paciente1.setIdade(20)
print(paciente1.getIdade())

print(paciente1.cpf)
paciente1.cpf = '123123123123' #Utilizado como Setter
print(paciente1.cpf) #Utilizado como Getter