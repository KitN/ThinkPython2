"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def print_time(self):
        """Prints a string representation of the time.

        t: Time object
        """
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        """Computes the number of seconds since midnight.

        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time




def add_times(t1, t2):
    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = t1.time_to_int() + t2.time_to_int()
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    noon_time.print_time()

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    run_time.print_time()

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print('Ends at', end=' ')
    end_time.print_time()


if __name__ == '__main__':
    main()
