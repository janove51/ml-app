import sys
import json
from pathlib import Path      # makes file paths OS agnostic
from importlib import import_module


# Fetch config file from std. input: todo: use config parser
def fetch_std_input(std_input):

    if len(std_input) > 1:
        config_file_path = std_input[1]
    else:
        raise Exception("File path to config file required")

    return(config_file_path)


def read_config(config_file_path):

    config_file_path = Path(config_file_path)

    with open(config_file_path) as f:
        config = json.load(f)

    # Task parameters
    task_definition = config['task']
    print("Task:", task_definition)

    # Input parameters
    input_config = config['input']
    input_path = Path(input_config['path'] + input_config['name'])
    print("input_path:", input_path)

    # Output parameters
    output_config = config['output']
    output_path = Path(output_config['path'] + output_config['name'])
    print("output_path:", output_path)

    return task_definition, input_path, output_path


def import_use_case(task_definition, module_parent = 'use_cases'):

    main_module = list(task_definition.keys())[0]
    sub_module =list(task_definition[main_module].keys())[0]
    use_case_module = module_parent + '.' + main_module + '.' + sub_module + '.' + 'model'
    print("Importing use case module:", use_case_module)

    module = import_module(use_case_module)

    return module


def run(std_input):

    config_file_path = fetch_std_input(std_input)

    # read out task definition with use cases and in/output paths
    task_definition, input_path, output_path = read_config(config_file_path)

    # import modules needed for specified use cases
    module = import_use_case(task_definition)

    return task_definition, input_path, output_path, module
