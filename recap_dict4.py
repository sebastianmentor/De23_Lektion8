avbildning_djur_till_lätten = {'ko':'muuu',
                               'hund': 'voff',
                               'katt': 'mjao'}



while True:
    djur = input('Skriv in ett djur: ')
    if djur == 'q': break

    if djur in avbildning_djur_till_lätten.keys():
        lätte = avbildning_djur_till_lätten(djur)
        print(f'{djur} säger {lätte}')
    else:
        print(f'Jag vet inte hur djuret {djur} låter!!')