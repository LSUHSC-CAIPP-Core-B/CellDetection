# Data preprocessing
Everything conected to working with the dataset.

## Cell Adjustor
`cell_image_adjustor_marplot.py`   
Script to preview cell images and check output each step of preprocessing. You can also change params of preprocessing to adjust cell mask and label creation accuracy.    
How to use:   
You need to provide *dataset path* in *config.py* to iterate over. To adjust params change the sliders and to keep current configuration press save button and params will be in *params.csv* with the date of save. Next and back button move through iamges but you can use random button to pick different image. Reset button resets current params to initial ones that were used on opening the app.   

## Labeling
`label_cell_images.ipynb`    
Iterate over images in provided dir and for each image crop part of it to gen mask and label (yolo format).
We cover whole image while croping. Crop params and path might need to be adjusted for different datasets to match iamge size and desired overlap of crops.

## Augumentation
`augument_cell_iamges.ipynb`   
Augumentations are only a change in brightness and contrast. We augument images, labels, masks at the same time.

## Spliting
`split_dataset.ipynb`   
Split augumented files into train, val, test parts.

## Labels formats etc.
`yolo_to_xml.py` and `xml_to_tfrecord.py`   
Theese files change the format of labels to needed formats (xml, tfrecord).
Specific params and paths might have to be adjusted depending on the dataset.
   
`change_yolo_class_num.py`   
Script to change yolo class numbers in label files.   
