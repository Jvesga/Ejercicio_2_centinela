print("-----------------------------")
print("------- Ejercicio 2 ---------")
print("------ NUMEROS REALES -------")
print("-----------------------------")

n = int(input(" Ingrese el número: "))
par = 0
impar = 0

while n != 0 :
        r = n % 2
        if r == 0:
            par = par + 1
        else:
            impar = impar + 1
        

print(" Los numeros pares son: " + par)
print(" Los numeros impares son: " + impar)

    

