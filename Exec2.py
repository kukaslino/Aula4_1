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
    limit_option = input("Digite 'L' para com limites ou 'S' para sem limites: ")
    command_string = input("Digite os comandos separados por ponto e vírgula (;): ")
    commands = command_string.split(';')
    position = 0

    for command in commands:
        command = command.strip()
        if command:
            if limit_option.upper() == 'L':
                position = execute_command_limited(command, position)
            elif limit_option.upper() == 'S':
                position = execute_command_unlimited(command, position)
            else:
                print("Opção inválida.")
                break

    print(f"Posição atual: {position}")

if __name__ == "__main__":
    main()