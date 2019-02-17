import pandas as pd
from datetime import datetime
from datetime import timedelta
import time
import calendar
import numpy as np


'''
CSV files:
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
'''

def city_filter():
    """Define function to prompt user to specify a city to analyze
    """
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nGood day! Let\'s explore some US bikeshare data!\n'
                     'Please choose from one of the following cities to begin:\n Chicago \n New York \n Washington\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower () == 'washington':
            return 'washington.csv'
        else:
            print('Please try again by typing one of the 3 cities above.')

def add_time_filter():
    '''Define function to prompt for filter based on time (month and day)
    '''

    #time_filter = ''
    time_filter = input('\nWould you like to specify the data by the type of: \n month \n day\n n/a (not at all)?\n').lower()
    while time_filter not in ['month', 'day', 'n/a']:
        time_filter = input('\nPlease try again using one of the selections for above.\n').lower()
        #if time_filter not in ['month', 'day', 'n/a']:
        #print('Please try again using one of the selections for above.')
        #else:
    return time_filter

def month_filter():
    '''Define function to add month filter
    '''
    #Create a dictionary with matching months in string to single integer number
    months_dictionary = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    #create variable for to obtain user input
    month_input = input('\nPlease choose a month to filter by:\n January \n February\n March \n April \n May \n June \n').lower()
    #while the user enter values not included in months_dictionary, prompt to gather input until it is in months_dictionary'''
    while month_input not in months_dictionary.keys():
        month_input = input('Please try again by typing of the 6 months above.\n').lower()
        #month_input = input('\nPlease choose a month to filter by:\n January \n February\n March \n April \n May \n June \n')
    #else:
    #while loop is completed when month_input is in months_dictionary
    month = months_dictionary[month_input]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def day_filter():
    '''Defines function to add a day filter
    '''
    #obtain first output of the month_filter function
    current_month = month_filter()[0]
    #obtain month portion of the start month, e.g., 2017-05, this will take only 05, and convert to integer
    month = int(current_month[5:])
    days_dictionary = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
    #obtain day input from user
    day_input = input('\nPlease type the day of the week would you like to filter by:\n Monday\n Tuesday\n Wednesday\n Thursday\n Friday\n Saturday\n Sunday\n').lower()
    #ensure input is part of the days_dictionary, while it's not, continue to prompt user to input a new string
    while day_input not in days_dictionary.keys():
        day_input = input('Please type a day of the week such as monday, tuesday, etc.\n').lower()
    #while loop completes, assign day varaible to the value to the correpsonding key in the days_dictionary
    day = days_dictionary[day_input]
    #convert day input into integer
    day = int(day)
    start_date = datetime(2017, month, day)
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

#Begin to calculate statistics based on the data
def popular_month(df):
    '''Determine the most poular month
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    #extract month out of start time, and find mode of
    mode_month = df['start_time'].dt.month.mode()
    #convert month (integer) to month (words) using months list. -1 is required due to list's 0 refrence indexing
    most_popular_month = months[int(mode_month) - 1]
    print('The most popular month for using bikeshare is {}.'.format(most_popular_month))

def popular_day(df):
    '''Determine the most popular day
    '''
    days_of_week = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #extract dayofweek out of start time column, find mode
    mode_day = int(df['start_time'].dt.dayofweek.mode())
    most_popular_day = days_of_week[mode_day]
    print('The most popular day of week for using bikeshare is {}.'.format(most_popular_day))

def popular_hour(df):
    '''Determine popular hour
    '''
    #set am or pm
    mode_hour = df['start_time'].dt.hour.mode()
    mode_hour = int(mode_hour)
    if mode_hour == 0:
        printed_hour = 12
        time_of_day = 'midnight'
    elif 1 <= mode_hour < 13:
        printed_hour = mode_hour
        time_of_day = 'am'
    elif 13 <= mode_hour < 24:
        printed_hour = mode_hour - 12
        time_of_day = 'pm'
    elif mode_hour == 12:
        printed_hour = 12
        time_of_day = 'noon'
    print('The most popular start time for using bikeshare is {}{}.'.format(printed_hour, time_of_day))

def trip_duration(df):
    '''Determine total trip duration
    '''
    total_duration = int(df['trip_duration'].sum())
    #total_duration = int(total_duration)
    duration_minutes = int(total_duration / 60)
    #duration_minutes = int(duration_minutes)
    duration_hours = duration_minutes / 60
    duration_hours = round(duration_hours,2)
    print('The total trip duration for your specified time period is the equivalent of {} seconds, {} minutes, or {} hours.'.format(total_duration, duration_minutes, duration_hours))
    # calculate average duration
    average_duration = int(df['trip_duration'].mean())
    #average_duration = int(average_duration)
    average_duration_minutes = int(average_duration / 60)
    #average_duration_minutes = int(average_duration_minutes)
    average_duration_hours = average_duration_minutes / 60
    average_duration_hours = round(average_duration_hours,2)
    print('The average trip duration using bikeshare is the equivalent of {} seconds, {} minutes, or {} hours.'.format(average_duration, average_duration_minutes, average_duration_hours))

def popular_stations(df):
    '''Determine most popular station for start and end
    '''
    popular_start_station = df['start_station'].mode().to_string(index = False)
    popular_end_station = df['end_station'].mode().to_string(index = False)
    print('The most popular start station using bikeshare is {}.'.format(popular_start_station))
    print('The most popular end station using bikeshare is {}.'.format(popular_end_station))

def popular_trip(df):
    '''Determine most popular trip
    '''
    most_popular_trip = df['trip'].mode().to_string(index = False)
    print('The most popular trip using bikeshare is {}.'.format(most_popular_trip))

def users(df):
    '''Determine number of subscribers and customers that uses bikeshare
    '''
    subscriber = df.query('user_type == "Subscriber"').user_type.count()
    customer = df.query('user_type == "Customer"').user_type.count()
    print('There are {} subscribers and {} customers using bikeshare.'.format(subscriber, customer))

def gender(df):
    '''Determine number of males and females that uses bikeshare
    '''
    number_males = df.query('gender == "Male"').gender.count()
    number_females = df.query('gender == "Female"').gender.count()
    print('There are {} males and {} females using the bikeshare service.'.format(number_males, number_females))

def birth_years(df):
    '''Determine birth year of the oldest, youngest, and most common
    '''
    minimum = df['birth_year'].min()
    maximum = df['birth_year'].max()
    mode = df['birth_year'].mode()
    print('The oldest users are born in the year {}, the youngest are born in {}, and the most common birth year is {}.'.format(int(minimum), int(maximum), int(mode)))

def raw_data(df):
    '''Obtain user input to determine if a portion of the raw data is to be displayed, if input is Yes, then raw data will be displayed.
    User will be prompted again to see if more raw data is to be displayed, next portion of the raw data will be displayed until user input is no
    '''
    start = 0
    end = 5
    data = ''
    data = input('\nWould you like to view the raw data? (Yes or No).\n')
    input_list = ['yes', 'no']
    #while the answer is not yes or no, keep on asking for yes or no until yes or no is the answer
    while data.lower() not in input_list:
        data = input('Incorrect input. Please try again by answering yes or no.\n')


    if data.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[start:end])
        more_data = input('\nWould you like to view more raw data? (Yes or No).\n')
        #check to see if input provided is yes or no, keep on asking the same question if not yes or no
        while more_data.lower() not in input_list:
            more_data = input('Incorrect input. Please try again by answering yes or no.\n')
        #once determined it is yes or no, then go into if statement
        while more_data.lower() == 'yes':
            start += 5
            end += 5
            print(df[df.columns[0:-1]].iloc[start:end])
            more_data = input('\nWould you like to view more raw data? (Yes or No).\n')
            while more_data.lower() not in input_list:
                more_data = input('Incorrect input. Please try again by answering yes or no.\n')
            if more_data == 'no':
                print ('thanks for using this file!')
            break
    elif data.lower()== 'no':
        print ('okay, no more')

def statistics():
    '''
    Function prompts user to request descriptive statistics
    '''
    # add city filter
    city = city_filter()
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    # format with underscores in column name
    format_column = []
    for col in df.columns:
        format_column.append(col.replace(' ', '_').lower())
    df.columns = format_column
    # add new trip column
    df['trip'] = df['start_station'].str.cat(df['end_station'], sep=' - ')

    # filter based on time
    time_filter = add_time_filter()
    if time_filter == 'n/a':
        df_end = df
    elif time_filter == 'month' or time_filter == 'day':
        if time_filter == 'month':
            low_range, high_range = month_filter()
        elif time_filter == 'day':
            low_range, high_range = day_filter()
        print('Filtering based on selected time period...')
        df_end = df[(df['start_time'] >= low_range) & (df['start_time'] < high_range)]


    if time_filter == 'n/a':
        start_time = time.time()

#Display summary of statistics

        # Most popular start month
        popular_month(df_end)
        print("Seconds to calcuate: %s." % (time.time() - start_time))


    if time_filter == 'n/a' or time_filter == 'month':
        start_time = time.time()

        # Most popular start day
        popular_day(df_end)
        print("Seconds to calculate: %s." % (time.time() - start_time))
        start_time = time.time()

    # most popular start hour
    popular_hour(df_end)
    start_time = time.time()
    print("Seconds to calculate: %s." % (time.time() - start_time))

    # total and average time duration
    trip_duration(df_end)
    print("Seconds to calculate: %s." % (time.time() - start_time))
    start_time = time.time()

    # most popular start and end stations
    popular_stations(df_end)
    print("Seconds to calculate: %s." % (time.time() - start_time))
    start_time = time.time()

    # most popular trip
    popular_trip(df_end)
    print("Seconds to calculate: %s." % (time.time() - start_time))
    start_time = time.time()

    # user type count
    users(df_end)
    print("Seconds to calculate: %s." % (time.time() - start_time))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
              start_time = time.time()

              # gender counts
              gender(df_end)
              print("Seconds to calculate: %s." % (time.time() - start_time))
              start_time = time.time()

              # oldest and youngest users plus most popular birth year
              birth_years(df_end)
              print("Seconds to calculate: %s." % (time.time() - start_time))

    raw_data(df_end)

    # restart questions
    restart = input('\nWould you like to restart? (yes or no)\n').lower()
    while restart not in ['yes','no']:
        restart = input('Incorrect input. Please try again by typing yes or no.\n').lower()
        #restart = input('\nWould you like to restart? (yes or no)\n').lower()
    #while loop completes
    if restart == 'yes':
        statistics()
    else:
        exit()


if __name__ == "__main__":
    statistics()
