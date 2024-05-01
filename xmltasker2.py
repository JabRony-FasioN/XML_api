import xml.etree.ElementTree as ET
import re

with open('Task2.xml', 'r') as xml_file:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    if root[0].text:
        text_parts = root[0].text.split('\n')  # Разбиваем текст по символам новой строки
        reversed_text = '\n'.join([part[::-1] for part in text_parts])  # Переворачиваем каждую часть и объединяем обратно
        root[0].text = reversed_text

    if root[1].text:
        text_parts = re.sub(r'\D','', root[1].text)  #регулярное выражение для вывода только цифр
        root[1].text = text_parts


    if root[2].text:
        text_parts = re.sub(r'\d+','', root[2].text) #регулярное выражение для вывода только цифр
        root[2].text = text_parts

   
    if root[3].text: # кол-во пробелов и абзацев
        space_count = 0
        for char in root[3].text:
            if char.isspace():
                space_count+=1
        root[3].text = str(space_count)

    
    tree.write('Task2.xml') #обновление файла
