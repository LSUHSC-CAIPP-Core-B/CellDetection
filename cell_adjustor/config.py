# OPTIONS
# Preprocessing values params
# 0 - initial params
# 1 - HT29 cells from 01/08 fine tuning
# 2 - MEF Apoptosis pt2 cells from 02/01 fine tuning
# 3 - HT29 Necroptosis/Apoptosis pt2 02/01 - 02/02 fine tuning
PREPROCESS_VALS = 3
# Datasets
# 3 - Necroptosis HT29
# 4 - Necroptosis MEF
# 5 - Apoptosis HT29
# 6 - Apoptosis MEF
# 7 - Necroptosis HT29 pt2
# 8 - Necroptosis MEF pt2
# 9 - Apoptosis HT29 pt2
# 10 - Apoptosis MEF pt2
# 11 Apoptosis MEF test
# 12 Necroptosis MEF test
DATASET = 101

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
elif PREPROCESS_VALS == 2:
    #A MEF pt2 - 02/01
    # contrast and brightness
    brightness = -9.4
    contrast = 7.4
    # thresh to get all the stained cells
    threshold = 42
    # erode and dialate to erase noise
    i_erode = 2
    i_dialate = 3
elif PREPROCESS_VALS == 3:
    #N/A HT29 pt2 - 02/02
    # contrast and brightness
    brightness = -18.2 #-9.26
    contrast = 12.0
    # thresh to get all the stained cells
    threshold = 42
    # erode and dialate to erase noise
    i_erode = 2
    i_dialate = 3

# PATHS
if DATASET == 3:
    # 3 Necroptosis HT29
    CELL_TYPE = "HT29"
    DEATH_TYPE = "Necroptosis"
    IMAGES_PATH = "../first_batch/Necroptosis/"
elif DATASET == 4:
    # 4 Necroptosis MEF
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Necroptosis"
    IMAGES_PATH = "../first_batch/Necroptosis/"
elif DATASET == 5:
    # 5 Apoptosis HT29
    CELL_TYPE = "HT29"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../first_batch/Apoptosis/"
elif DATASET == 6:
    # 6 Apoptosis MEF
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../first_batch/Apoptosis/"
# NEWPART--------------------------------------------------------------|
elif DATASET == 7:
    # 7 Necroptosis HT29 pt2
    CELL_TYPE = "HT29"
    DEATH_TYPE = "Necroptosis"
    IMAGES_PATH = "../new_data/Necroptosis/"
elif DATASET == 8:
    # 8 Necroptosis MEF pt2
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Necroptosis"
    IMAGES_PATH = "../new_data/Necroptosis/"
elif DATASET == 9:
    # 9 Apoptosis HT29 pt2
    CELL_TYPE = "HT29"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../new_data/Apoptosis/"
elif DATASET == 10:
    # 10 Apoptosis MEF pt2
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../new_data/Apoptosis/"
elif DATASET == 91:
    # 9 Apoptosis HT29 pt2 TEST
    CELL_TYPE = "HT29"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../new_data/Apoptosis2/"
elif DATASET == 101:
    # 10 Apoptosis MEF pt2 TEST
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../new_data/Apoptosis2/"
# TESTDATA-------------------------------------------------------------|
elif DATASET == 11:
    # 11 Apoptosis MEF test
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Apoptosis"
    IMAGES_PATH = "../test_images/Apoptosis/"
elif DATASET == 12:
    # 12 Necroptosis MEF test
    CELL_TYPE = "MEF"
    DEATH_TYPE = "Necroptosis"
    IMAGES_PATH = "../test_images/Necroptosis/"

# DATASET PATHS
GREEN_PATH = IMAGES_PATH + CELL_TYPE + "_Green/"
PHASE_PATH = IMAGES_PATH + CELL_TYPE + "_phase/"
CROP_PHASE_PATH = IMAGES_PATH + CELL_TYPE + "_Crop_phase/"
CROP_GREEN_PATH = IMAGES_PATH + CELL_TYPE + "_Crop_green/"