import sys
import time
import json
from lxml import etree
from xml_to_json_utils import *
from args import *


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
