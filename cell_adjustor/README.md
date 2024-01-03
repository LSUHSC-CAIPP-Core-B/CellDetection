# Data preprocessing
Everything conected to working with the dataset.

## Cell Adjustor
`cell_image_adjustor_marplot.py`   
Script to preview cell images and check output each step of preprocessing. You can also change params of preprocessing to adjust cell mask and label creation accuracy.

## Labeling
`label_cell_images.ipynb`    
Iterate over images in provided dir and for each image crop part of it to gen mask and label (yolo format).
We cover whole image while croping. Crop params and path might need to be adjusted for different datasets to match iamge size and desired overlap of crops.

## Augumentation
`augument_dell_iamges.ipynb`   
Augumentations are only a change in brightness and contrast. We augument images, labels, masks at the same time.

## Spliting
`split_dataset.ipynb`   
Split augumented files into train, val, test parts.

## Labels formats
`yolo_to_xml.py` and `xml_to_tfrecord.py`   
Theese files change the format of labels to needed formats (xml, tfrecord).   