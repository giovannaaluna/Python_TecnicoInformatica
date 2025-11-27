login = str(input("Login: "))
senha = str(input("Senha: "))

while login != "medical" or senha != "2025":
    print("Login ou senha incorretos. Tente novamente.")
    login = str(input("Login: "))
    senha = str(input("Senha: "))

print("Acesso concedido.")

print("\n1 - Cadastro de paciente \n2 - Agendamento de consulta \n3 - Cancelamento de consulta \n4 - Solicitação de Exames")

opcao = int(input("\nEscolha uma opção: "))

match opcao:
    case 1:
        nome = str(input("Nome do Cliente: "))
        idade = int(input("Idade: "))
        plano_saude = str(input("Plano de Saúde ou Particular? "))

        print("\nNome do Cliente: ", nome , "\nIdade: ", idade , "\nPlano de Saúde ou Particular? ", plano_saude)
    case 2:
        nome = str(input("Nome do Cliente: "))
        especialidade = str(input("Especialidade: "))
        data_consulta = str(input("Data da Consulta: "))

        print("\nNome do Cliente: ", nome , "\nEspecialidade: ",especialidade,"\nData da consulta: ",data_consulta)
    case 3:
        print("\nDeseja cancelar a consulta? \n1 - Sim \n2 - Não")
        opcao_cancelar = int(input("\nEscolha uma opção: "))

        match opcao_cancelar:
            case 1:
                print("Consulta cancelada.")
            case 2:
                print("Atendimento finalizado.")
    case 4:
        nome = str(input("Nome do Cliente: "))
        tipo_exame = str(input("Tipo de exame: "))
        data_exame = str(input("Data do Exame: "))
        
        print("\nNome do Cliente",nome,"\nTipo de exame:",tipo_exame,"\nData do Exame: ",data_exame)
        




