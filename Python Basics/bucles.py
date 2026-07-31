#ciclo for
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)
#ciclo for en una cadena de texto
palabra = 'Python'
for letra in palabra:
    print(letra)    

#for anidado   
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento) 

#ciclo while
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Adivina el número secreto (entre 1 y 10): "))
    if guess < secret_number:
        print("Demasiado bajo. Intenta de nuevo.")
    elif guess > secret_number:
        print("Demasiado alto. Intenta de nuevo.")
print("¡Felicidades! Has adivinado el número secreto.")

#break rompe el ciclo actual 
for i in range(1, 11):
    if i == 5:
        break  # Detiene el ciclo cuando i es igual a 5
    print(i)

#continue salta a la siguiente iteración del ciclo
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta el número par y continúa con la siguiente iteración
    print(i)  # Imprime solo los números impares


words = ['sky', 'apple', 'rhythm', 'fly', 'aaorange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")