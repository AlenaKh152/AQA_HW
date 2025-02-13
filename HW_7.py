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
time = '00:30'
time_list = time.split(':')

if int(time_list[0]) < 10:                         # если часы меньше 10 - не пишите '0' перед ними
    time_list[0] = str(int(time_list[0]))

am = ' a.m.'
pm = ' p.m.'

if int(time_list[0]) == 0:                         # с 00:00 до 00:59
    time_list[0] = str(int(time_list[0]) + 12)
    converted_time = (':').join(time_list) + am
elif 12 < int(time_list[0]) <= 23:                 # с 13:00 до 23:59
    time_list[0] = str(int(time_list[0]) - 12)
    converted_time = (':').join(time_list) + pm
elif int(time_list[0]) == 12:                      # с 12:00 до 12:59
    converted_time = (':').join(time_list) + pm
else:                                              # с 01:00 до 11:59
    converted_time = (':').join(time_list) + am

print(converted_time)
