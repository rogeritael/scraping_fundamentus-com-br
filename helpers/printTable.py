from tabulate import tabulate
import locale

def printTable(elements):
    header = ['CÓDIGO', 'SEGMENTO','COTAÇÃO ATUAL','DIVIDEND YIELD']
    table = []

    for element in elements:
        table.append([
            element.codigo,
            element.segmento,
            locale.currency(element.cotacao_atual),
            f'{locale.str(element.dividend_yield)}%'
        ])

    print(tabulate(table, headers=header, showindex='always', tablefmt="fancy_grid"))