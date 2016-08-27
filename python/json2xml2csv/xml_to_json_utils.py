from lxml import etree
from types import ListType


def children_to_dict(xml_element):
  children_dict = {}
  for child_element in xml_element:
    child_dict = element_to_dict(child_element)
    new_value = child_dict[child_element.tag]

    if children_dict.has_key(child_element.tag):
      existing_value = children_dict[child_element.tag]

      if type(existing_value) is ListType:
        children_dict[child_element.tag].append(new_value)
      else:
        children_dict[child_element.tag] = [existing_value, new_value]

    else:
      children_dict[child_element.tag] = new_value

  return children_dict

def element_to_dict(xml_element):
  result_dict = {}

  if len(xml_element):
    children_dict = children_to_dict(xml_element)
    result_dict[xml_element.tag] = children_dict

  elif xml_element.text:
    result_dict[xml_element.tag] = xml_element.text

  return result_dict
