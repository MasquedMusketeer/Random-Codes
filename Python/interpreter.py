words = []
letters = []
processor = []
finalprocessing = []
decrypted = "Sua menssagem é:"
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specialstring = ['á','à','ã','â','é','ê','í','î','ó','ô','õ','ú','û','ç',',','.','!','?',' ']
counter = 0
keydiv = 0

numtot = int(input('Quantos números a menssagem codificada possue?: '))

while counter < numtot:
    values = int(input('Insira sua mensagem codificada: '))
    words.append(values)
    counter += 1

cryptkey = input('Insira sua chave: ')
cripkey = cryptkey
for x in cripkey:
    processing = list(x)
    for z in processing:
        processor.append(z)

for x in processor:
    f = processor.pop(0)
    if f in alphabet:
        z = alphabet.index(f)
    elif f in Alphabet:
        z = Alphabet.index(f)+100
    else:
        z = specialstring.index(f)+200
    processor.append(z+1)

for x in words:
    keydiv = 0
    num = words.pop(0)
    for z in processor:
        keydiv += z
    data = num/keydiv
    letters.append(data)
    words.append(num)

for x in letters:
    ver = x
    for z in alphabet:
        y = alphabet.index(z)
        if y == (ver - 1):
            letter1 = z
            finalprocessing.append(letter1)
    for z in Alphabet:
        y = Alphabet.index(z)
        if y == (ver - 101):
            letter1 = z
            finalprocessing.append(letter1)
    for z in specialstring:
        y = specialstring.index(z)
        if y == (ver - 201):
            letter1 = z
            finalprocessing.append(letter1)

for x in finalprocessing:
    decrypted += x

print(decrypted)