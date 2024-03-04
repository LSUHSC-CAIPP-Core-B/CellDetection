# YOLO pipeline

## Data preparation
The labels have to be in Yolo format and paths to dataset has to be prepared the same way as this example *.yaml* file.
Data has to be split into images and labels folders each containing train, val, test subfolders.
### YAML file structure
- *path* is the main path to dataset
- *train, val, test* is the paths to coresponding parts of dataset
- *nc* is the number of calsses dataset has
- *names* is to give name to the number representing specific class in label files

## Training
Training file uses ultralytics YOLOv8 package. You have to provide *.pt* model, *.yaml* dataset file and specifiy training params in the train section.
The output of the training will be saved in the *runs* folder but additional sample code for metrics and inference has been provided in the file.

## Inference
To test the model on an image file *yolo_inference_test.ipynb* was made. The notebook performes prediction on a given image and can display the results.   
### CellDetector
Class to wrap trained YOLOv8 cell detection model. CellDetector provide functions to do inference, and visualization.
Inference can be performed on a single image in desired size or on a larger whole microscope image with croping it into samller images. 
Croping for inference can be done with overlapping of the cropped images (to prevent slicing the cells on the edge of crops) or without.
Visualization part is applying bounding boxes in different colors to detected cells.   