'''
# Analysis questions
2. Analyse daily active users
Compare DAU changes over time
Can you identify trends in the data?
Can you find any ups or drops that are out of normal behavior?
What do you think, why do they happen?

3.
Analyze geographic split of the revenue and the users
Calculate average revenue per user per market
What are your observations of the results
'''

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


#commit
con.commit()
#close the connection
con.close()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#groups the Date Dataframe by day, reduces each day to its size
df_date_group = df_date.groupby('date').account_id.size()

#PRINTS DAU TIME SERIES GRAPH
#GraphFunctions.DAUgraph(df_date_group)

#group by day of week
df_date_group.index = pd.to_datetime(df_date_group.index, format='%Y-%m-%d')
df_date_group = df_date_group.reset_index()
#df_date_group is now a <class 'pandas.core.frame.DataFrame'>
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#group Daily User Activity by day of the week, and get mean.
week_df = df_date_group.groupby(df_date_group['date'].dt.day_name()).mean().reindex(days)
#is now a <class 'pandas.core.frame.DataFrame'>

week_df = week_df.reset_index()

#plot days of week DAU as bar graph
#GraphFunctions.DailyGraph(week_df)

#Convert the 'date' column to datetime
df_date_group['date'] = pd.to_datetime(df_date_group['date'])

# Set the 'date' column as the index
df_date_group.set_index('date', inplace=True)

#create dicts for data
quarters = {1: None, 2: None, 3: None, 4: None}
weekdays_data = {day: [] for day in days}

#Loop through each quarter, filter the data, and calculate the weekly means
for q in quarters:
    quarter_data = df_date_group[df_date_group.index.quarter == q]
    quarter_data = quarter_data.reset_index()#dataframe
    quarters[q] = quarter_data.groupby(quarter_data['date'].dt.day_name()).mean().reindex(days)

#Concatenate the data for each day of the week across all quarters
for day in days:
    weekdays_data[day] = pd.concat([quarters[q].loc[day] for q in quarters])

#Graphs QuarterlyDailyGraph
#GraphFunctions.QuarterlyDailyGraph(weekdays_data)


'''
3.
Analyze geographic split of the revenue and the users
Calculate average revenue per user per market
What are your observations of the results
'''
print(df_iap.head(),"\n")
#How many unique countries?
print(df_account.head(),"\n")

#first groups iap_df by account and sums all purchases for each account, then merges with account df,
#only keeping accounts with purchases
#then groups by country code and sums the purchases for all users within that country
CountryPurchases = pd.merge(df_account, df_iap.groupby('account_id').sum().reset_index(),
                            how="inner", on=["account_id", "account_id"]).groupby('country_code').sum().reset_index()
CountryPurchases=CountryPurchases.drop(['created_app_store_id', 'app_store_id'], axis=1)

#loses the package_id_hash numbers, and therefore what they are purchasing but only need revenue analysis
CountryPurchases=CountryPurchases.sort_values('iap_price_usd_cents',ascending=False)
CountryPurchases['iap_price_usd_cents'] = CountryPurchases['iap_price_usd_cents'].div(100)
print(type(CountryPurchases))
print((CountryPurchases))

#prints country Revenue in USD sorted top to bottom
#GraphFunctions.CountryRevenue(CountryPurchases)


#Lets get a graph of the user base by country.
UserBaseCountry = df_account.groupby('country_code').account_id.size().reset_index()
UserBaseCountry=UserBaseCountry.sort_values('account_id',ascending=False)
UserBaseCountry = UserBaseCountry[UserBaseCountry['account_id'] > 250]
print(UserBaseCountry)

GraphFunctions.CountryUsers(UserBaseCountry)


