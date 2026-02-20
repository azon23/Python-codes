

def to_binary(decimal):
    bits = 32
    binary = ''
    for n in range(bits-1, -1, -1):
        if decimal // 2**n == 1:
            binary += '1'
            decimal -= 2**n
        else:
            binary += '0'

    print(binary)

def to_decimal(binary):
    binary_len = len(str(binary))
    reversed_binary = str(binary)[::-1]
    decimal = 0
    for n in range(binary_len-1, -1, -1):
        decimal += int(reversed_binary[n])*2**n

    print(decimal)

# présentation
print('Que voulez-vous trouver ?')
while True:
    choice = input('1: Binaire | 2 : Decimal : ')
    entry = int(input('Entrez le nombre : '))
    if choice == '1':
        to_binary(entry)
    elif choice == '2':
        to_decimal(entry)
    elif choice == 'exit' or choice == 'quit':
        break
    else:
        print('\nNon pris en charge. Entrez un numéro correct !')
        print('\n--------------------------------------------')
        continue
