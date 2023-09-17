from requests import get

data = get('http://localhost:9999/data/GMKN/2022-05-01/2023-09-16').json()
print(data)

sst_strategies = get('http://localhost:9999/sst/GMKN/2022-05-01/2023-09-16').json()
print(sst_strategies)
