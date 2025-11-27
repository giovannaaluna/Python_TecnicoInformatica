pessoas_operador = float(input("Quantidade de Operadores: "))
salario_operador = float(input("Sálario do cargo de Operador: "))
                         
pessoas_tecnico = float(input("Quantidade de Técnicos: "))
salario_tecnico = float(input("Sálario do cargo de Técnico: "))

pessoas_engenheiro = float(input("Quantidade de Engenheiros: "))
salario_engenheiro = float(input("Salário do cargo de Engenheiro: "))

media_ponderada = float((pessoas_operador * salario_operador + pessoas_tecnico * salario_tecnico + pessoas_engenheiro * salario_engenheiro) / 3)

print("\nA média ponderada é: R$",media_ponderada)

