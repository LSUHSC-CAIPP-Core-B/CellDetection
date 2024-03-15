# CellDetection
Repository for died cell detection with apoptosis and necroptosis distinction. It provides training and inference pipelines for training cell detection model as well as all needed data preparation steps.

## cell_adjustor
Contains cell adjustor script that enables us to check parameters of cell images labeling process.
Here are also all the data preprocessing/managment scripts used to prepare the dataset.

### Setup
Python version required: 3.9.*
Create environment with:    
`python3 -m venv <venv_name>`    
or this for specific version of python installed:    
`python3.9 -m venv <venv_name>`   
Activate the environment with:    
`source <venv_name>/bin/activate`    
Install requirements with:    
`pip install -r requirements_cell_mac.txt`

## yolo
Yolo training pipeline with custom model wrapper and inference example.
### Setup
Python version required: 3.8.*
#### Mac
Create environment with:    
`python3 -m venv <venv_name>`    
or this for specific version of python installed:    
`python3.8 -m venv <venv_name>`   
Activate the environment with:    
`source <venv_name>/bin/activate`  
Install requirements with:    
`pip install -r requirements_ultralytics_mac.txt`
#### Ubuntu with CUDA
Setup was tested on an Ubunto 20.04 LTS machine with NVIDIA RTX A5000 and CUDA 12.3.   
Create environment and install requirements with:    
`conda create --name <venv_name> --file requirements_ultralytics.txt`   
Activate environment with:   
`conda activate <venv_name>`
### Example output
![example1](docs/cell_example.png)