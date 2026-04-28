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

tab1, tab2, tab3 = st.tabs(["Net Income", "ROIC", "Cash Conversion Ratio"])

with tab1:
    st.subheader("Net Income Quarterly")
    net_income_chart = ch.net_income_chart(ticker_data)
    st.altair_chart(net_income_chart, use_container_width=True)

with tab2:
    st.subheader("Return on Invested Capital")

with tab3:
    st.subheader("Cash Conversion Ratio")

st.subheader("Analyst Price Target")
#st.write("Low:", ticker_data.analyst_price_targets["low"])