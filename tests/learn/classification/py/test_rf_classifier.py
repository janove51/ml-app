import os, sys
print(os.path.abspath('../../../../ml-app'))
sys.path.append(os.path.abspath('../../../../ml-app'))

from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_circles

from interface.task_handler import Task
from entities.utils.utils import read_file

CONSTANTS = {
    'train_rf': '../tasks/test_rf_classifier.json'
}

##### Job file test #####

filename = CONSTANTS['train_rf']
task = Task(read_file(filename))
task.run()

##### RF Classifier test ####