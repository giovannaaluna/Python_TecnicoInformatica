tarefas = []

comandos = ["Adicionar", "Ver", "Remover", "Sair"]

print("""
------------------------------------
       GERENCIADOR DE TAREFAS
------------------------------------""")

while True: 
    for i,item_comandos in enumerate(comandos):
        print(f"{i + 1} - {item_comandos}")
    opcao = int(input("\n--> ")) 

    match opcao:
        case 1:
            #Adicionar
            adicionar = str(input("\nAdicionar tarefa: "))
            tarefas.append(adicionar)
            print("\nTarefa adicionada.\n")
        case 2:
            #Ver
            print("\nLista de Tarefas: ")
            if not tarefas:
                print("\nSem Tarefas\n")
                continue
            for i, ver_tarefas in enumerate(tarefas):
                print(f"{i + 1} - {ver_tarefas}")
            print(" ")
            
        case 3:
            #Remover
            print("\nLista de Tarefas: ")
            if not tarefas:
                print("Sem Tarefas\n")
                continue
            for i, ver_tarefas in enumerate(tarefas):
                print(f"{i + 1} - {ver_tarefas}")

            remover_tarefa = int(input("\nQual tarefa você deseja remover?\n-->"))    
          
            tarefa_removida = tarefas.pop(remover_tarefa - 1)
            print(f"\nTarefa {tarefa_removida} foi removida com sucesso.\n")
        case 4:
            #Sair
            print("Programa encerrado.")
            break
    