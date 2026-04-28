import streamlit as st
from data import load_ticker_data
import charts as ch

st.title("Stock Dashboard")
ticker_symbol = st.text_input("Enter stock symbol", "MSFT")

ticker_data = load_ticker_data(ticker_symbol)

st.subheader("Company Info")
st.write(
    "Dividend Yield", ticker_data["dividendYield"],
    "Forward PE", ticker_data["forwardPE"],
    #"Avg trading volume", ticker.info[""]
    )

st.subheader("Price History (1 month)")
history_chart = ch.history_chart(ticker_data)
st.altair_chart(history_chart, use_container_width=True)


st.subheader("Net Income Quarterly")
quarterly_chart = ch.quarterly_chart(ticker_data)
st.altair_chart(quarterly_chart, use_container_width=True)

st.subheader("Analyst Price Target")
#st.write("Low:", ticker.analyst_price_targets["low"])