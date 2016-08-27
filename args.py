import argparse

def parse_args():
    arg_parser = argparse.ArgumentParser()

    # Help messages for each option
    helps = {}
    helps['source'] = 'Source JSON file to convert'
    helps['output'] = 'Destination file name (full path)'

    arg_parser.add_argument(
        'source_json_file',
        help=helps['source']
    ) 

    arg_parser.add_argument(
        '-o', '--output',
        help=helps['output'],
        metavar='FULL_FILE_PATH'
    ) 

    return arg_parser.parse_args()
