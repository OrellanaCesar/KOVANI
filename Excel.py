import pandas as pd
import xlwings as xw
from datetime import date, timedelta

class Excel(object):
    def __init__(self):
        self.__excel = xw.Book('BYMADATA.xlsb')
        self.__tickers = self.get_sheet('Tickers')
        self.__bolsuite = self.get_sheet('Bolsuite')
        self.__dates = self.create_date()
        self.__cauciones = self.create_cauciones()
        self.__basesGGAL = pd.DataFrame()


    def get_excel(self):
        return self.__excel


    def get_tickers(self):
        return self.__tickers


    def get_sheet(self,name_sheet):
        return self.get_excel().sheets(name_sheet)


    def get_dates(self):
        return self.__dates


    def get_cauciones(self):
        return self.__cauciones

    def get_bolsuite(self):
        return self.__bolsuite


    def get_data_frame(self,range_excel):
        rng = self.get_tickers().range(range_excel).expand()
        oOpciones = rng.value
        data_frame = pd.DataFrame({'Especie': oOpciones},
                                  columns=["Especie", "CantC", "PrecioC","PrecioV", "CantV", "Ultimo", "Variacion",
                                           "Apertura", "Max", "Min", "Cierre", "Monto $", "Nominal", "CantOp",
                                           'Hora', 'Promedio'])

        data_frame = data_frame.set_index('Especie')
        data_frame['Hora'] = pd.to_datetime(data_frame['Hora'])















        return data_frame


    def create_date(self):
        i = 1
        dates = []
        while i < 31:
            dates = date.today() + timedelta(days=i)
            dates.extend([dates])
            i += 1
        return dates


    def create_cauciones(self):
        cauciones = pd.DataFrame({'settlement': self.get_dates()},
                                 columns=['settlement', 'last', 'turnover', 'bid_amount', 'bid_rate', 'ask_rate',
                                          'ask_amount'])
        cauciones['settlement'] = pd.to_datetime(cauciones['settlement'])
        cauciones = cauciones.set_index('settlement')
        return cauciones