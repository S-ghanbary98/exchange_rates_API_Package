# Exchange Rates API Package

### Summary

In this task I will create a class that will take in a base currency and output the current exchange rates. 
This is done by making a call to an external api. 

### Exchange Class
- Firstly we import the `json` and `request` modules.
- Then create an Exchange class allows object to be created with a base currency as the argument.
- The `rates` function then displays all the exchange rates against the chosen base currency.
- `single_rate` function can display single rates.

- Result is both printed in the terminal anc can be found in `rates.txt` file

```
import json
import requests

class Exchange:
    def __init__(self, base_currency):
        self.rates(base_currency)                # calls rates function with base_currency argument 
        self.base_currency = base_currency


    def rates(self, base_currency):
    # API call
        url = "https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/" + base_currency.upper()
        check_response_rates = requests.get(url)
    #check for successful status code
        if check_response_rates.status_code == 200:
            response_dict = check_response_rates.json()               # Turn into json()
                
            for key in response_dict['conversion_rates'].keys():
                print("{} exchange rate is {}".format(key, response_dict['conversion_rates'][key]))

        else:
            print("base Currency not available")



    def single_rate(self, currency):

        url = "https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/" + self.base_currency.upper()

        check_response_rates = requests.get(url)
        if check_response_rates.status_code == 200:
            response_dict = check_response_rates.json()

            print("{} exchange rate is {}".format(currency.upper(), response_dict['conversion_rates'][currency.upper()]))

        else:
            print("Currency not available")

```

#### Program.py
- Program run in `program.py`
- `AUD` Chosen as base currency. 
- Once program is run `rates.txt` will be populated as seen below

```python
from app.exchange_api import Exchange


rate1 = Exchange("AUD")
```
#### Rates.txt
```python
AUD/AUD --- 1: 1
AUD/AED --- 1: 2.7652
AUD/AFN --- 1: 59.722
AUD/ALL --- 1: 77.5955
AUD/AMD --- 1: 373.16
AUD/ANG --- 1: 1.3478
AUD/AOA --- 1: 492.3415
...............
```