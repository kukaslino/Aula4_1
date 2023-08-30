def execute_command_limited(command, position):
    if command == "Direita":
        position = min(position + 1, 10)
    elif command == "Esquerda":
        position = max(position - 1, -2)
    else:
        print(f"Comando desconhecido: {command}")
    return position

def execute_command_unlimited(command, position):
    if command == "Direita":
        position += 1
    elif command == "Esquerda":
        position -= 1
    else:
        print(f"Comando desconhecido: {command}")
    return position

def main():
    limit_option = input("Digite 'L' para limites ou 'S' para sem limites: ")
    position = int(input("Digite a posição inicial: "))
    
    if limit_option.upper() != 'L' and limit_option.upper() != 'S':
        print("Opção inválida. Saindo.")
        return

    command_string = input("Digite a lista de comandos separados por espaço (máximo 30 comandos): ")
    commands = command_string.split()[:30] 

    for command in commands:
        if limit_option.upper() == 'L':
            position = execute_command_limited(command, position)
        elif limit_option.upper() == 'S':
            position = execute_command_unlimited(command, position)

    print(f"Posição atual: {position}")

if __name__ == "__main__":
    main()
