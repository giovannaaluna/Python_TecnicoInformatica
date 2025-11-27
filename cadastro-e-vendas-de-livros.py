# Giovanna Freitas
# Lídia Beatriz
# Gabriella Hadassa

print("------------------------------------------------------------\n                        LIVRARIA\n------------------------------------------------------------")
print("\nSeja bem-vindo(a)!\n")

login = str(input("Login: "))
senha = str(input("Senha: "))

while (login != "estoque") or (senha != "1234"):

    print("\nLogin ou Senha inválidos.\n")

    login = str(input("Login: "))
    senha = str(input("Senha: "))

print("\n----------------------------------\n1 - Cadastro de Livros\n2 - Vender Livro\n3 - Sair\n----------------------------------\n")

opcao = int(input("Escolha uma opção: "))

while opcao != 3:
    match opcao:
        case 1:
            titulo = str(input("\nTítulo do Livro: "))
            autor = str(input("Autor: "))
            preco = float(input("Preço: "))
            inserir_estoque = int(input("Quantidade: "))
            data_cadastro = str(input("Data de Cadastro: "))

            print("\nTítulo do Livro: ",titulo,"\nAutor: ",autor,"\nPreço: R$",preco,"\nQuantidade: ",inserir_estoque,"\nData de Cadastro: ",data_cadastro)
        case 2: 
            titulo = str(input("\nTítulo do Livro: "))
            autor = str(input("Autor: "))
            pagamento = int(input("\nForma de Pagamento: \n1 - Dinhero\n2 - Crédito\n3 - Débito\n\nEscolha uma opção: "))
            match pagamento:
                case 1:
                    dinheiro = float(input("\nInsira o valor em dinheiro: "))
                    tirar_estoque = int(input("Quantidade: "))
                    print("\n----------------------------------\n        VENDA EFETUADA.\n----------------------------------")

                    print("\nTítulo do Livro: ",titulo,"\nAutor: ",autor,"\nPreço: R$",dinheiro,"\nQuantidade: ",tirar_estoque)
                case 2:
                    nome_titular = str(input("Nome completo do titular: "))
                    numero_cartao = float(input("Número do cartão: "))
                    validade_cartao = str(input("Data de Validade: "))
                    cvv = int(input("Código de segurança (CVV): "))
                    preco = float(input("Preço: "))
                    tirar_estoque = int(input("Quantidade: "))
                    data_venda = str(input("Data da Venda: "))
                    print("\n----------------------------------\n       VENDA EFETUADA.\n----------------------------------")
                    print("\nTítulo do Livro: ",titulo,"\nAutor: ",autor,"\nPreço: R$",preco,"\nQuantidade: ",tirar_estoque)
                case 3:
                    nome_titular = str(input("Nome completo do titular: "))
                    numero_cartao = float(input("Número do cartão: "))
                    validade_cartao = str(input("Data de Validade: "))
                    cvv = int(input("Código de segurança (CVV): "))
                    preco = float(input("Preço: "))
                    tirar_estoque = int(input("Quantidade: "))
                    data_venda = str(input("Data da Venda: "))
                    
                    print("\nVENDA EFETUADA.")

                    print("\nTítulo do Livro: ",titulo,"\nAutor: ",autor,"\nPreço: R$",preco,"\nQuantidade: ",tirar_estoque)

    print("\n----------------------------------\n1 - Cadastro de Livros\n2 - Vender Livro\n3 - Sair\n----------------------------------\n")

    opcao = int(input("Escolha uma opção: "))

print("\n----------------------------------\n       SISTEMA FINALIZADO.\n----------------------------------")


                            
