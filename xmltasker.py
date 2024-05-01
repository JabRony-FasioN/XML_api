import xml.etree.ElementTree as ET 
keys = ['type', 'birthDate', 'name', 'surname', 'prefix']
typer = {'10':'ADT', '8':'CHD', '7':'INF'}
def get_str(url): #парсинг из файла и фильтрация данных
    tree = ET.parse(url)
    root = tree.getroot()
    arr = []
    for x in root.iter():
        if x.text is None:
            pass
        else:
            arr.append(list(filter(None,x.text.split("|"))))
    arr.pop(0)
    return arr

url = 'Task1.xml'
root = ET.Element("touristInfo") #родительский тег
container =[]
data = get_str(url)
for i in data:
    do = ET.SubElement(root, "touristGroup")# дочерний тег
    for j in i: # дочерние теги с атрибутами из полученых файлов
        x = dict(zip(keys,j.split("/")))
        myattrib = dict(list(x.items())[0:1])
        myattrib = dict(type=typer[myattrib['type']])
        myattrib2 = dict(list(x.items())[1:2])
        if myattrib2['birthDate'] != "null": # исключение атрибута если его нет
            myattrib = dict(myattrib.items() | myattrib2.items())
        doc = ET.SubElement(do, "tourist", attrib= myattrib)
        ET.SubElement(doc, 'prefix').text = x['prefix']
        ET.SubElement(doc, 'name').text = x['name']
        ET.SubElement(doc, 'surname').text = x['surname']
    
tree = ET.ElementTree(root) # сосздание структуры xml файла
tree.write('output.xml') # вывод