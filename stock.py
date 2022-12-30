import yfinance as yf
import streamlit as st

st.write("""
## Simple Stock Information App """)

# Get stock symbol from user
symbol = st.text_input("Stock Symbol")
Data = yf.Ticker(symbol)
info = Data.info

if type(info) == dict:
    # check if variable having value
    # get some important values
    if st.button('More Information'):
        st.write("Name:  {}  ".format(info.get('shortName')))
        st.write("Sector:  {}".format(info.get('sector')))
        st.write("Country:  {}".format(info.get('country')))
        st.write("Industry:  {}".format(info.get('industry')))
        st.write("Total Revenue:  {}".format(info.get('totalRevenue')))
        st.write("Pre Market Price:  {}".format(info.get('preMarketPrice')))
        st.write("Open:  {}".format(info.get('open')))
        st.write("Current Price:  {}".format(info.get('currentPrice')))
        st.write("Fifty Two Week High:  {}".format(info.get('fiftyTwoWeekHigh')))
        st.write("fifty Two Week Low:  {}".format(info.get('fiftyTwoWeekLow')))
        st.write("Website:  {}".format(info.get('website')))

    else:
        pass

    if st.button('Balance sheet'):
        st.write(Data.balancesheet)

    if st.button('Cashflow sheet'):
        st.write(Data.cashflow)

    if st.button('Financials sheet'):
        st.write(Data.financials)

    # closing price graph
    tickerDf = Data.history(period='1d', start='2021-01-01', end='2022-12-30')
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
        ('Historical Data', 'Closing Price', 'Volume'))
    if option == 'Historical Data':
        st.write(Data.history())
    elif option == "Closing Price":
        st.write("""
        ### Closing Price """, tickerDf.Close)
    else:
        st.write("""
            ### Volume """, tickerDf.Volume)

else:
    st.write("""### Please input Valid Stock symbol """)
