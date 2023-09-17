from pandas_datareader import data
from pandas import DataFrame
from asyncio import sleep
from warnings import filterwarnings
filterwarnings('ignore')


class TickerData:
	using_columns: list[str] = [
		'OPEN', 'CLOSE', 'HIGH', 'LOW', 'CLOSE-OPEN', 'VOLATILITY',
		'SMA5', 'SMA12', 'EMA5', 'EMA12', 'MACD', 'SIGNAL'
	]

	@classmethod
	def data_prepare(cls, ticker_data: DataFrame) -> dict[str, list[float]]:
		return {column: [round(price, 2) for price in ticker_data[column] if price is not None] for column in cls.using_columns}

	@classmethod
	async def get(cls, ticker: str, start_date: str, end_date: str) -> dict[str, list[float]]:
		await sleep(0.5)
		ticker_data = data.DataReader(ticker, 'moex', start_date, end_date)
		ticker_data['CLOSE-OPEN'] = ticker_data['CLOSE'] - ticker_data['OPEN']
		ticker_data['VOLATILITY'] = ticker_data['CLOSE'].rolling(5).std()
		ticker_data['SMA5'] = ticker_data['CLOSE'].rolling(5).mean()
		ticker_data['SMA12'] = ticker_data['CLOSE'].rolling(12).mean()
		ticker_data['EMA5'] = ticker_data['CLOSE'].ewm(span=5).mean()
		ticker_data['EMA12'] = ticker_data['CLOSE'].ewm(span=12).mean()
		ticker_data['MACD'] = ticker_data['CLOSE'].ewm(span=12).mean() - ticker_data['CLOSE'].ewm(span=26).mean()
		ticker_data['SIGNAL'] = ticker_data['MACD'].ewm(span=9).mean()
		ticker_data.drop(ticker_data.columns.difference(cls.using_columns), 1, inplace=True)
		ticker_data = ticker_data[11:]
		return cls.data_prepare(ticker_data)
