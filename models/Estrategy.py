from models.RealEstateFund import RealEstateFund

class Estrategy:
    def __init__(self, segmento='', cotacao_atual_minimum=0, ffo_yield_minimum=0, dividend_yield_minimum=0, p_vp_minimum=0, valor_mercado_minimum=0, liquidez_minimum=0, qt_imoveis_minimum=0, preco_m2_minimum=0, aluguel_m2_minimum=0, cap_rate_minimum=0, vacancia_media_maximum=0 ):
        self.segmento = segmento
        self.cotacao_atual_minimum = cotacao_atual_minimum
        self.ffo_yield_minimum = ffo_yield_minimum
        self.dividend_yield_minimum = dividend_yield_minimum
        self.p_vp_minimum = p_vp_minimum
        self.valor_mercado_minimum = valor_mercado_minimum
        self.liquidez_minimum = liquidez_minimum
        self.qt_imoveis_minimum = qt_imoveis_minimum
        self.preco_m2_minimum = preco_m2_minimum
        self.aluguel_m2_minimum = aluguel_m2_minimum
        self.cap_rate_minimum = cap_rate_minimum
        self.vacancia_media_maximum = vacancia_media_maximum
    
    def runEstrategy(self, fund: RealEstateFund):
        if self.segmento != '':
            if fund.segmento != self.segmento:
                return False

        if fund.cotacao_atual < self.cotacao_atual_minimum \
            or fund.ffo_yield < self.ffo_yield_minimum \
            or fund.dividend_yield < self.dividend_yield_minimum \
            or fund.p_vp < self.p_vp_minimum \
            or fund.valor_mercado < self.valor_mercado_minimum \
            or fund.liquidez < self.liquidez_minimum \
            or fund.qt_imoveis < self.qt_imoveis_minimum \
            or fund.preco_m2 < self.preco_m2_minimum \
            or fund.aluguel_m2 < self.aluguel_m2_minimum \
            or fund.cap_rate < self.cap_rate_minimum \
            or fund.vacancia_media > self.vacancia_media_maximum \
        :
            return False
        else:
            return True