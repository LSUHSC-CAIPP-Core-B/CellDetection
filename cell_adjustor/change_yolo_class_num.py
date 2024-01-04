import os
from config import *

#LABELED_IMAGES_DIR_PATH = IMAGES_PATH + "MEF_Labeles_phase/"
LABELED_IMAGES_DIR_PATH = "sample_labels_dir/"

# first class/group in pre list is changed to first class in the post list
classes_pre_swap = [[1, 3]] # list of lists of classes or list of classes ex. [[0,1], [3]]
classes_post_swap = [11] # list of classes ex. [1, 2]

new_lines = []

labels = os.listdir(LABELED_IMAGES_DIR_PATH)

# for each label file in dir
for label in labels:
    label_path = LABELED_IMAGES_DIR_PATH + label
    label_file = open(label_path, 'r')
    lines = label_file.readlines()
    # for each box line in file
    for line in lines:
        new_line = line
        # for len of classes list (to get all swaps)
        for classes_list_id in range(len(classes_pre_swap)):
            classes_pre = classes_pre_swap[classes_list_id]
            # for each class_num in group in pre swap list
            for class_pre in classes_pre:
                line_class = line.split(" ")[0]
                if int(line_class) == class_pre:
                    new_line = str(classes_post_swap[classes_list_id]) + line[len(line_class):]
        new_lines.append(new_line)

# writing to file
label_file_write = open(label_path, 'w')
label_file_write.writelines(new_lines)
label_file_write.close()