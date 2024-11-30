usuario = {
'nome' :str (input ("digite seu nome")),
'idade' :int (input ("digite sua idade")),
'cidade' : str (input ('Digite o nome da sua cidade')),
'email':str (input("digite seu email"))
}
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

Formaspagamento = ['debito', 'credito', 'pix']
escolhapagamento = int (input("escolha a forma de pagamento"))
print ("forma de pagamento" , Formaspagamento[escolhapagamento])
#print (usuario,"escolheu pagar o valor de " ,soma,"na opção de pagamento seguinte", Formaspagamento)
