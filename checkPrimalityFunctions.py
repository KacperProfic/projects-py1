num = int(input('Wpisz liczbę: '))
a = [x for x in range(2, num) if num % x == 0]

def isPrime(n):
    if num > 1:
        if len(a) == 0:
            print('liczba pierwsza')

        else:
            print('liczba nie jest pierwsza')
    else:
        print('liczba nie jest pierwsza')
isPrime(num)


    