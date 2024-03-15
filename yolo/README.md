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
### Notebook version
This file has examples on how to use the YOLO package for simple training and get mterics from training output as well as perform inference.
### Script version
This training Python script was mainly used for training and is a minimal example of setting the training up.
## Inference
### Base inference
To test the model on an image file *yolo_inference_test.ipynb* was made. The notebook performes prediction on a given image and can display the results. The inference is made on cropped images of the  original image provided to suit the model requirements and then our custom wrapper takes care of the result predictions format for visualization purposes. The visualization can be done with additional microscopic image of staining.  
### Heat map inference
Other inference method prepared is generating a heat map. Detection is performed multiple times on a single crop at different rotations and then normalized. Heat map can ensure that only cells that yield multiple results are visible.
The results are 3 heat map images for apoptosis cells, necroptosis cells and background. Each heat map is in range of <0.0,1.0>.
### Comparison
There is one additional file *yolo_inference_comparison.ipynb* for comparing both methods of inference side by side.
### CellDetector
Class to wrap trained YOLOv8 cell detection model. CellDetector provide functions to do inference, and visualization.
Inference can be performed on a single image in desired size or on a larger whole microscope image with croping it into samller images. 
Another option for inference is generating a heat map.
Croping for inference can be done with overlapping of the cropped images (to prevent slicing the cells on the edge of crops) or without.
Visualization part is applying bounding boxes in different colors to detected cells.   