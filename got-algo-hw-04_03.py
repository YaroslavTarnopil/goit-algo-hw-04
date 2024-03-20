def handle_command(command):
    if command == 'hello':
        return 'How can I help you?'
    elif command == 'add username phone':
        return 'Contact added'
    elif command == 'change username phone':
        return 'username'
    elif command == 'Goodbye!':
        return 'Goodbye! If you need help, dont hesitate to reach out'
    else:
        return 'Goodbye! If you need help, dont hesitate to reach out'

# Головний цикл програми
while True:
    # Очікуємо введення команди від користувача
    command = input('Введіть команду: ')

    # Обробляємо команду та виводимо результат
    response = handle_command(command.lower())
    print(response)

    # Вихід з циклу, якщо користувач ввів "close"
    if command.lower() == 'close':
        break