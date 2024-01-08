# OPTIONS
# Preprocessing values params
# 0 - initial params
# 1 - HT29 cells from 01/08 fine tuning
PREPROCESS_VALS = 0
# Datasets
# 3 - Necroptosis HT29
# 4 - Necroptosis MEF
# 5 - Apoptosis HT29
# 6 - Apoptosis MEF
DATASET = 4

# INITIAL VARS
if PREPROCESS_VALS == 0:
    # contrast and brightness
    brightness = 0.0
    contrast = 1.7
    # thresh to get all the stained cells
    threshold = 45
    # erode and dialate to erase noise
    i_erode = 1
    i_dialate = 1
elif PREPROCESS_VALS == 1:
    #HT29 - 01/08
    # contrast and brightness
    brightness = -9.4
    contrast = 5.6
    # thresh to get all the stained cells
    threshold = 42
    # erode and dialate to erase noise
    i_erode = 2
    i_dialate = 3

# PATHS
# 1
#IMAGES_PATH = "jian/"
#GREEN_PATH = IMAGES_PATH + "green/"
#PHASE_PATH = IMAGES_PATH + "phase/"
# 2
#IMAGES_PATH = "MEF1/"
#GREEN_PATH = IMAGES_PATH + "TSV_green/"
#PHASE_PATH = IMAGES_PATH + "TSV_phase/"

#GREEN_PATH = IMAGES_PATH + "Masks_phase/"
#PHASE_PATH = IMAGES_PATH + "TSV_Labeled_phase/"
    
if DATASET == 3:
    # 3 Necroptosis HT29
    IMAGES_PATH = "../Necroptosis/"
    GREEN_PATH = IMAGES_PATH + "HT29_Green/"
    PHASE_PATH = IMAGES_PATH + "HT29_phase/"
    CROP_PHASE_PATH = IMAGES_PATH + "HT29_Crop_phase/"
    CROP_GREEN_PATH = IMAGES_PATH + "HT29_Crop_green/"
elif DATASET == 4:
    # 4 Necroptosis MEF
    IMAGES_PATH = "../Necroptosis/"
    GREEN_PATH = IMAGES_PATH + "MEF_Green/"
    PHASE_PATH = IMAGES_PATH + "MEF_phase/"
    CROP_PHASE_PATH = IMAGES_PATH + "MEF_Crop_phase/"
    CROP_GREEN_PATH = IMAGES_PATH + "MEF_Crop_green/"
elif DATASET == 5:
    # 5 Apoptosis HT29
    IMAGES_PATH = "../Apoptosis/"
    GREEN_PATH = IMAGES_PATH + "HT29_Green/"
    PHASE_PATH = IMAGES_PATH + "HT29_phase/"
    CROP_PHASE_PATH = IMAGES_PATH + "HT29_Crop_phase/"
    CROP_GREEN_PATH = IMAGES_PATH + "HT29_Crop_green/"
elif DATASET == 6:
    # 6 Apoptosis MEF
    IMAGES_PATH = "../Apoptosis/"
    GREEN_PATH = IMAGES_PATH + "MEF_Green/"
    PHASE_PATH = IMAGES_PATH + "MEF_phase/"
    CROP_PHASE_PATH = IMAGES_PATH + "MEF_Crop_phase/"
    CROP_GREEN_PATH = IMAGES_PATH + "MEF_Crop_green/"