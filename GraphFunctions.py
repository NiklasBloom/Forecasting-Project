import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def DAUgraph(df_date_group):
    plt.figure(figsize=(12, 7))
    plt.xticks(fontsize=8, rotation=45)
    p = plt.plot(df_date_group.index, df_date_group.values, color='skyblue')
    plt.title('Daily Active Users Yearly')
    plt.xlabel('Time by Months')
    plt.ylabel('Daily Active Users')
    xValues = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01', '2016-07-01',
               '2016-08-01'
        , '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01', '2016-12-31']
    plt.xticks(xValues)
    plt.show()

def DailyGraph(week_df):
    #plot day of week DAU as bar graph
    #Plot the bar graph
    plt.figure(figsize=(12, 7))
    plt.bar(week_df['date'], week_df['account_id'], color='skyblue')
    plt.title('Daily Active Users by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Daily Active Users')
    plt.xticks(rotation=45)
    plt.show()

def QuarterlyDailyGraph(weekdays_data):

    #Now access the data for each day of the week:
    Mondays = weekdays_data['Monday']
    Tuesdays = weekdays_data['Tuesday']
    Wednesdays = weekdays_data['Wednesday']
    Thursdays = weekdays_data['Thursday']
    Fridays = weekdays_data['Friday']
    Saturdays = weekdays_data['Saturday']
    Sundays = weekdays_data['Sunday']


    #assign Values from each day to respective list
    Mondays_values = np.array(Mondays.values)
    Tuesdays_values = np.array(Tuesdays.values)
    Wednesdays_values = np.array(Wednesdays.values)
    Thursdays_values = np.array(Thursdays.values)
    Fridays_values = np.array(Fridays.values)
    Saturdays_values = np.array(Saturdays.values)
    Sundays_values = np.array(Sundays.values)
    #Generate a color palette using Tableau's color blind 10 palette for better visibility and aesthetics
    colors = plt.get_cmap('tab10').colors

    N = 4
    ind = np.arange(N)
    width = 0.1

    #Create the figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    #Creates bars
    bar1 = ax.bar(ind, Mondays_values, width, color=colors[0], label='Monday')
    bar2 = ax.bar(ind + width, Tuesdays_values, width, color=colors[1], label='Tuesday')
    bar3 = ax.bar(ind + width * 2, Wednesdays_values, width, color=colors[2], label='Wednesday')
    bar4 = ax.bar(ind + width * 3, Thursdays_values, width, color=colors[3], label='Thursday')
    bar5 = ax.bar(ind + width * 4, Fridays_values, width, color=colors[4], label='Friday')
    bar6 = ax.bar(ind + width * 5, Saturdays_values, width, color=colors[5], label='Saturday')
    bar7 = ax.bar(ind + width * 6, Sundays_values, width, color=colors[6], label='Sunday')

    #Set the x-axis label, y-axis label, title, and x-tick marks
    ax.set_xlabel("Quarters", fontsize=14, labelpad=15)
    ax.set_ylabel('Average DAU', fontsize=14, labelpad=15)
    ax.set_title("Average Daily Active Users by Day and Quarter", fontsize=16, pad=20)
    ax.set_xticks(ind + width * 3)
    ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'], fontsize=12)

    #Adds gridlines below the bars
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

    #Set the legend to right and adds title
    legend = ax.legend(title="Days", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
    legend.get_title().set_fontsize('13')

    #Show plot
    plt.tight_layout()
    plt.show()

def CountryRevenue(CountryPurchases):
    #style
    sns.set_style("whitegrid")

    #Plot bar graph
    plt.figure(figsize=(12, 7))
    txt="Countries with less than 250 registered users are dropped from the graph"
    plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
    bars = sns.barplot(x='country_code', y='iap_price_usd_cents', data=CountryPurchases, palette='husl')

    #Set title and labels
    plt.title('Geographic Revenue Split', fontsize=18)
    plt.xlabel('Countries', fontsize=14)
    plt.ylabel('Revenue (USD)', fontsize=14)

    #Rotate x-axis labels
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    #remove scientific notation
    plt.ticklabel_format(style='plain', axis='y')

    #Add bar values
    for bar in bars.patches:
        plt.annotate(format(bar.get_height(), '.2f'),
                     (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     ha='center', va='center',
                     size=10, xytext=(0, 8),
                     textcoords='offset points', rotation=45)


    #Remove the left and top spines
    sns.despine(left=True, top=True)

    #Show plot
    plt.tight_layout()
    plt.show()


def CountryUsers(UserBaseCountry):
    #style
    sns.set_style("whitegrid")

    #Plot bar graph
    plt.figure(figsize=(12, 7))
    bars = sns.barplot(x='country_code', y='account_id', data=UserBaseCountry, palette='husl')

    #Set title and labels
    plt.title('User Base by Country', fontsize=18)
    plt.xlabel('Countries', fontsize=14)
    plt.ylabel('Registered Users', fontsize=14)

    #Rotate x-axis labels
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    #remove scientific notation
    plt.ticklabel_format(style='plain', axis='y')

    '''
    #Add bar values
    for bar in bars.patches:
        plt.annotate(format(bar.get_height(), '.2f'),
                     (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     ha='center', va='center',
                     size=10, xytext=(0, 8),
                     textcoords='offset points', rotation=45)
    '''

    #Remove the left and top spines
    sns.despine(left=True, top=True)

    #Show plot
    plt.tight_layout()
    plt.show()