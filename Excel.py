import pandas as pd
import xlwings as xw
from datetime import date, timedelta
import datetime

class Excel(object):
    def __init__(self):
        self.__excel = xw.Book('BYMADATA.xlsb')
        self.__tickers = self.get_sheet('Tickers')
        self.__bolsuite = self.get_sheet('Bolsuite')
        self.__dates = self.create_date()
        self.__cauciones = self.create_cauciones()
        self.__basesGGAL = pd.DataFrame()
        # self.__allOptions = pd.DataFrame()


    def get_excel(self):
        return self.__excel


    def get_tickers(self):
        return self.__tickers


    def get_sheet(self,name_sheet):
        return self.get_excel().sheets(name_sheet)

    def get_data_frame_options(self):
        return self.__allOptions

    def set_data_frame_options(self,data_frame):
        self.__allOptions = data_frame

    def get_dates(self):
        return self.__dates


    def get_cauciones(self):
        return self.__cauciones

    def get_bolsuite(self):
        return self.__bolsuite


    def get_data_frame(self,range_excel):
        rng = self.get_tickers().range(range_excel).expand()
        oOpciones = rng.value
        data_frame = pd.DataFrame({'symbol': oOpciones},
                                  columns=["symbol", "bid_size", "bid", "ask", "ask_size", "last",
                                       "change", "open", "high", "low", "previous_close", "turnover", "volume",
                                       'operations', 'datetime'])

        data_frame = data_frame.set_index('symbol')
        data_frame['datetime'] = pd.to_datetime(data_frame['datetime'])
        print('dataframe***************************************************')
        return data_frame
    
    # def get_data_frame_options(self,range_excel):
    #     rng = self.get_tickers().range(range_excel).expand()
    #     oOpciones = rng.value
    #     data_frame = self.get_data_frame_options()
    #     print('dataframe')
    #     print(data_frame)
    #     data_frame = pd.DataFrame({'symbol': oOpciones},
    #                               columns=["symbol", "bid_size", "bid", "ask", "ask_size", "last",
    #                                    "change", "open", "high", "low", "previous_close", "turnover", "volume",
    #                                    'operations', 'datetime'])

    #     data_frame = data_frame.set_index('symbol')
    #     data_frame['datetime'] = pd.to_datetime(data_frame['datetime'])
    #     # self.set_data_frame_options(data_frame)
    #     print('dataframe options***************************************************')
    #     print(data_frame)
    #     return data_frame


    def create_date(self):
        i = 1
        dates = []
        while i < 31:
            fecha = date.today() + timedelta(days=i)
            dates.extend([fecha])
            i += 1
        return dates


    def create_cauciones(self):
        cauciones = pd.DataFrame({'settlement': self.get_dates()},
                                 columns=['settlement', 'last', 'turnover', 'bid_amount', 'bid_rate', 'ask_rate',
                                          'ask_amount'])
        cauciones['settlement'] = pd.to_datetime(cauciones['settlement'])
        cauciones = cauciones.set_index('settlement')
        print("CAUCIONES")
        print(cauciones)
        return cauciones