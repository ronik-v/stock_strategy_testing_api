from setuptools import setup, find_packages


# load files
with open('requirements.txt') as file:
	requires = file.readlines()

with open('README.md') as file:
	readme = file.readlines()

setup(
	author='ronik-v',
	name='Stock strategy testing',
	description='API for receiving stock price data and using this data in other languages, as well as testing trading '
				'strategies in a consistent format.',
	license='Apache-2.0 license',
	packages=find_packages(include=['src']),
	python_requires='>=3.10',
	url='https://github.com/ronik-v/stock_strategy_testing_api'
)
