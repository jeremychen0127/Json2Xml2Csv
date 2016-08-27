from lxml import etree
from types import ListType
from json_to_xml_utils import *
from args import *

def json_to_xml(json):
  """
  Returns XML pretty print string converted from json object
  :type json: python dictionary
  """
  xml_pretty_string = ''
  for key, value in json.items():
    if type(value) is ListType:
      element_list = json_array_to_xml(key, value)
    else:
      element_list = key_value_to_xml(key, value)

    for element in element_list:
      xml_pretty_string += etree.tostring(element, pretty_print=True)

  return xml_pretty_string


def main():
  start_time = time.time()
  print("Start Processing...")

  # Get arguments
  args = parse_args()

  # Open the input JSON file
  with open(args.source_json_file) as json_data_file:

    # Load the JSON
    print("Loading JSON file..."),
    sys.stdout.flush()
    json_data = json.load(json_data_file)
    print("\rLoading JSON file...[Completed]")

    print("Converting to XML..."),
    sys.stdout.flush()

    # Process the JSON
    xml_pretty_string = json_to_xml(json_data)

    print("\rConverting to XML...[Completed]")

    print("Writing to file..."),
    sys.stdout.flush()

    # Determine the output file name
    if args.output:
      output_file_name = args.output
    else:
      output_file_name = args.source_json_file.split('.json')[0] + '.xml'

    # Open the output file for writing
    output_file = open(output_file_name, 'w')

    # Writes the XML pretty string to file
    output_file.write(xml_pretty_string)
    print("\rWriting to file...[Completed]")

    # Calculate the processing time
    end_time = time.time()
    processing_time = end_time - start_time
    print("COMPLETED: JSON -> XML in %.5f seconds" % processing_time)


if __name__ == "__main__":
  main()
