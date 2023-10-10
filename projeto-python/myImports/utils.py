def validarInt(value):
    while True:
        try:
            int(value)
            break
        except Exception:
            value = input('Digite um valor válido: ')
            continue
    return int(value)

def validarFloat(value):
    while True:
        try:
            float(value)
            break
        except Exception:
            value = input('Digite um valor válido: ')
            continue
    return float(value)

def criarMenu(text):
    print('-'*42)
    print(f'{text:^40}')
    print('-' * 42)
