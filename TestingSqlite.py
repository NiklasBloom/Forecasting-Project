import sqlite3

#Create a SQL connection to the SQLite database
con = sqlite3.connect("sample.sqlite")

cur = con.cursor()

#Prints SQlite information from the pragma tables, table information and names,
#Queries the table name, queries for listed column names, and print all information from SQLite_Master table
#iterates over tables to print

# table information from the website
#______________________________
#The database contains three tables:
#account, account_date_session and iap_purchase.
#account contains user profiles, iap_purchase contains in-app purchases by the users,
#and account_date_session contains the number of sessions for the users for the days they
#have been active.
#All the tables contain data for the year of 2016.

# Queries Table names
for row in cur.execute('SELECT name FROM sqlite_master'):
    print(row)


# Listed Column names
#account: "account_id" text , "created_time" timestamp, "created_device" text, "created_platform" text, "country_code" text, "created_app_store_id" int
#account_date_session: "account_id" text, "created_time" timestamp , "package_id_hash" text, "iap_price_usd_cents" int, "app_store_id" int
#iap_purchase: "account_id" text, "date" date, "session_count" int, "session_duration_sec" int


# prints all table information from the sqlite_master
for row in cur.execute('SELECT * FROM sqlite_master'):
    print(row)


# iterates over SQlite table to print
for row in cur.execute('SELECT * FROM iap_purchase LIMIT 2;'):
    print(row)
