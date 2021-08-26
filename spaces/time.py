import time

class Time:
    def time_difference_minutes(time1, time2):
        time1_arr = [int(time) for time in time1.split(':')]
        time2_arr = [int(time) for time in time2.split(':')]

        time1_min = time1_arr[0] * 60 + time1_arr[1] 
        time2_min = time2_arr[0] * 60 + time2_arr[1]

        return time2_min - time1_min

    def current_time():
        return time.strftime("%H:%M:%S", time.localtime())

