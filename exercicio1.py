for i in range(2,22,2):
     print(i)
     print ("**********")


soma = 5 
for i in range (5,51,5):
    soma = soma + i 
    print(soma)

    
 pessoa = ["pessoa1,pessoa2,pessoa3,pessoa4,pessoa5"]
for pessoa in range(1,6):

    print('Pessoa', pessoa)


 

Lista_produtos = ["macarrão","feijão","uva","sal"]
lista_valores = [2.50,5.00,10.00,5.00]
print("escolha seus produtos")
print (Lista_produtos)

    
carrinho = [] 
meus_valores = []

produto1 = int(input('digite o seu produto'))
produto2 = int(input('digite o seu produto'))
produto3 = int(input('digite o seu produto'))

carrinho += (Lista_produtos[produto1],Lista_produtos[produto2],Lista_produtos[produto3])
meus_valores += (lista_valores[produto1],lista_valores[produto2],lista_valores[produto3],)

print ("seus produtos", carrinho)
print ("valores", meus_valores)
soma = sum(meus_valores)
print ('============TOTAl==========')
print ('R$$', soma)  

nome = input ('digite seu nome ')
cpf = input ('digite seu cpf')
email = input ('digite seu email ')
rg = input ('digite seu rg ')

dados = []

dados.extend ([nome,cpf,email,rg])
dado_imutavel = tuple(dados)
dado_imutavel.append('endereço x ')
print(dado_imutavel)


