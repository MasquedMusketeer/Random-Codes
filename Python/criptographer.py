singleword = []
cryptprocess = []
cryptmessage = []
processnum = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specialstring = ['á','à','ã','â','é','ê','í','î','ó','ô','õ','ú','û','ç',',','.','!','?',' ']

message = input('Insira sua mensagem: ')
usrinput = list(message)

for x in usrinput:
    singleword.append(x)
cryptkey = input('Insira sua chave: ')
cripkey = cryptkey
for x in cripkey:
    processing = list(x)
    for z in processing:
        cryptprocess.append(z)

for x in singleword:
    f = singleword.pop(0)
    if f in alphabet:
        z = alphabet.index(f)
    elif f in Alphabet:
        z = Alphabet.index(f)+100
    else:
        z = specialstring.index(f)+200
    singleword.append(z+1)

for x in cryptprocess:
    f = cryptprocess.pop(0)
    if f in alphabet:
        z = alphabet.index(f)
    elif f in Alphabet:
        z = Alphabet.index(f)+100
    else:
        z = specialstring.index(f)+200
    cryptprocess.append(z+1)

for x in singleword:
    processnum = 0
    num = singleword.pop(0)
    for z in cryptprocess:
        data = num*z
        processnum += data
    cryptmessage.append(processnum)
    singleword.append(num)

print("output: ", cryptmessage)