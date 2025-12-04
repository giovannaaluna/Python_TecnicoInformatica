


# Lista de serviços disponíveis

servicos = ["Reconhecimento de Firma", "Autenticação de Documentos", "Emissão de Certidão", "Procuração"]
print("=== Bem-vindo ao Sistema de Triagem de Atendimento Cartório ===\n")
while True:
    print("\nServiços Disponíveis:")
    # Loop para exibir os serviços numerados
    for i, servico in enumerate(servicos):
        print(f"{i + 1} - {servico}")
        print("5 - Sair/Encerrar")
        escolha = input("\nDigite o número do serviço desejado: ")


    match escolha: 
        case '1':
            print("⏳ Serviço: Reconhecimento de Firma. Tempo de Espera: 15 minutos. Dirija-se ao Guichê 1.")
        case '2':
            print("⏳ Serviço: Autenticação de Documentos. Tempo de Espera: 10 minutos. Dirija-se ao Guichê 2.")
        case '3':
            print("⏳ Serviço: Emissão de Certidão. Tempo de Espera: 20 minutos. Dirija-se ao Guichê 3.")
        case '4':
            print("⏳ Serviço: Procuração. Tempo de Espera: 30 minutos. Dirija-se ao Guichê 4.")
        case '5':
            break 
        case _: 
            print("⚠️ Opção inválida. Por favor, digite um número de 1 a 5.")
            print("\nObrigado por utilizar o sistema. Volte sempre!")
        
if escolha == '1':
    print("\nTeste de condição - esta linha nunca será exibida sem a correção do erro.")
else:
    print("Este é o segundo erro de sintaxe - falta de dois-pontos")


