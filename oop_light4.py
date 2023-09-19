from oop_ligth3 import Cykel,Bil,Moped,Traktor

# Skapar några cykel-objekt!
c1 = Cykel('Blå', 'tvåhjuling')
c2 = Cykel('Grön', 'tvåhjuling')
c3 = Cykel('Svart', 'trehjuling')
# Skapar några Bil-objekt
b1 = Bil('Blå', 2010, 200)
b2 = Bil('Röd', 1995, 120)
b3 = Bil('Lila', 2021, 180)
# Skapar några Moped-objekt
m1 = Moped('Vit', 'flakmoped', 12)
m2 = Moped('Svart', 'vespa', 5)
m3 = Moped('Grön', 'EU-moped', 3)
# Skapar några Traktorer-objekt
t1 = Traktor('Grön', 1930, 9)
t2 = Traktor('Röd', 1990, 25)
t3 = Traktor('Svart', 2020, 70)

lista_med_objekt = [c1,c2,c3,b1,b2,b3,m1,m2,m3,t1,t2,t3]

# Testa anropa några metoder
# print(f'{c1.get_färg()=} och {c1.get_typ()=}')
print(20*'-')
for objekt in lista_med_objekt:
    print(f'{objekt.__class__} och har färgen: {objekt.get_färg()}')
print(20*'-')
for objekt in lista_med_objekt:
    objekt.set_färg('Svart')

for objekt in lista_med_objekt:
    print(f'{objekt.__class__} och har färgen: {objekt.get_färg()}')
print(20*'-')

