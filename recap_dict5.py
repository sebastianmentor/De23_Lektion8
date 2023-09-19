# 3. Dictionary

# Skriv en bankapplikation. Skriv först en meny med följande val:  
# Skapa konto
# Ta bort konto
# Lista alla kontonummer
# Lista totalsaldo
# Lista alla kontonummer och saldo

# Felhantering behöver du inte bry dig om i steg 1
konto_saldo_dictionary = {}

def lista_kontonummer_och_saldo():
    # loopa igenom nyckel och värde par och skriva ut dem snyggt med f-string 
    pass

def lista_totalsaldo():
    # loopa igenom alla värden och summera dem
    pass

def lista_alla_kontonummer():
    # Loopa igenom alla nycklar
    pass

def ta_bort_konto():
    # kolla om kontot finns
    # Om det finns, ta bort från dictionary
    # Annars, felmeddelande
    pass

def skapa_konto():
    # Ta in ett kontonummer från användaren! 
    # Därefter lägga till kontonummer plus saldo 0
    pass

while True:
    print('1. Skapa konto')
    print('2. Ta bort konto')
    print('3. Lista alla kontonummer')
    print('4. Lista totalsaldo') # Saldot totalt för alla konton tillsammans
    print('5. Lista alla kontonummer och saldo')
    print('6. Avsluta')
    meny_val =  input('Gör ditt val: ')

    if meny_val == '1':
        skapa_konto()

    elif meny_val == '2':
        ta_bort_konto()

    elif meny_val == '3':
        lista_alla_kontonummer()

    elif meny_val == '4':
        lista_totalsaldo()

    elif meny_val == '5':
        lista_kontonummer_och_saldo()

    elif meny_val == '6':
        break

    else:
        print('Ej giltligt val!!')

