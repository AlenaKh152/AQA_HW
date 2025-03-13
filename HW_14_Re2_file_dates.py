import re

file = open('C:/Users/Admin/Documents/AQA_HW/Dates_file.txt', 'r')
text = file.read()

pattern = r"\d{2}\.\d{2}\.\d{4}"
match = re.findall(pattern, text)

for date in match:
    print(date)
