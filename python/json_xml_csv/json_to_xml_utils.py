import json
import sys
import time
from types import *
from lxml import etree

def isPrimitive(value):
  """
  Returns True if value is one of the following:
    * boolean, int, long, float, string, unicode character
  and False otherwise
  """
  PRIMITIVES = [BooleanType, StringType, UnicodeType, FloatType, IntType, LongType]
  return type(value) in PRIMITIVES


def json_array_to_xml(key, values):
  # Initialize list of XML elements
  element_list = []

  # For each member, say X, of the array, create an XML element with
  # name=key and process X
  for value in values:
    parent = key_value_to_xml(key, value)[0]
    element_list.append(parent)

  return element_list


def key_value_to_xml(key, value):
  # Initialize list of XML elements
  element_list = []

  # Primitive Value: Create element(s) with name=key and set value to the text
  if isPrimitive(value):
    parent = etree.Element(key)

    # Set value to text of the element
    parent.text = str(value).lower()

    # Add the element to the list
    element_list.append(parent)

  # Object Value: Create a parent element with name=key and recursively process value
  elif type(value) is DictType:
    parent = etree.Element(key)

    # Process all the key-value pairs in the current value
    for child_key, child_value in value.items():

      # Recursively process value by applying responding functions
      if type(child_value) is ListType:
        child_element_list = json_array_to_xml(child_key, child_value)
      else:
        child_element_list = key_value_to_xml(child_key, child_value)

      # Add all the children to the parent element
      for element in child_element_list:
        parent.append(element)

    # Add the processed element to the list
    element_list.append(parent)

  # Array Value: Create elements with name=key
  elif type(value) is ListType:
    element_list = json_array_to_xml(key, value)

  return element_list
