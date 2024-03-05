from ultralytics import YOLO
import cv2
import math
import numpy as np

class CellDetector:
    """
    Class to wrap cell detection YOLOv8 model

    model_path (str): path to the YOLOv8 model
    """
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.IMAGE_SIZE = 128
        self.CROP_WIDTH = 128
        self.CROP_HEIGHT = 128

# |----------------------PREDICTIONS--------------------------------------------|

    def predict(self, image, conf, iou):
        """
        Predict boxes of died cells on a single image and postprocess the results

        image (np.array): image to predict
        conf (float): confidence threshold for predictions
        iou (float): IoU threshold for predictions

        return: list of predicted boxes with classes
        """
        if len(image.shape) < 3:
            image = cv2.merge((image,image,image))
        results = self.model.predict(image, conf=conf, iou=iou, imgsz=self.IMAGE_SIZE)
        results = self.process_results(results)
        return results

    def predict_with_crop(self, big_image, conf, iou, withOverlap = False):
        """
        Predict boxes if died cells on a single image. Predictions are made on a smaller cropped images from the original
        and then scaled to the original image.

        big_image (np.array): image to predict
        conf (float): confidence threshold for predictions
        iou (float): IoU threshold for predictions
        withOverlap (bool): If cropping should be with overlap or not

        return: list of predicted boxes with classes
        """
        if withOverlap:
            pass
        else:
            big_image, width_shift, height_shift = self.prepare_image_to_crop_no_overlap(big_image, withWinShift = True)

        image_h, image_w = big_image.shape[:2]
        num_width_windows = image_w/width_shift
        num_height_windows = image_h/height_shift

        results_all = []

        for width_window in range(int(num_width_windows)):
            for height_window in range(int(num_height_windows)):
                curr_topleft_x = width_window * width_shift
                curr_topleft_y = height_window * height_shift
                img_crop = big_image[curr_topleft_y:curr_topleft_y + self.CROP_HEIGHT, curr_topleft_x:curr_topleft_x + self.CROP_WIDTH]
                results = self.predict(img_crop, 0.2, 0.4)
                results = self.scale_crop_results(results, curr_topleft_x, curr_topleft_y)
                for result in results:
                    results_all.append(result)
        return results_all

    def predict_with_heatmap(self, big_image, conf, iou):
         """
        Predict boxes if died cells on a single image. Predictions are made on a smaller random cropped images from the original
        and then scaled to the original image. All the predictions are then converted to a heat map.

        big_image (np.array): image to predict
        conf (float): confidence threshold for predictions
        iou (float): IoU threshold for predictions

        return: list of predicted boxes with classes
        """
        big_image = self.prepare_image_to_crop_heatmap(big_image)

        # TODO
        # 1. for each image in random crop (limit random crop to image dimension without padding)
        # 2. predict for each iamge with 3 x 90deg rotations
        # 3. postprocess predictions and append to list
        # 4. 

# |----------------------RESULT PROCESSING--------------------------------------------|

    def scale_crop_results(self, results, curr_topleft_x, curr_topleft_y):
        """
        Scale predicted boxes coordinates made on a cropped image to match the original image dimensions

        results (list(list)): list of predicted boxes with classes
        curr_topleft_x (int): x axis coordinate value of top left corner of the cropped image from the original
        curr_topleft_y (int): y axis coordinate value of top left corner of the cropped image from the original

        return: list of scaled predicted boxes with classes
        """
        new_results = []
        for r in results:
            new_result = [r[0] + curr_topleft_y, r[1] + curr_topleft_x, r[2] + curr_topleft_y, r[3] + curr_topleft_x, r[4]]
            new_results.append(new_result)
        return new_results

    def process_results(self, results):
        """
        Process YOLOv8 prediction to desired format [top, left, bottom, right, class]

        results (list(list)): list of predicted boxes with classes

        return: list of predicted boxes with classes in the desired format
        """
        results_list = []
        result = results[0]
        for box in result.boxes:
            cell_cls = int(box.cls)
            b_xyxy = box.xyxy[0]
            l = int(b_xyxy[0])
            t = int(b_xyxy[1])
            r = int(b_xyxy[2])
            b = int(b_xyxy[3])
            results_list.append([t,l,b,r,cell_cls])
        return results_list

# |----------------------PREPROCESSING--------------------------------------------|

    def prepare_image_to_crop_no_overlap(self, image, withWinShift = False):
        """
        Add padding if required to the image before crop it into equal parts

        image (np.array): image to add padding to
        withWinShift (bool): if to return shift values of croping window

        return: processed image (optionaly: shift values of croping window)
        """
        image_h, image_w = image.shape[:2]

        CROP_WIDTH_SHIFT = self.CROP_WIDTH
        CROP_HEIGHT_SHIFT = self.CROP_HEIGHT

        if image_w % self.CROP_WIDTH != 0:
            desired_w = math.ceil(image_w/self.CROP_WIDTH)
            left = ((desired_w - (image_w/self.CROP_WIDTH)) * 128)
            right = 0
        else:
            left = 0
            right = 0

        if image_h % self.CROP_HEIGHT != 0:
            desired_h = math.ceil(image_h/self.CROP_HEIGHT)
            top = int((desired_h - (image_h/self.CROP_HEIGHT)) * 128)
            bottom = 0
        else:
            top = 0
            bottom = 0

        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT)

        if withWinShift:
            return image, CROP_WIDTH_SHIFT, CROP_HEIGHT_SHIFT
        else:
            return image

    def prepare_image_to_crop_heatmap(self, image):
        """
        Add padding to the image before random cropping for heatmap to make sure to cover all parts of image in all positions

        image (np.array): image to add padding to

        return: processed image
        """
        top = 128
        bottom = 128
        left = 128
        right = 128

        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT)

        return image


# |----------------------VISUALIZATIONS--------------------------------------------|

    def box_image(self, image, boxes, image_green = None):
        """
        Add prediction boxes of cells in specified colors to the image

        image (np.array): image to add boxes to
        boxes (list(list)): list of predicted boxes to add to the image
        image_green (np.array): additional image to add boxes to

        return: image with added boxes (optionaly: additional image with added boxes)
        """
        image = self.prepare_image_to_crop_no_overlap(image)
        if image_green is not None:
            image_green = self.prepare_image_to_crop_no_overlap(image_green)
            image_green_crop_3channel = cv2.merge((image_green,image_green,image_green))

        for box in boxes:
            t = box[0]
            l = box[1]
            b = box[2]
            r = box[3]

            cell_cls = box[4]
            if cell_cls == 0:
                color = (255,255,255)
                color_green = (255,50,100)
            elif cell_cls == 1:
                color = (0,0,0)
                color_green = (50,100,255)

            image = cv2.rectangle(image, (l,t), (r,b), color, 2)
            if image_green is not None:
                image_green_crop_3channel = cv2.rectangle(image_green_crop_3channel, (l,t), (r,b), color_green, 2)
        
        if image_green is not None:
            return image, image_green_crop_3channel
        else:
            return image
