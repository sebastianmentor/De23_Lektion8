import random
my_dict = {}

for _ in range(3):
    namn = input("Skriv ditt namn: ")
    lösen = input("Skriv ditt lösen")
    slump = random.randint(1000,9999)
    my_dict[namn]= {
        'kontonummer':slump,
        'lösen':lösen
    }

# print(my_dict)
# print(f'{type(my_dict[namn])}')
for namn, konton_dict in my_dict.items():
    print(f'{namn} är kopplat till en dictionary som innenhåller kontouppgifter!')
    print(f'{konton_dict["kontonummer"]=}')
    print(f'{konton_dict["lösen"]=}')
