from enum import Enum

class Veckodag(Enum):
    MÅNDAG = 1
    TISDAG = 2
    ONSDAG = 3
    TORSDAG = 4
    FREDAG = 5
    LÖRDAG = 6
    SÖNDAG = 7

# Användning:
print(Veckodag.MÅNDAG)     # Veckodag.MÅNDAG
print(Veckodag.MÅNDAG.name)  # MÅNDAG
print(Veckodag.MÅNDAG.value) # 1

dag = Veckodag.MÅNDAG

if dag == Veckodag.MÅNDAG:
    print("Det är måndag!")

tisdag = Veckodag(2)
fake_tisdag = Veckodag.MÅNDAG

if tisdag == fake_tisdag:
    print('Äkta tisdag!')
else: 
    print('DU ÄR FAKE!!!')