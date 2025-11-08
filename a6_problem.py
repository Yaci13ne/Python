capitale_pays ={'Algerie':'Alger','France':'Paris','Espagne':'Madrid','Portugal':'Lisbonne',"Japon": "Tokyo"}

print(capitale_pays['Algerie'])
capitale_italie = capitale_pays.get('Italie','Rome')
capitale_pays['Marroque']='Rabat'

capitale_pays['Japon']='Kyoto'
del capitale_pays['France']

for pays,capitale in capitale_pays.items():
    print(f'La capitale de {pays} est {capitale}')