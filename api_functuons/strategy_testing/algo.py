from asyncio import sleep


class TradingAlgorithms:
	def __init__(self, ticker_data: dict[str, list[float]]):
		self.ticker_data = ticker_data
		self.delay: float = 0.5

	async def sma_strategy(self) -> list[float]:
		"""
		Base variation sma strategy with the condition of profitability of the previous day
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			if self.ticker_data['SMA5'][day_index] > self.ticker_data['SMA12'][day_index] \
					and self.ticker_data['CLOSE-OPEN'][day_index - 1] > 0:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income

	async def increase_strategy(self) -> list[float]:
		"""
		Growth will be estimated for the last 5 days
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			five_days_slise_prices = self.ticker_data['CLOSE-OPEN'][day_index - 5:day_index]
			if sum(five_days_slise_prices) / 5 > 0:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income

	async def ema_strategy(self) -> list[float]:
		"""
		Similar to sma strategy
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			if self.ticker_data['EMA5'][day_index] > self.ticker_data['EMA12'][day_index] \
					and self.ticker_data['CLOSE-OPEN'][day_index - 1] > 0:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income

	async def threshold_strategy(self) -> list[float]:
		"""
		The average price is taken as the threshold.
		Buy Condition: The current open price is greater than the 5-day average close price.
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			average_close_five_days = sum(self.ticker_data['CLOSE'][day_index - 5:day_index]) / 5
			if self.ticker_data['OPEN'][day_index] > average_close_five_days:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income

	async def volatility_strategy(self) -> list[float]:
		"""
		Buy strategy: yesterday's volatility is less than the day before
		yesterday and yesterday's yield is greater than zero.
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			before_yesterday_volatility = self.ticker_data['VOLATILITY'][day_index - 2]
			yesterday_volatility = self.ticker_data['VOLATILITY'][day_index - 1]
			yesterday_income = self.ticker_data['CLOSE-OPEN'][day_index - 1]
			if yesterday_volatility < before_yesterday_volatility and yesterday_income > 0:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income

	async def macd_strategy(self) -> list[float]:
		"""
		Buying logic strategy is similar to sma and ema.
		"""
		await sleep(self.delay)
		income = list()
		for day_index in range(len(self.ticker_data)):
			if self.ticker_data['MACD'][day_index] > self.ticker_data['SIGNAL'][day_index] and \
					self.ticker_data['CLOSE-OPEN'][day_index - 1] > 0:
				income.append(round(self.ticker_data['CLOSE-OPEN'][day_index], 2))
		return income
