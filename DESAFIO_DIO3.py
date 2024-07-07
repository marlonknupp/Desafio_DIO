import re 
pattern = r"(\([0-9]{2}\)) (9[0-9]{4})-([0-9]{4})"

def validate_numero_telefone(phone_number):
    if re.match(pattern, phone_number):
        print ('\n Número de telefone válido.\n')
    else:
        print ('\n Número de telefone inválido.\n')
phone_number = input('\n Digite um numero de telefone:')

validate_numero_telefone(phone_number)

#DIO.