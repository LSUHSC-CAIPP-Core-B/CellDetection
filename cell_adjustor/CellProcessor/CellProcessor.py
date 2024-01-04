import cv2
import imutils
import numpy as np
import tensorflow as tf

def get_bboxes(img_dilation, dims=False):
    # blur
    img_blur = cv2.GaussianBlur(img_dilation, (5, 5), 0)

    # get contours and calc center
    cnts = cv2.findContours(img_blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    bboxes = []
    for c in cnts:
        x_points = c[:,0,0]
        y_points = c[:,0,1]
        x_min = min(x_points)
        x_max = max(x_points)
        y_min = min(y_points)
        y_max = max(y_points)

        xw = x_max - x_min
        yh = y_max - y_min
        box_width = max([xw, yh])
        x_padding = box_width*0.45
        y_padding = box_width*0.45

        xp_min = int(x_min - x_padding)
        xp_max = int(x_min + box_width + x_padding)
        yp_min = int(y_min - y_padding)
        yp_max = int(y_min + box_width + y_padding)

        start_pt = (xp_min, yp_min) # top left
        end_pt = (xp_max, yp_max) # bottom right

        if dims:
            h, w = img_dilation.shape[:2]
            bboxes.append([start_pt, end_pt, w, h])
        else:
            bboxes.append([start_pt, end_pt])
    return bboxes

def draw_contours(img_dilation, img_base):
    img_out = img_base.copy()
    bboxes = get_bboxes(img_dilation)
    for start_pt, end_pt in bboxes:
        cv2.rectangle(img_out, start_pt, end_pt, color=(255,35,35), thickness=1)

    return img_out

def process_image(img, contrast, brightness, threshold, iterations_erode, iterations_dilate, plot=False):
    # brightness and contrast
    img_br = cv2.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)
    # threshold
    ret, img_thr = cv2.threshold(img_br, threshold, 255, cv2.THRESH_BINARY)
    # erosion and dialation to erase noise
    kernel0 = np.ones((2, 2), np.uint8)
    img_erosion = cv2.erode(img_thr, kernel0, iterations=iterations_erode)
    img_dilation = cv2.dilate(img_erosion, kernel0, iterations=iterations_dilate)

    if plot:
        return img_br, img_thr, img_erosion, img_dilation
    else:
        return img_dilation
    
def read_image(green_image_path, base_image_path):
    img_base = cv2.imread(base_image_path, cv2.IMREAD_UNCHANGED)
    img = cv2.imread(green_image_path, cv2.IMREAD_UNCHANGED)
    #print(f'dtype: {img.dtype}, shape: {img.shape}, min: {np.min(img)}, max: {np.max(img)}')
    img = cv2.convertScaleAbs(img, alpha=(255.0/65535.0))
    #print(f'dtype: {img.dtype}, shape: {img.shape}, min: {np.min(img)}, max: {np.max(img)}')
    return img, img_base

def get_label(start_pt, end_pt):
    x_min = start_pt[0]
    y_min = start_pt[1]
    x_max = end_pt[0]
    y_max = end_pt[1]

    box_width = x_max - x_min
    box_height = y_max - y_min

    x_center = x_min + box_width/2
    y_center = y_min + box_height/2

    return x_center, y_center, box_width, box_height

def get_label_yolo(start_pt, end_pt, img_width, img_height):
    x_center, y_center, box_width, box_height = get_label(start_pt, end_pt)

    x = float(x_center/img_width)
    y = float(y_center/img_height)
    w = float(box_width/img_width)
    h = float(box_height/img_height)

    if x > 1.0:
        x = 1.0
    elif x < 0:
        x = 0.0

    if y > 1.0:
        y = 1.0
    elif y < 0:
        y = 0.0

    return x, y, w ,h

def read_yolo_labels(annotation_file):
    bboxes_list = []
    classes_list = []
    with open(annotation_file, "r") as af:
        labels_str = af.readlines()
        for ls in labels_str:
            ls_values = ls.split(" ")
            c = str(ls_values[0])
            x = float(ls_values[1])
            y = float(ls_values[2])
            w = float(ls_values[3])
            h = float(ls_values[4])
            bboxes_list.append([x,y,w,h])
            classes_list.append(c)

    return bboxes_list, classes_list

def yolo_to_original(img, yolo_label):
    img_height, img_width = img.shape[:2]
    xc = float(yolo_label[0] * img_width)
    yc = float(yolo_label[1] * img_height)
    w = int(yolo_label[2] * img_width)
    h = int(yolo_label[3] * img_height)
    x = int(xc - w/2)
    y = int(yc - h/2)

    return x, y, w, h

def crop_img_from_label(img, yolo_label, padding=0, retCords=False, withMask=False, img_mask=None):
    x, y, w, h = yolo_to_original(img, yolo_label)
    img_height, img_width = img.shape[:2]
    if img_mask is None:
        img_mask = np.zeros((img_width, img_height))
        img_mask = cv2.rectangle(img_mask, (x,y), (x+w,y+h), (255,255,255), -1)

    if padding != 0:
        #TODO add padding but check if there is enough image
        '''
        HAVE TO KEEP IT SQUARE

        if px to low double padding in right
        others same way
        '''
        px = x - padding
        py = y - padding
        pxw = x + w + padding
        pyh = y + h + padding
        # if padding exceeds 0 on x axis
        if px < 0:
            px = 0
            # if also exceeds img_width on x axis then max the box
            if pxw > img_width:
                pxw = img_width
            # else just add double padding to one side
            else:
                pxw = x + w + padding + padding
        # else add double padding on the other side
        elif pxw > img_width:
            px = x - padding - padding
            pxw = img_width

        # if padding exceeds 0 on y axis
        if py < 0:
            py = 0
            # if also exceeds img_height on y axis then max the box
            if pyh > img_height:
                pyh = img_height
            # else just add double padding to one side
            else:
                pyh = y + h + padding + padding
        # else add double padding to the other side
        elif pyh > img_height:
            py = y - padding - padding
            pyh = img_height

        img_crop = img[py:pyh, px:pxw]
        img_mask = img_mask[py:pyh, px:pxw]
    else:
        img_crop = img[y:y+h, x:x+w]
        img_mask = img_mask[y:y+h, x:x+w]

    if retCords:
        return img_crop, x, y, w, h
    elif withMask:
        return img_crop, img_mask
    else:
        return img_crop
