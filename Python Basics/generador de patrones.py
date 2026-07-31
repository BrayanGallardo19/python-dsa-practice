def number_pattern(n):
    if (isinstance(n,int)) == False:
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    cadena = ''
    for x in range(1,n+1):
        if x < n:
            cadena += str(x) 
            cadena += ' '
        else:
            cadena += str(x)
    return cadena
print(number_pattern(5))
