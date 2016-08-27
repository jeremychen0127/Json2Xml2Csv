import json
from types import *
from lxml import etree

def isPrimitive(value):
  PRIMITIVES = [BooleanType, StringType, UnicodeType, FloatType, IntType, LongType]
  return type(value) in PRIMITIVES

def json_array_to_xml(key, values):
  element_list = []

  for value in values:
    parent = json_to_xml(key, value)[0]
    element_list.append(parent)

  return element_list


def json_to_xml(key, value):
  element_list = []

  if isPrimitive(value):
    parent = etree.Element(key)
    parent.text = str(value).lower()
    element_list.append(parent)
  elif type(value) is DictType:
    parent = etree.Element(key)
    for child_key, child_value in value.items():
      if type(child_value) is ListType:
        child_element_list = json_array_to_xml(child_key, child_value)
      else:
        child_element_list = json_to_xml(child_key, child_value)

      for element in child_element_list:
        parent.append(element)

    element_list.append(parent)
  elif type(value) is ListType:
    element_list = json_array_to_xml(key, value)

  return element_list

def main():
  with open('sample1.json') as json_data_file:
    json_data = json.load(json_data_file)

    xml_pretty_string = ''
    for key, value in json_data.items():
      if type(value) is ListType:
        element_list = json_array_to_xml(key, value)
      else:
        element_list = json_to_xml(key, value)

      for element in element_list:
        xml_pretty_string += etree.tostring(element, pretty_print=True)

    print xml_pretty_string

    output_file = open('sample.xml', 'w')
    output_file.write(xml_pretty_string)


if __name__ == "__main__":
  main()
