# Sabor Python

#Giovanna Freitas

#registrar os pedidos de seus clientes
#calcular o total da conta e mostrar resumo

print("""
---------------------------------------------------
                  - SABOR PYTHON -
---------------------------------------------------""")


print("""
---------------------------------------------------
                     CARDÁPIO
--------------------------------------------------- 
       PRATOS                  BEBIDAS
      
1 - Cuzcuz - R$14        4 - Água 500ml - R$8
2 - Hambúrguer - R$18    5 - Coca-Cola 2,5L - R$15  
3 - Salada - R$10        6 - Suco de Uva - R$13
---------------------------------------------------""")

codigos_cardapio = [1, 2, 3, 4, 5, 6]

pedido = int(input("""
Deseja realizar algum pedido?
                   
1 - Sim
2 - Não

Escolha uma opção: """))

pedido_prato = []
pedido_bebida = []
valor = []

while pedido != 2:

    codigo_pedido = int(input("\nDigite o Código do seu Prato ou Bebida, um por vez: "))
    match codigo_pedido:
        case 1:
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                pedido_prato.append("Cuzcuz")
                valor.append(14)
        case 2:
           quantidade = int(input("Quantidade: "))
           for i in range(quantidade):
                pedido_prato.append("Hambúrguer") 
                valor.append(18) 
        case 3:
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                pedido_prato.append("Salada")
                valor.append(10)
        case 4:
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                pedido_bebida.append("Água")
                valor.append(8)
        case 5:
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                pedido_bebida.append("Cola-Cola")
                valor.append(15)
        case 6:
            quantidade = int(input("Quantidade: "))
            for i in range(quantidade):
                pedido_bebida.append("Suco de Uva")
                valor.append(13)
    
    pedido = int(input("""
Deseja realizar alguma coisa?
                    
1 - Sim
2 - Finalizar Pedido

Escolha uma opção: """))
    
import os
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
pagamento = int(input("""
Qual a forma de pagamento? 
                      
1 - Débito
2 - Crédido
3 - Pix
                      
Escolha uma opção: """))

match pagamento:
    case 1:
        titular_cartao = str(input("Nome do Titular do Cartão: "))
        numero_cartao = int(input("Numéro do Cartão: "))
        cvv = int(input("CVV: "))
    case 2:
        titular_cartao = str(input("Nome do Titular do Cartão: "))
        numero_cartao = float(input("Número do Cartão: "))
        cvv = int(input("CVV: "))
    case 3:
        print("""
Copiar Pix:
saborpython@gmail.com""")

print("""
PAGAMENTO APROVADO
""")

print(f"""
--------------------------------------
            SABOR PYTHON
             NOTA FISCAL
--------------------------------------    
""")

for pratos in pedido_prato:
    print(pratos)
for bebida in pedido_bebida:
    print(bebida)

total = sum(valor)

print("\nValores: ",*valor)
print("Valor total: ",total)
   
print("""
--------------------------------------
            SABOR PYTHON
            Volte Sempre!
--------------------------------------""")


        

    




            


