import os
import sys
from datetime import date, datetime, timedelta, time
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.append(os.path.abspath(os.path.join('.')))

import paper_pants.data_collection.scraper.statement_scraper as ws
import paper_pants.data_collection.API.stock_api as sa
import paper_pants.trading_strategies.strategies.technical_indicators.ohlcv_ti as ti
from paper_pants.trading_strategies.backtesting.kpis.kpi import CAGR, volatility, sharpe, sortino, max_dd, calmar
import paper_pants.portfolio.portfolio as pfl
import paper_pants.trading_strategies.strategies.strategies as st
import paper_pants.trading_strategies.backtesting.backtest as bt

import pandas_datareader.data as pdr

pages = ['Balance Sheet', 'Income Statement', 'Cash Flow', 'Key Ratios']
companies = ['MSFT']
startDate = datetime.combine(date.today(), time()) - timedelta(1095)
endDate = datetime.combine(date.today(), time())


if __name__ == "__main__":
    # yh_ws = ws.StatementScraper(pages, companies)
    # print(yh_ws)
    # yh_ws.scrape_yahoo()
    #
    # sA = sa.StockApi(companies, alpha_key_path='/app/api.key')
    #
    # ohlcv = sA.get_data_pd_yahoo(startDate, endDate)
    # print('CAGR: {}'.format(CAGR(ohlcv['MSFT'], 'd' )))
    # print('Volatility: {}'.format(volatility(ohlcv['MSFT'], 'd' )))
    # print('Sharpe: {}'.format(sharpe(ohlcv['MSFT'], 'd', 0.022 )))
    # print('Sortino: {}'.format(sortino(ohlcv['MSFT'], 'd', 0.022 )))
    # print('MaxDD: {}'.format(max_dd(ohlcv['MSFT'] )))
    # print('Calmar: {}'.format(calmar(ohlcv['MSFT'], 'd' )))
    #

    # print(sA.get_data_yahoofinancials(startDate,endDate))
    # print(sA.get_data_alpha_vantage(startDate, endDate))

    # ticker = "MSFT"
    # ohlcv = pdr.get_data_yahoo(ticker, datetime.date.today() - datetime.timedelta(1825), datetime.date.today())

    # print(ti.macd(ohlcv, 12, 26, 9))
    # print(ti.atr(ohlcv, 20))
    # print(ti.bollinger_band(ohlcv, 20))
    # print(ti.rsi(ohlcv, 14))
    # print(ti.adx(ohlcv, 14))
    # print(ti.obv(ohlcv))
    # print(ti.slope(ohlcv, 5))
    # print(ti.renko(ohlcv))

    tickers = ['MSFT', 'AAPL']
    tickers_strategy = {}

    for ticker in tickers:
        ohlcv = pdr.get_data_yahoo(ticker, startDate, endDate)
        st_ren_macd = st.Strategy(ohlcv)
        st_ren_macd.renko_macd()
        bt.Backtest(st_ren_macd)
        tickers_strategy[ticker] = st_ren_macd.df

        print(tickers_strategy[ticker])

    # st_rb = stgy.Strategy(ohlcv)
    # st_rb.resist_breakout()
    # print(bt.Backtest(st_rb))

    # st_ren_obv = stgy.Strategy(ohlcv)
    # st_ren_obv.renko_obv()
    # print(bt.Backtest(st_ren_obv))

    # st_ren_macd = st.Strategy(ohlcv)
    # st_ren_macd.renko_macd()
    # print(bt.Backtest(st_ren_macd))