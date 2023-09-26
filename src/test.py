from requests import get

data = get('http://localhost:9999/api_sst/data/GAZP/2022-05-01/2023-09-26').json()
print(data)

sst_strategies = get('http://localhost:9999/api_sst/strategy/GAZP/2022-05-01/2023-09-26').json()
print(sst_strategies)
