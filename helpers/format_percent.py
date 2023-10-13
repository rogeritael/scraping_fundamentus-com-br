import locale

def format_percent(percent):

    #recebe uma string e faz o processamento de acordo com o locale definido no projeto
    return locale.atof(percent.split('%')[0])