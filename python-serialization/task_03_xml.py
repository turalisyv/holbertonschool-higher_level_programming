#!/usr/bin/python3
'''
My module document
'''


def serialize_to_xml(sample_dict, xml_file):
    res = "<data>"
    for key, value in zip(sample_dict.keys(), sample_dict.values()):
        res = res + "\n" + 4 * " " + "<{}>{}</{}>".format(key, value, key)
    res = res + "\n" + "</data>"

    with open(xml_file, mode='w', encoding='utf-8') as j:
        j.write(res)

def deserialize_from_xml(xml_file):
    import xml.etree.ElementTree as ET
    import json

    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {}
    for i in range(len(root)):
        data.update({root[i].tag : root[i].text})
    
    with open('data.json', mode='w', encoding='utf-8') as j:
        json.dump(data, j)
    
    return data
