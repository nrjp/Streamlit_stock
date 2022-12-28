import yfinance as yf
import streamlit as st
import pandas as  pd


st.write("""
### Simple Stock Information App """)

#Get stock symbol from user
X = st.text_input("Stock Symbol")
#symbol
symbol = X

Data = yf.Ticker(symbol)
info = Data.info


# app
st.write("""
shows are the stock **closing price** and **Volume** of {}""".format(info.get('longBusinessSummary')[0:22]))

tickerDf = Data.history(period='1d',start='2020-01-01',end='2022-11-30')
st.write("""
### Closing Price """)
st.line_chart(tickerDf.Close)
st.write("""
### Volume """)
st.line_chart(tickerDf.Volume)
## other information
option = st.selectbox(
    'Seleted from following',
    ('History', 'Closing Price', 'Volume'))
st.write(Data.history(period="max"))

