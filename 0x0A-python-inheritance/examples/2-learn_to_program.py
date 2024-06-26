#!/usr/bin/python3
"""module is about"""


class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()
        # add the seconds and correct if sum is >60
        if (other_time.second + self.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second
        # add the minutes and correct if sum is > 60
        if (other_time.minute + self.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute - other_time.minute
        # add the hours and correct if sum > 24
        if (other_time.hour + self.hour) > 24:
            new_time.hour = (other_time.hour + self.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(24, 41, 30)
    print(time1 + time2)


main()
