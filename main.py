from numpy import arange

def kod_pocz(kod1, kod2):
    liczba1=int(kod1[0:2] +kod1[3:6])
    liczba2 = int(kod2[0:2] +kod2[3:6])
    print(liczba1, liczba2)
    if liczba1 < liczba2:
        for i in range(liczba1 + 1, liczba2 - 1):
            print(i)
    elif liczba1 > liczba2:
        for i in range(liczba2 + 1, liczba1 - 1):
            print(i)
    else:
        print("codes are this same")

def check_list():
    lista=[2,3,7,4,9]
    n=10
    output=[]
    for k in range(n):
        if k not in lista:
            output.append(k)
    print(output)

def generator():
    a=2.0; b=5.5; c=0.5
    gen=[]
    for k in arange(a,b+c,c):
        gen.append(k)
    print(gen)

# Main
wybor = int(input("1 - postal code; 2 - check list; 3 - number generator: "))

if wybor==1:
    kod1 = input("wprowadź kod 1: ")
    kod2 = input("wprowadź kod 2: ")

    kod_pocz(kod1, kod2)

if wybor==2:
    check_list()

if wybor==3:
    generator()
