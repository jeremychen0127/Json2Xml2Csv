from lxml import etree
from types import ListType
from json_to_xml_utils import *
from args import *

def children_to_dict(xml_element):
  children_dict = {}
  for child_element in xml_element:
    child_dict = element_to_dict(child_element)
    new_value = child_dict[child_element.tag]
    if children_dict.has_key(child_element.tag):
      existing_value = children_dict[child_element.tag]
      if existing_value is ListType:
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


def xml_to_json(xml_element):
  """
  Returns JSON object converted from xml tree object
  :type xml: XML Element Object
  """
  result_dict = element_to_dict(xml_element)

  return json.dumps(result_dict, indent=2)


def main():
  start_time = time.time()
  print("Start Processing...")

  # Get arguments
#args = parse_args()

  # Load the JSON
  print("Loading XML file..."),
  sys.stdout.flush()
  xml_data = etree.parse("sample.xml")
  root = xml_data.getroot()
  print("\rLoading XML file...[Completed]")

  print("Converting to JSON..."),
  sys.stdout.flush()

  # Process the JSON
  json_object = xml_to_json(root)

  print("\rConverting to JSON...[Completed]")

  print("Writing to file..."),
  sys.stdout.flush()

  # Determine the output file name
#  if args.output:
#    output_file_name = args.output
#  else:
#    output_file_name = args.source_xml_file.split('.xml')[0] + '.json'

  # Open the output file for writing
  output_file = open("sam.json", 'w')

  # Writes the XML pretty string to file
  output_file.write(json_object)
  print("\rWriting to file...[Completed]")

  # Calculate the processing time
  end_time = time.time()
  processing_time = end_time - start_time
  print("COMPLETED: XML -> JSON in %.5f seconds" % processing_time)


if __name__ == "__main__":
  main()
