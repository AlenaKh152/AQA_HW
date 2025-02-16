# 1 Time
n = 545
hours = n // 60
minutes = n - hours * 60

cur_time_str = str(hours) + str(minutes)
cur_time_tuple = (int(cur_time_str[i]) for i in range(len(cur_time_str)))
print(sum(cur_time_tuple))

# 2 Level Up
experience = 10
threshold = 15
reward = 5

if experience + reward >= threshold:
    print('true')
else:
    print('false')

# 3 Time Converter
time = '00:15'
time_list = time.split(':')

hours = int(time_list[0])

if hours < 10:                                     # если часы меньше 10 - не пишите '0' перед ними
    time_list[0] = str(hours)

am = ' a.m.'
pm = ' p.m.'

if hours == 0:                                     # с 00:00 до 00:59
    time_list[0] = str(hours + 12)
    converted_time = (':').join(time_list) + am
elif 12 < hours <= 23:                             # с 13:00 до 23:59
    time_list[0] = str(hours - 12)
    converted_time = (':').join(time_list) + pm
elif hours == 12:                                  # с 12:00 до 12:59
    converted_time = (':').join(time_list) + pm
else:                                              # с 01:00 до 11:59
    converted_time = (':').join(time_list) + am

print(converted_time)
