# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# idade = 20
# dinheiro = 1.5
# nome = "leonardo"
# idade2 = "10"
# print()


# lista_vazia = []
# lista1 = [1,6,9,1]
# print(lista1[0])
# lista1.append(8)
# print(lista1)
# lista1[0] = 7
# print(lista1)
# del lista1[0]
# print(lista1)

# cores = {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00'}
# print(cores)
# print(cores['vermelho'])
# cores['amarelo'] = '#FFFF00'
# print(cores['amarelo'])
# print(cores)
# cores['vermelho'] = '#6b0000'
# print(cores)
#
# print(cores['amarelo'])
# del cores['amarelo']
# print(cores)

# def multiplicar_por_dois(x,y):
#     return (str(x*2),str(y*2))
# funcao = multiplicar_por_dois(5,9)
# print(funcao)
#
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print(numero)
#
# cores = {'vermelho': '#FF0000', 'azul': '#0000FF', 'verde': '#00FF00'}
#
# for key, value in cores.items():
#     print(key + ': ' + value)
#
# counter = 0
# while counter<= 10:
#     print(counter)
#     counter = counter + 1
#
# numero = -6
# if numero > 0:
#     print('O número é positivo')
# else:
#     print('O número é zero')

class Cachorro:
     tipo = "Yorkshire"

     def __init__(self,nome,idade,latido):
         self.nome = nome
         self.idade = idade
         self.latido = latido
     def latir(self):
        print(self.nome,"está latindo :",self.latido)

     def print_nome(self):
        print("nome" +"= " +self.nome)

cachorro1 = Cachorro("Bob", 17,"Au Au")
print(cachorro1.nome)
print(cachorro1.idade)
cachorro1.nome = "Micheal"
print(cachorro1.nome)
print(cachorro1.tipo)
print(cachorro1.latir())
print(cachorro1.print_nome())

class Cachorro_Grande(Cachorro):
    def latir(self):
        self.latido = (self.latido+" ALTO")
        print((self.nome+ " está latindo :" + self.latido))

    def print_nome(self):
        print("nome do cachorro grande " + "= " + self.nome)


cachorro2 = Cachorro_Grande("Big Bob",22,"AU AU")
print(cachorro2.nome)
print(cachorro2.latido)
print(cachorro2.idade)
print(cachorro2.latir())
print(cachorro2.print_nome())
