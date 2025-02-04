import sys

def is_valid(value, input_type):
    value = value.strip().lower()
    if not value:
        return False
    if value[0] == '-':
        if len(value) == 1:
            return False
        num_part = value[1:]
    else:
        num_part = value
    if input_type == 'decimal':
        return num_part.isdigit()
    elif input_type == 'binary':
        return all(c in '01' for c in num_part) and len(num_part) > 0
    elif input_type == 'hex':
        try:
            int(num_part, 16)
            return True
        except ValueError:
            return False
    return False

def dec_to_bin(dec_str):
    dec = int(dec_str)
    if dec < 0:
        return '-' + bin(abs(dec))[2:]
    return bin(dec)[2:]

def bin_to_dec(bin_str):
    return str(int(bin_str, 2))

def dec_to_hex(dec_str):
    dec = int(dec_str)
    if dec < 0:
        return '-' + hex(abs(dec))[2:].upper()
    return hex(dec)[2:].upper()

def hex_to_dec(hex_str):
    return str(int(hex_str, 16))

def hex_to_bin(hex_str):
    dec = int(hex_str, 16)
    if dec < 0:
        return '-' + bin(abs(dec))[2:]
    return bin(dec)[2:]

def bin_to_hex(bin_str):
    dec = int(bin_str, 2)
    if dec < 0:
        return '-' + hex(abs(dec))[2:].upper()
    return hex(dec)[2:].upper()

def print_menu():
    print("\nSelect conversion type:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Hexadecimal to Binary")
    print("6. Binary to Hexadecimal")
    print("7. Exit")

def handle_conversion(choice):
    conversion_map = {
        '1': {'name': 'Decimal to Binary', 'input_type': 'decimal', 'func': dec_to_bin},
        '2': {'name': 'Binary to Decimal', 'input_type': 'binary', 'func': bin_to_dec},
        '3': {'name': 'Decimal to Hexadecimal', 'input_type': 'decimal', 'func': dec_to_hex},
        '4': {'name': 'Hexadecimal to Decimal', 'input_type': 'hex', 'func': hex_to_dec},
        '5': {'name': 'Hexadecimal to Binary', 'input_type': 'hex', 'func': hex_to_bin},
        '6': {'name': 'Binary to Hexadecimal', 'input_type': 'binary', 'func': bin_to_hex}
    }
    info = conversion_map[choice]
    print(f"\nSelected: {info['name']}")
    print("Enter 'back' to return to the main menu.")
    print("Enter 'exit' to quit the program.\n")
    while True:
        user_input = input(f"Enter {info['input_type']} value: ").strip().lower()
        if user_input == 'back':
            return
        if user_input == 'exit':
            sys.exit()
        if is_valid(user_input, info['input_type']):
            try:
                result = info['func'](user_input)
                print(f"Result: {result}\n")
            except:
                print("An error occurred during conversion.\n")
        else:
            print("Invalid input. Please try again.\n")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == '7':
            print("Exiting program. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            handle_conversion(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")

if __name__ == "__main__":
    main()