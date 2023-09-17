from fastapi import FastAPI
from uvicorn import run as uvi_run

from api_functuons.data.parser import TickerData
from api_functuons.strategy_testing.algo import TradingAlgorithms
sst_app = FastAPI(title='Stock strategy testing')
HOST: str = 'localhost'
PORT: int = 9999


@sst_app.get('/sst/{ticker}/{date_start}/{date_end}')
async def strategy_testing(ticker: str, date_start: str, date_end: str) -> dict:
	try:
		ticker_data = await TickerData.get(ticker=ticker, start_date=date_start, end_date=date_end)
	except:
		return {'status': 400, 'data': []}

	try:
		t_alg = TradingAlgorithms(ticker_data=ticker_data)
		sst_result = {
			'sma_strategy': await t_alg.sma_strategy(),
			'increase_strategy': await t_alg.increase_strategy(),
			'ema_strategy': await t_alg.ema_strategy(),
			'threshold_strategy': await t_alg.threshold_strategy(),
			'volatility_strategy': await t_alg.volatility_strategy(),
			'macd_strategy': await t_alg.macd_strategy()
		}
		return {'status': 200, 'data': [sst_result]}
	except:
		return {'status': 408, 'data': []}


@sst_app.get('/data/{ticker}/{date_start}/{date_end}')
async def get_data(ticker: str, date_start: str, date_end: str) -> dict:
	try:
		ticker_data = await TickerData.get(ticker=ticker, start_date=date_start, end_date=date_end)
		return {'status': 200, 'data': [ticker_data]}
	except:
		return {'status': 400, 'data': []}


if __name__ == '__main__':
	uvi_run(sst_app, host=HOST, port=PORT)
