#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17th, 2020

@author: adityakalia
"""

import yfinance as yf
import pandas as pd
import os

download_folder = os.path.expanduser("~") + "/Downloads/"


def read_file():
	df = pd.read_csv(download_folder + 'stock_sheet.csv')
	return df


def daily_change(df):
	stocks_df = pd.DataFrame()
	grand_total = 0
	for index, x in enumerate(df.stock):
		try:
			stock = yf.Ticker(x)
			tempdf = stock.history(period='1mo')
			tempdf.loc[:, "StockName"] = x
			tempdf['CloseNormalized'] = tempdf['Close'] - df.pricePaid[index]
			tempdf.loc[:, "$Change"] = (tempdf['CloseNormalized'] - df.pricePaid[index]).diff(periods=1)
			total_gain = (tempdf['CloseNormalized'][-1] * df.qty[index]).round(2)
			month_gain = ((tempdf["Close"][-1] - tempdf["Close"][0]) * df.qty[index]).round(2)
			week_gain = ((tempdf["Close"][-1] - tempdf["Close"][-5]) * df.qty[index]).round(2)
			day_gain = ((tempdf["Close"][-1] - tempdf["Close"][-2]) * df.qty[index]).round(2)
			print("|-------------------------------------|")
			print(f'{x} has made you\n${total_gain} In Total\n${month_gain} '
				  f'This Month\n${week_gain} This Week\n${day_gain} Today')
			stocks_df = stocks_df.append(tempdf, sort='False')

			grand_total = grand_total + total_gain
		except:
			print("Incorrect stock entered " + x)
			pass
	grand_total = grand_total.round(2)
	print("|-------------------------------------|")
	print(f'In Total you have made ${grand_total} !!')


def main():
	df = read_file()
	daily_change(df)


if __name__ == '__main__':
	main()