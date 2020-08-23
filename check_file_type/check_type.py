import json
import argparse
import yaml


def _check_type(loader, data, error):
    try:
        loader(data)
        return True
    except error:
        return False

def is_json(data):
    return _check_type(json.loads, data, ValueError)

def is_yaml(data):
    return _check_type(yaml.safe_load, data, yaml.scanner.ScannerError)

def check_type():
    usage = "check_type -f file.json -t json"
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('-f', '--file',
                        help="File for which type need to check")
    parser.add_argument('-i', '--is_type',
                        help="Type of file to check")
    args = parser.parse_args()
    fh = open(args.file, "r")
    data = fh.read()
    result = 'unknown'
    if args.is_type == 'json':
        result =  is_json(data)
    elif args.is_type == 'yaml':
        # Every json file can be loaded as yaml file so
        # return the result False if file is json loadable
        result = is_yaml(data) and not is_json(data)
    else:
        raise Exception("Only json or yaml format type are supported for now")
    print(result)
