# Frukter och färg!  Färg-->Frukt

# kom ihåg nu att en färg kan ha många frukter! d.v.s. färg --> lista med frukter
avbildning_färg_till_frukt = {}


while True: 
    # 
    färg_och_frukt = input('Skriv in färg och frukt med ett mellanslag mellan dessa: ').lower().split()
    # Om vi vill avsluta programmet!
    if färg_och_frukt[0] == 'q': break

    färg = färg_och_frukt[0]
    frukt = färg_och_frukt[1]
    
    # Färgen finns redan som nyckel
    if färg in avbildning_färg_till_frukt.keys():
        if frukt in avbildning_färg_till_frukt[färg]:
            print('Frukten finns redan!')            
        else:
            avbildning_färg_till_frukt[färg].append(frukt)
    
    # Färgen finns inte som nyckel        
    else:
        avbildning_färg_till_frukt[färg] = []
        avbildning_färg_till_frukt[färg].append(frukt)

print(avbildning_färg_till_frukt)

for färg, lista_med_frukter in avbildning_färg_till_frukt.items():
    print(f'{färg}:')
    for frukt in lista_med_frukter:
        print(f'\t{frukt}')