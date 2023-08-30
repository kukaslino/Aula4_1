def execute_command(command, position):
    if command == "Direita":
        position += 1
    elif command == "Esquerda":
        position -= 1
    return position

def main():
    command_string = input("Digite os comandos separados por ponto e vírgula (;): ")
    commands = command_string.split(';')
    position = 0

    for command in commands:
        command = command.strip()
        if command:
            position = execute_command(command, position)
            
    print(f"Posição atual: {position}")

if __name__ == "__main__":
    main()