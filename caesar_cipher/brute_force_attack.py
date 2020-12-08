message = 'XasrMrrSrirVsa'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(letters)):
    translated = ''

    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol) - key
            if num < 0:
                num = num + len(letters)
            translated = translated + letters[num]
            # print(f'symbol in letters: {symbol}')
            # print(f'key: {key}, num: {letters.find(symbol)}')
        else:
            translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))