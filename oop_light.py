class Person:
    # Händer massa saker!!
    # Sedan anropas __init__ inifrån Person
    def __init__(self, namn, ålder) -> None:
        self._name = namn
        self._age = ålder

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def __str__(self):
        return f'Jag heter {self._name} och är {self._age} gammal!'
    
    def __add__(self,person):
        return Person(self._name + person.get_name(),
                      self._age + person.get_age())
        # return self._age + person.get_age()


if __name__=='__main__':
    # objekt1 = Person('Sebastian',35)
    # objekt2 = Person('Daniel', 28)
    # print(objekt1.get_age())
    # print(objekt1.get_name())
    # print(objekt2.get_age())
    # print(objekt2.get_name())
    lista_med_personer = []
    while True:
        # Vi tar in en sträng med <namn> <ålder> med ett mellanslag mellan ordern!
        namn_och_ålder = input('Skriv in namn och ålder: ')
        # Om q så avslutar vi
        if namn_och_ålder == 'q':break
        # Annars delar vi upp strängen till en lista med första elementet namn och andra elementet är ålder
        namn_och_ålder=namn_och_ålder.split()
        # Vi tilldelar namn och ålder respektive element i listan
        namn,ålder = namn_och_ålder[0],namn_och_ålder[1]
        # Skapa en ny person som har name = namn och age = ålder 
        new_person = Person(namn, int(ålder))
        lista_med_personer.append(new_person)

    # for person in lista_med_personer:
    #     # print(person.get_name())
    #     # print(person.get_age())
    #     print(person)
    p1 ,p2, p3 = lista_med_personer[:3]
    print(f'{p1+p2+p3}')
    