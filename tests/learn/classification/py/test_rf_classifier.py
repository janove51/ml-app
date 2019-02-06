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

# generate 2d classification dataset for testing
X, y = make_blobs(n_samples=100, centers=3, n_features=2)


# generate 2d classification dataset
# X, y = make_circles(n_samples=100, noise=0.05)

# train the random forest
filename = CONSTANTS['train_rf']
task = Task(read_file(filename))
task.run()
