import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_name = ''
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    bikeshare_cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('\nEnter a city, either chicago, new york city or washington: ')
        if city in bikeshare_cities:
            break
        else:
            print("You've entered an invalid city. Please retry\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_choices = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nEnter a month january, february, ... , june or all: ')
        if month in month_choices:
            break
        else:
            print("You've entered an invalid month. Please retry\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_choices = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input("\nEnter day of the week or 'all': ")
        if day in day_choices:
            break
        else:
            print("You've entered an invalid day. Please retry\n")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

   # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # months = ['january', 'february', 'march', 'april', 'may', 'june']
    # month_num = df['Start Time'].dt.month.mode()
    # print("The most common month to travel is {}.\n".format(months[int(month_num)]).title())
    # Note: Previous 3 lines work when entering a month name, but fail when using 'all'

    print("The most common month to travel is {}.\n".format(df['Start Time'].dt.month.mode()))

    # TO DO: display the most common day of week
    print("The most common day of the week is {}.\n".format(df['Start Time'].dt.weekday_name.mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is {}.\n".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used Start Station is {}.\n".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used End Station is {}.\n".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Stations'] = df['Start Station'] + " and " + df['End Station']
    print("The most commonly used combinations of Starting and Ending Stations is {}.\n".format(df['Start End Stations'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total time spent for all trips taken is {} minutes.\n".format((df['Trip Duration'].sum())/60))

    # TO DO: display mean travel time
    print("The average trip duration is {} minutes.\n".format((df['Trip Duration'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Total trips by user type:\n {} \n'.format(df['User Type'].value_counts()))

    if city != 'washington':
        # TO DO: Display counts of gender
        print('Total trips by gender:\n{} \n'.format(df['Gender'].value_counts()))
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest birth year recorded is: {:.0f} \n'.format(df['Birth Year'].min()))
        print('The most recent birth year is: {:.0f} \n'.format(df['Birth Year'].max()))
        print('The most common year of birth is: {:.0f} \n'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
