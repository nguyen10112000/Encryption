
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def cypher(mess, mode, key):
    res = ''
    for symbol in mess:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            if mode == 'Encrypt':
                symbolIndex += key
                if symbolIndex >= len(SYMBOLS):
                    symbolIndex -= len(SYMBOLS)
                res += SYMBOLS[symbolIndex]
            elif mode == 'Decrypt':
                symbolIndex -= key
                if symbolIndex < 0:
                    symbolIndex += len(SYMBOLS)
                res += SYMBOLS[symbolIndex]
        else:
            res += symbol

    return res

mess = input('Enter your message')


mode = input('Encrypt or Decrypt')
while mode != 'Encrypt' and mode != 'Decrypt':
    print('Wrong mode!!! Choose again')
    mode = input('Encrypt or Decrypt')

key = int(input('Enter the key'))

print('Result:' + cypher(mess, mode, key))

