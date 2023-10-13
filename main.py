import requests
from bs4 import BeautifulSoup
import locale
import tabulate

# helpers
from helpers.format_percent import format_percent
from helpers.format_decimal import format_decimal

#altera o sistema monetários do sistema Brasileiro para o sistema americano, com .
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# simula o browser Mozila
headers = { 'User-Agent': 'Mozila/5.0' }

# Retorna a estrura da página HTML
response = requests.get('https://fundamentus.com.br/fii_resultado.php', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

#busca pelo id
lines = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

for line in lines:
    data = line.find_all('td')

    codigo = data[0].text
    segmento = data[1].text
    cotacao_atual = format_decimal(data[2].text)
    ffo_yield = format_percent(data[3].text)
    dividend_yield = format_percent(data[4].text)
    p_vp = format_decimal(data[5].text)
    valor_mercado = format_decimal(data[6].text)
    liquidez = format_decimal(data[7].text)
    qt_imoveis = int(data[8].text)
    preco_m2 = format_decimal(data[9].text)
    aluguel_m2 = format_decimal(data[10].text)
    cap_rate = format_percent(data[11].text)
    vacancia_media = format_percent(data[12].text)

    print(cotacao_atual)