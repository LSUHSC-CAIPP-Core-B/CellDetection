# YOLO pipeline

## Data preparation
The labels have to be in Yolo format and paths to dataset has to be prepared the same way as this example *.yaml* file.
### YAML file structure
- *path* is the main path to dataset
- *train, val, test* is the paths to coresponding oarts of dataset
- *nc* is the number of calsses dataset has
- *names* is to give name to the number representing specific class in label files

## Training
Training file uses ultralytics YOLOv8 package. You have to provide *.pt* model and specifiy training params in the train section.
The output of the training will be saved in the *runs* folder but additional sample code for metrics and inference has been provided in the file.