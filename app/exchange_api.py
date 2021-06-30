import json
import requests

class Exchange:
    def __init__(self, base_currency):
        self.rates(base_currency)
        self.base_currency = base_currency

    def rates(self, base_currency):
        url = "https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/" + base_currency.upper()
        check_response_rates = requests.get(url)

        try:
            check_response_rates.status_code == 200
            response_dict = check_response_rates.json()
            file = open('rates.txt', 'w')

            for key in response_dict['conversion_rates'].keys():

                file.write("{}/{} --- 1: {}\n".format(base_currency, key ,response_dict['conversion_rates'][key]))
                print("{} exchange rate is {}".format(key, response_dict['conversion_rates'][key]))

        except:
            print("base Currency not available")



    def single_rate(self, currency):

        url = "https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/" + self.base_currency.upper()

        check_response_rates = requests.get(url)
        try:
            check_response_rates.status_code == 200
            response_dict = check_response_rates.json()

            print("{} exchange rate is {}".format(currency.upper(), response_dict['conversion_rates'][currency.upper()]))

        except:
            print("Currency not available")


    def graph_plotter(self, currency):
        for i in range(1,10):
            year = 2005 + i
            for t in range(1, 12):
                month = 0 + t
                for o in range(0, 28)
                    day = 0 + 1

            url = "https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/history/" + self.base_currency + "/" + str(year) + "/" + str(month) + "/" + str(day)
            check_response_rates = requests.get(url)
            response_dict = check_response_rates.json()
            y = range(1,3660)
            x = response_dict['conversion_rates'][currency]

            plt.plot(x, y, color="red")
        plt.show()


