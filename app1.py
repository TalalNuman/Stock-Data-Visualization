import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App
Shows the stock price of a given stock of Tesla 
"""
         )

tikcersymbol = "TSLA"
tickerdata = yf.Ticker(tikcersymbol)
tickerdf = tickerdata.history(
    period="1d", start="2010-01-01", end="2020-04-01")

# open  High  Low Close Volume Dividends Stock Splits

st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)
