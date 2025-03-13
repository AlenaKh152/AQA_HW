import xml.etree.ElementTree as ET

file = open('C:/Users/Admin/Documents/AQA_HW/products.xml', 'r')
text = file.read()


def parseXML(text):
    root = ET.fromstring(text)
    result_price = 0
    for child in root:
        result_price += float(child[1].text) * float(child[2].text)
    return result_price


print(f'Total price: {parseXML(text)}')
