# en dictionary är på svenska en "avbildning"
# x --> y

x1 = 0.0
x2 = 0.1
x3 = 0.2

def f(x):
    return x**2

dict_avbildning = {}
dict_avbildning[x1] = f(x1)
dict_avbildning[x2] = f(x2)
dict_avbildning[x3] = f(x3)

for x,y in dict_avbildning.items():
    print(f'Vi har kartlagt {x=} så att värdet i våran dictionary är {y=}')