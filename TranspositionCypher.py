import math

def encrypt(mess, key):

    res = ''
    for index in range(key):
        while(index<len(mess)):
            res += mess[index]
            index += key
    return res

def decrypt(mess, key):
    res = ''
    a = int(math.ceil(len(mess)/key))
    k = a*key - len(mess)
    x = key - k
    b = a-1;
    for index in range(a-1):
        while index < len(mess):
            res += mess[index]
            index += a
            if index >= (x+1)*a:
                index -= 1
    while b < (x+1)*a-1:
        res += mess[b]
        b += a

    return res

def translate(mess, mode, key):
    if mode == 'Encrypt':
        return encrypt(mess, key)
    elif mode == 'Decrypt':
        return decrypt(mess, key)

mess = input('Enter the message')

mode = input('Encrypt or Decrypt')

while mode != 'Encrypt' and mode != 'Decrypt':
    print('Wrong mode!!! Choose again')
    mode = input('Encrypt or Decrypt')

key = int(input('Enter the key'))

print('Result:' + translate(mess, mode, key))
