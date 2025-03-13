import re

with open('Dates_file.txt', 'r', encoding="utf-8") as file:
    text = file.read()

pattern = r"\d{2}\.\d{2}\.\d{4}"
match = re.findall(pattern, text)

for date in match:
    print(date)
