import json
from types import *
from lxml import etree

def json_to_xml(key, value):
  parent = etree.Element(key)

  if type(value) is BooleanType:
    parent.text = value
  elif type(value) is StringType:
    parent.text = value
  elif type(value) is UnicodeType:
    parent.text = value
  elif type(value) is FloatType:
    parent.text = value
  elif type(value) is IntType:
    parent.text = value
  elif type(value) is LongType:
    parent.text = value
  elif type(value) is DictType:
    for child_key, child_value in value.items():
      child_xml = json_to_xml(child_key, child_value)
      parent.append(child_xml)

  return parent

def main():
  with open('sample.json') as json_data_file:
    json_data = json.load(json_data_file)

    for key, value in json_data.items():
      xml = json_to_xml(key, value)

    xml_pretty = etree.tostring(xml, pretty_print=True)
    print xml_pretty
    xml_tree = etree.ElementTree(xml)
    xml_tree.write('sample.xml', pretty_print=True)


if __name__ == "__main__":
  main()
