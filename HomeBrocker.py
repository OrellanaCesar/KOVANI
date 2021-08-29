from pyhomebroker import HomeBroker
from Excel import  Excel
import pandas as pd
import time

class HomeBrocker(object):
    def __init__(self,broker, dni, user, password ):
        self.__user = user
        self.__dni = dni
        self.__password = password
        self.__broker = broker
        self.__excel = Excel()
        self.__options = self.get_excel().get_sheet('A2:A500')
        self.__actions = self.get_excel().get_sheet('C2:C500')
        self.__bonds = self.get_excel().get_sheet('E2:E500')
        self.__cauciones = self.get_excel().create_cauciones()
        self.__everything = self.get_actions().append(self.get_bonds())
        self.__home_broker = HomeBroker(int(broker), on_options=self.on_options, on_securities=self.on_securities,on_repos=self.on_repos, on_error=self.on_error)


    def get_user(self):
        return self.__user


    def set_user(self,user):
        self.__user = user


    def get_dni(self):
        return self.__dni


    def set_dni(self, dni):
        self.__dni = dni


    def get_password(self):
        return self.__password


    def set_password(self, password):
        self.__password = password


    def get_broker(self):
        return self.__broker


    def set_broker(self, broker):
        self.__broker = broker


    def get_excel(self):
        return self.__excel


    def get_options(self):
        return self.__options


    def get_actions(self):
        return self.__actions


    def get_bonds(self):
        return self.__bonds


    def get_everything(self):
        return self.__everything


    def get_cauciones(self):
        return self.__cauciones

    def get_home_broker(self):
        return self.__home_broker


    def rename_columns(self):
        return {"symbol": "Especie", "bid_size": "CantC", "bid": "PrecioC", "ask": "PrecioV", "ask_size": "CantV",
                   "last": "Ultimo","change": "Variacion", "open": "Apertura", "high": "Max", "low": "Min",
                    "previous_close": "Cierre","turnover": "Monto $", "volume": "Nominal","operations": "CantOp",
                "datetime": "Hora"}




    def on_options(self,online, quotes):
        thisData = quotes
        thisData = thisData.drop(['expiration', 'strike', 'kind'], axis=1)
        thisData['change'] = thisData["change"] / 100
        thisData['datetime'] = pd.to_datetime(thisData['datetime'])

        thisData = thisData.rename(columns=self.rename_columns())
        self.__options.update(thisData)


    def on_securities(self,online,quotes):
        # La siguiente linea muestra en pantalla como va actualizando... si molesta se la puede comentar con un numeral y deja de mostrarse, pero si actualiza igual.
        print(quotes)
        thisData = quotes
        thisData = thisData.reset_index()
        thisData['symbol'] = thisData['symbol'] + ' - ' + thisData['settlement']
        thisData = thisData.drop(["settlement"], axis=1)
        thisData = thisData.set_index("symbol")
        thisData['change'] = thisData["change"] / 100
        thisData['datetime'] = pd.to_datetime(thisData['datetime'])
        thisData = thisData.rename(columns=self.rename_columns())
        self.get_everything().update(thisData)

    def on_repos(self,online, quotes):
        thisData = quotes
        thisData = thisData.reset_index()
        thisData = thisData.set_index("symbol")
        thisData = thisData[['PESOS' in s for s in quotes.index]]
        thisData = thisData.reset_index()
        thisData['settlement'] = pd.to_datetime(thisData['settlement'])
        thisData = thisData.set_index("settlement")
        thisData['last'] = thisData["last"] / 100
        thisData['bid_rate'] = thisData["bid_rate"] / 100
        thisData['ask_rate'] = thisData["ask_rate"] / 100
        thisData = thisData.drop(['open', 'high', 'low', 'volume', 'operations', 'datetime'], axis=1)
        thisData = thisData[['last', 'turnover', 'bid_amount', 'bid_rate', 'ask_rate', 'ask_amount']]
        thisData = thisData.rename(columns=self.rename_columns())
        self.get_cauciones().update(thisData)

    def on_error(self,online, error):
        print("Error Message Received: {0}".format(error))


    def login_broker(self):
        self.get_home_broker().auth.login(dni=self.get_dni(),user=self.get_user(),password=self.get_password(),raise_exception=True)
        self.get_home_broker().online.connect()
        self.get_home_broker().online.subscribe_options()
        self.get_home_broker().online.subscribe_securities('bluechips', '48hs')
        self.get_home_broker().online.subscribe_securities('bluechips', '24hs')
        self.get_home_broker().online.subscribe_repos()


    def run(self):
        while True:
            try:
                oRange = 'R' + str(len(self.get_everything()) + 2)
                self.get_excel().get_bolsuite().range('R1').options(index=True, header=True).value = self.get_everything()
                self.get_excel().range(oRange).options(index=True, header=False).value = self.get_options()
                self.get_excel().range('AR2').options(index=True, header=False).value = self.get_cauciones()
                time.sleep(2)
            except:
                print('Hubo un error al actualizar excel')


