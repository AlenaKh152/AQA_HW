import xml.etree.ElementTree as ET

with open('C:/Users/Admin/Documents/AQA_HW/products.xml', 'r',  encoding="utf-8") as file:
    data = file.read()


def total_price(text):
    root = ET.fromstring(text)
    result_price = 0
    for child in root:
        result_price += float(child[1].text) * float(child[2].text)
    return result_price


print(f'Total price: {total_price(data)}')
