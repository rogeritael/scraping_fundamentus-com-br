import locale

def format_decimal(decimal_str):

    #recebe uma string e faz o processamento de acordo com o locale definido no projeto
    return locale.atof(decimal_str)