import os
import sys
from importlib import import_module
from error_handler import handle_warnings


# Setting default Encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf8')



class Task(object):
    '''
    Tasks are defined by the definition_json, which specifies the use case to be executed
    '''

    def __init__(self, definition_json):
        self.task_definition = definition_json
        self._set_project_path()     # so that subsequent import statements find the modules such as utils
        self._get_task_io()
        # self.ml_app_folder = 'commons.etl_blackbox.modules.'    # where the ml-app is sitting
        self.commons_module_data_io = '.data_io'
        self._get_task_module()

    def _set_param(self, param):
        ''' Used for getting the value of specified parameter from the task definition '''
        return self.task_definition[param]

    def _set_project_path(self):
        ''' Base path from where the project module is called '''

        self.project_base_path = os.getcwd() + "/" + self.task_definition['base_path']

    def _get_task_io(self):
        ''' Dynamically assemble the use case from input and output definition '''
        self.task_input_name = self.task_definition['input'].keys()[0]
        self.task_output_name = self.task_definition['output'].keys()[0]
        self.task_input_definition = self.task_definition['input'][self.task_input_name]
        self.task_output_definition = self.task_definition['output'][self.task_output_name]

    def _get_module_file(self, module_name):
        ''' Import file module
        :param module_name: Module file name
        :return: file object of module
        '''

        return import_module(module_name)

    def _get_module(self, module_file, module_name):
        ''' Import module object
        :param module_file: file name of module
        :param module_name: class name of module
        :return: class object of module
        '''

        return getattr(module_file, module_name)

    def run(self):
        ''' Execute a task

        :return: Initialises and runs input class object
        '''
        # self.input_module = self.task_input_module(base_path=self.project_base_path,
        #                                            definition=self.task_input_definition)
        # self.output_module = self.task_output_module(base_path=self.project_base_path,
        #                                              definition=self.task_output_definition)
        # try:
        #     self.input_module.run_input(output_io=self.output_module)
        #
        # except Exception as e:
        #     raise RuntimeError(e)

        print('running task')