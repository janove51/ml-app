import sys
from .interface import task_handler
if sys.argv[0] > 1:
    conif2g_file_path = sys.argv[0]
else:
    raise Exception("File path to config file required")

# Execute Task:
task_handler.Task(conif2g_file_path)

