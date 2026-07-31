test_settings={
    'theme':'green'
}
setting = ('a','b')

def add_setting(dic,tup):
    key,value = tup
    key = key.lower()
    value = value.lower()
    if key in dic:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dic[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dic,tup):
    key,value = tup
    key = key.lower()
    value = value.lower()
    if key in dic:
        dic[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dic, key):
    key = key.lower()

    if key in dic:
        del dic[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

def view_settings(dic):
    resulta = "Current User Settings:\n"
    if not dic:
        return 'No settings available.'
    for key,value in dic.items():
        resulta += f'{key.capitalize()}: {value}\n'
    return resulta
