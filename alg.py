def contar_algarismos(inicio, fim):
    total_algarismos = 0

    # Contar algarismos para números de inicio até fim
    for i in range(inicio, fim + 1):
        total_algarismos += len(str(i))

    return total_algarismos

# Solicitar ao usuário para inserir o intervalo de números
inicio = int(input("Informe o valor inicial do intervalo: "))
fim = int(input("Informe o valor final do intervalo: "))

# Chamando a função para contar os algarismos
total_algarismos = contar_algarismos(inicio, fim)

print(f"O número total de algarismos necessários para escrever todos os números de {inicio} até {fim} é: {total_algarismos}")
