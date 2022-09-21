from sre_parse import CATEGORIES
from unicodedata import category
import streamlit as st
import pandas as pd
from main import Data
import datetime

st.set_page_config(layout="wide")

st.title("Financial Analyzer")


date_range = {
    'January': "2022-01-01 2022-01-30",
    "February": "2022-02-01 2022-02-29",
    "March": "2022-03-01 2022-03-31",
    "April": "2022-04-01 2022-04-30",
    "May": "2022-05-01 2022-05-31",
    "June": "2022-06-01 2022-06-30",
    "July": "2022-07-01 2022-07-31",
    "August": "2022-08-01 2022-08-31",
    "September": "2022-09-01 2022-09-30",
    "October": "2022-10-01 2022-10-31",
    "November": "2022-11-01 2022-11-30",
    "December": "2022-12-01 2022-12-31"
}
chosen_date = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "October",
    "November",
    "December"
]
# Takes file input
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Please input your CSV File:")

# Choose date range
with col2:
    selected_date = st.selectbox("Choose date:", chosen_date)   

# When file is loaded
if uploaded_file is not None:
    data = Data()
    income_df, expense_df = data.main(uploaded_file)

    expense_df = expense_df.loc[((expense_df['Date'] >= date_range[selected_date].split(" ")[0]) &
                                    (expense_df['Date'] <= date_range[selected_date].split(" ")[1]))]
    expense_df['Date'] = expense_df['Date'].dt.date
    expense_df = expense_df.reset_index(drop=True)
    category_df = expense_df.groupby('Category').sum()

    income_df = income_df.loc[((income_df['Date'] >= date_range[selected_date].split(" ")[0]) &
                                    (income_df['Date'] <= date_range[selected_date].split(" ")[1]))]
    income_df['Date'] = income_df['Date'].dt.date
    income_df = income_df.reset_index(drop=True)
    income_category_df = income_df.groupby('Category').sum()

    # Spending Presentation
    st.header("Spending")
    st.table(expense_df.style.format({'Amount': '{:.2f}'}))

    col3, col4 = st.columns(2)
    with col3:
        total_expense = category_df["Amount"].sum()
        total_income = income_category_df.sum()
        st.header(f"Total Expenses: ${total_expense}")
    with col4:
        st.table(category_df.style.format({'Amount': '{:.2f}'}))


    # Income Presentation
    st.header("Income")
    st.table(income_df.style.format({'Amount': '{:.2f}'}))

    col5, col6 = st.columns(2)
    with col5:
        total_income = income_category_df["Amount"].sum()
        st.header(f"Total Income: ${total_income}")
    with col6:
        st.table(income_category_df.style.format({'Amount': '{:.2f}'}))

    