def verify_card_number(cadena):
    cadena = cadena.replace("-", "").replace(" ", "")
    print(cadena)
    try:
        int(cadena)
    except:
        return None
    verificador = int(cadena[-1])
    total = 0
    cadena = cadena[:-1]
    cadena_invertida = cadena[::-1]
    for x,y in enumerate(cadena_invertida):
        
        if x == 0:
            if int(y) * 2 > 9:
                total += int(y) * 2
                total -= 9
            else:
                total += int(y) * 2
        elif x % 2 == 0:
            if int(y) * 2 > 9:
                total += int(y) * 2
                total -= 9
            else:
                total += int(y) * 2
        else:
            total += int(y)

        print(total)
    total += verificador
    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'
    

print(verify_card_number('453914889'))