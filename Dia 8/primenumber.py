def isItPrime(n):
    for x in range(2,n):
        numeroPrimo = True
        if n % x ==0:
            numeroPrimo = False
            break
    if numeroPrimo == False:
        print('El numero no es primo')
    else:
        print('El numero es primo')


n = int(input('Introduce un numero: '))
isItPrime(n)

contador = int(input('cuantos primos quieres calcular?'))
for num in range(2,contador):
    prime = True
    for i in range(2,num):
       if (num%i==0):
            prime = False
    if prime:
       print (num)