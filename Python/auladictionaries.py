mydict = {
    "n1":5,
    "n2":10,
    "soma":"",
    "subt":"",
    "numeroMaior":""
}

for t in mydict.keys():
    if t == 'soma':
        mydict[t] = mydict['n1'] + mydict['n2']
    elif t == 'subt':
        mydict[t] = mydict['n1'] - mydict['n2']
    elif t == 'numeroMaior':
        mydict[t] = mydict['n1'] if mydict['n1'] > mydict['n2'] else mydict['n2']

print(mydict)