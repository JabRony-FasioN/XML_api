import xml.etree.ElementTree as ET

ET.register_namespace('','http://www.opentravel.org/OTA/2003/05')
tree = ET.parse('Task3.xml')
root = tree.getroot()


# 6. Перенос элемента 'DescriptiveText' в атрибут 'Service'
descriptive_text_elements = root.findall(".//{http://www.opentravel.org/OTA/2003/05}Service") # получение родительский
for element in descriptive_text_elements: # Проход по найденным элементам
    descriptive_text = element.text
    child_tags= element.findall(".//{http://www.opentravel.org/OTA/2003/05}DescriptiveText") # получение дочерних
    for i in child_tags:
        element.set('DescriptiveText', i.text ) # кстановака атрибутов
        element.remove(i)


def process_element(element):
    
    for child in list(element): # Обработка дочерних элементов

        if child.tag in ['{http://www.opentravel.org/OTA/2003/05}ContactInfo', '{http://www.opentravel.org/OTA/2003/05}MultimediaDescription', '{http://www.opentravel.org/OTA/2003/05}ImageFormat']:         # 1. Поднять потомков элементов 'ContactInfo', 'MultimediaDescription', 'ImageFormat' на уровень выше
            element.remove(child)
            element.extend(child)
        elif 'rds' in child.tag:  # 2. Удалить элементы, в имени которых встречается 'rds', перенося их дочерние элементы на уровень выше
            element.remove(child)
            element.extend(child)
        elif 'Caption' in child.attrib:   # 3. Атрибут 'Caption' становится дочерним элементом

            caption = child.attrib['Caption']
            child.attrib.pop('Caption')
            caption_element = ET.Element('Caption')
            caption_element.text = caption
            element.append(caption_element)
        if child.tag == '{http://www.opentravel.org/OTA/2003/05}Description':         # 4. Оставляем только один элемент 'Description' с самым длинным текстом
            number = element.findall('{http://www.opentravel.org/OTA/2003/05}Description')
            if len(number) > 1:
                max_len_desc = max(element.findall('{http://www.opentravel.org/OTA/2003/05}Description'), key=lambda x: len(x.text), default=0)
                if child != max_len_desc:
                    element.remove(child)
        if child.text:   # 5. Удалить символы ©, ¶, ∑, Œ из текста
            child.text = child.text.replace('©', '').replace('¶', '').replace('∑', '').replace('Œ', '')
        process_element(child)

process_element(root) # Применяем функцию process_element к корневому элементу




tree.write('Task3.xml') # Запись обработанного XML обратно в файл
