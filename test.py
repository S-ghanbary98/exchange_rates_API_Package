import requests
import json

url="https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/GBR"

check_response_postcode = requests.get("https://v6.exchangerate-api.com/v6/92ae685f1a767893873e4b71/latest/GBP")

# print(type(check_response_postcode.headers))

response_dict = check_response_postcode.json()
print(response_dict['conversion_rates'])

for key in response_dict['conversion_rates'].keys():
    print("{} exchange rate is {}".format(key,response_dict['conversion_rates'][key]))