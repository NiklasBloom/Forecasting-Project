
import sqlite3
import pandas as pd
import numpy as np
import GraphFunctions

#Create a SQL connection to the SQLite database
con = sqlite3.connect("sample.sqlite")

cur = con.cursor()

#inserts the SQL data into a dataframe for easier analysis
df_account = pd.read_sql_query("SELECT * FROM account", con)
df_date = pd.read_sql_query("SELECT * FROM account_date_session", con)
df_iap = pd.read_sql_query("SELECT * FROM iap_purchase", con)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("the time frame of the data is from 2016-01-01 to 2016-12-31, this data is obtained form the df_Date dataset")
#The data is also from 190 countries across the world

print("Head of df_account: \n",df_account.head())
print("\nHead of df_date: \n",df_date.head())
print("\nHead of df_iap: \n",df_iap.head())

print("\nnumber of rows in df_account: ",len(df_account.index))
print("\nnumber of rows in df_date: ",len(df_date.index))
print("\nnumber of rows in df_iap: ",len(df_iap.index))

print("\nsize of df_account: ",df_account.size)
print("\nsize of df_date: ",df_date.size)
print("\nsize of df_iap: ",df_iap.size)

print("\ndata types and column names in df_account: ",df_account.dtypes)
print("\ndata types and column names in df_date: ",df_date.dtypes)
print("\ndata types and column names in df_iap: ",df_iap.dtypes)

print()



