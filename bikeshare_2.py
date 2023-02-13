import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# moths list
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

# week days list
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

# This function will allow the user to choose which city, month, and day
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
    city = city.lower()
    while city not in CITY_DATA:
        city = input('Sorry, invalid city name. Please try again!\n')
        city.lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Which month (january, ..., june, or all)?\n')
    month = month.lower()
    while month not in months:
        month = input('Sorry, invalid city name. Please try again!\n')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day (saturday, ..., friday, or all)?\n')
    day = day.lower()
    while day not in days:
        day = input('Sorry, invalid city name. Please try again!\n')
        day = month.lower()

    print('-'*50)
    return city, month, day

# This function will loads data for the specified city and filters by month and day if applicable.
def load_data(city, month, day):

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

# This function will displays statistics on the most frequent times of travel.
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Popular Month: ', common_month)

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The Most Popular Day Of Week: ', common_day)

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The Most Popular Hour Of Day: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

# This function will displays statistics on the most popular stations and trip.
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = str(df['Start Station'].mode()[0])
    print('The Most Common Start Station: ', common_start_station)

    # Display most commonly used end station
    common_end_station = str(df['End Station'].mode()[0])
    print('The Most Common End Station: ', common_end_station)

    # Create new column that holds combination of start station and end station
    df['Combination Of Start - End Station'] = (df['Start Station'] + ' - ' + df['End Station'])

    # Display most frequent combination of start station and end station trip
    common_trip = str(df['Combination Of Start - End Station'].mode()[0])
    print('The Most Frequent Trip From Start Station to End Station: ', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

# This function will displays statistics on the total and average trip duration.
def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time: ', total_travel_time)

    # Display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

# This function will displays statistics on the total and average trip duration.
def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time: ', total_travel_time)

    # Display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

# This function will displays statistics on bikeshare users.
def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts Of Each User Type:\n', user_type)
    print()

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Counts Of Each Gender:\n', gender_counts)
        print()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')
        while user_input.lower() not in ['yes','no']:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()

        n = 0
        while True:
            if user_input == 'yes':
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('Would you like to see more data? (Enter:Yes/No).\n')
                while user_input.lower() not in ['yes','no']:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower() 
            else:
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
        


