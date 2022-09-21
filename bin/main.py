from typing_extensions import Self
import pandas as pd
from datetime import datetime 
import numpy as np
class Data:
    def main(self,df):
        df = self.convert(df)
        income_df, expense_df = self.prepare_data(df)
        return income_df, expense_df

    # Convert the file path into a dataframe, return dataframe
    def convert(self,df) ->pd.DataFrame:
        df = pd.read_csv(df)
        return df

    # Filter to necessary data, split income and expense data
    def prepare_data(self,df: pd.DataFrame) -> pd.DataFrame: 
        df['Date'] = pd.to_datetime(df['Date'])
        df = df[df['Category'].str.contains('Transfer|Credit Card Payment')==False]

        income_df = self.drop_columns(df[df['Transaction Type'] == 'credit'].reset_index())
        expense_df = self.drop_columns(df[df['Transaction Type'] == 'debit'].reset_index())
        
        return income_df, expense_df

    # Drop unwanted columns
    def drop_columns(self,df:pd.DataFrame) -> pd.DataFrame:
        df = df.drop(['index','Transaction Type','Original Description','Account Name','Labels','Notes'],axis=1)
        return df


if __name__ == "__main__":
    data = Data()
    data.main()
