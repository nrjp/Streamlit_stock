import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Simple Stock Information App """)

# Get stock symbol from user
symbol = st.text_input("Stock Symbol")
Data = yf.Ticker(symbol)
info = Data.info
if type(info) == dict:
    # check if variable having value
    # get some important values
    st.write("Name:  {}  ".format(info.get('shortName')))
    st.write("Sector:  {}".format(info.get('sector')))
    st.write("Country:  {}".format(info.get('country')))
    st.write("Industry:  {}".format(info.get('industry')))
    st.write("Total Revenue:  {}".format(info.get('totalRevenue')))
    st.write("Pre Market Price:  {}".format(info.get('preMarketPrice')))
    st.write("Open:  {}".format(info.get('open')))
    st.write("Fifty Two Week High:  {}".format(info.get('fiftyTwoWeekHigh')))
    st.write("fifty Two Week Low:  {}".format(info.get('fiftyTwoWeekLow')))

    # closing price graph
    tickerDf = Data.history(period='1d', start='2020-01-01', end='2022-11-30')
    st.write("""
    ### Closing Price """)

    # volume graph
    st.line_chart(tickerDf.Close)
    st.write("""
    ### Volume """)
    st.line_chart(tickerDf.Volume)

    ## information in dataframe
    option = st.selectbox(
        'Seleted from following',
        ('History', 'Closing Price', 'Volume'))
    if option == 'History':
        option = st.selectbox(
            'Seleted from following',
            ('1 month', '4 Months', '1 Year', '5 Year', 'max'))
        st.write(Data.history(period=option))
    elif option == "Closing Price":
        st.write("""
        ### Closing Price """, tickerDf.Close)
    else:
        st.write("""
            ### Closing Price """, tickerDf.Volume)
else:
    st.write("""### Please input Valid Stock symbol """)
