full_dot = '●'
empty_dot = '○'

def create_character(nombre,fuerza,inteligencia,carisma):
    if not isinstance(nombre,str):
        return 'The character name should be a string'
    if nombre == '':
        return 'The character should have a name'
    if len(nombre) > 10:
        return 'The character name is too long'
    if ' ' in nombre:
        return 'The character name should not contain spaces'
    if not isinstance(fuerza,int) or not isinstance(inteligencia,int) or not isinstance(
        carisma,int):
        return 'All stats should be integers'
    if fuerza < 1 or inteligencia < 1 or carisma < 1:
        return 'All stats should be no less than 1'
    if fuerza >4 or inteligencia >4 or carisma >4 :
        return 'All stats should be no more than 4'
    if fuerza+inteligencia+carisma != 7:
        return 'The character should start with 7 points'
    return f'''{nombre}
    STR {'●'*fuerza}
    
    '''

print(create_character('Aragorn', 3, 2, 2))