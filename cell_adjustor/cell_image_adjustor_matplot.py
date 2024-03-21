import os
import csv
import random
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons

from config import *
from CellProcessor import read_image, process_image, draw_contours

# Comment this paths if not to use cropped images paths
GREEN_PATH = CROP_GREEN_PATH
PHASE_PATH = CROP_PHASE_PATH

# Read image and initial process
curr_image_num = 0
images = os.listdir(GREEN_PATH)
len_images = len(images)
green_image_path = GREEN_PATH + images[curr_image_num]
base_image_path = PHASE_PATH + images[curr_image_num]
img, img_base = read_image(green_image_path, base_image_path)

# initial preporcess and contours
img_br, img_thr, img_erosion, img_dilation = process_image(img, 
                                                           contrast, 
                                                           brightness, 
                                                           threshold, 
                                                           i_erode, 
                                                           i_dialate, 
                                                           plot = True)

img_out = draw_contours(img_dilation, img_base)

# PLOTS
fig = plt.figure(figsize=(14,10))
plt.subplots_adjust(wspace=0.2, hspace=0.05, bottom=0.2)

ax1 = plt.subplot(2,3,1)
image1 = ax1.imshow(img, cmap='gray')
plt.title('input')

ax2 = plt.subplot(2,3,2, sharex=ax1, sharey=ax1)
image2 = ax2.imshow(img_br, cmap='gray')
plt.title('input - brightness/contrast')

ax3 = plt.subplot(2,3,3, sharex=ax1, sharey=ax1)
image3 = ax3.imshow(img_thr, cmap='gray')
plt.title('input - thresh')

ax4 = plt.subplot(2,3,4, sharex=ax1, sharey=ax1)
image4 = ax4.imshow(img_erosion, cmap='gray')
plt.title('input - erosion')

ax5 = plt.subplot(2,3,5, sharex=ax1, sharey=ax1)
image5 = ax5.imshow(img_dilation, cmap='gray')
plt.title('input - dilation')

ax6 = plt.subplot(2,3,6, sharex=ax1, sharey=ax1)
image6 = ax6.imshow(img_out, cmap='gray')
plt.title('output')

# VARIABLES
axcolor = 'lightgoldenrodyellow'
axbr = plt.axes([0.25, 0.16, 0.65, 0.02], facecolor=axcolor)
axcontr = plt.axes([0.25, 0.13, 0.65, 0.02], facecolor=axcolor)
axthr = plt.axes([0.25, 0.10, 0.65, 0.02], facecolor=axcolor)
axerd = plt.axes([0.25, 0.07, 0.65, 0.02], facecolor=axcolor)
axdial = plt.axes([0.25, 0.04, 0.65, 0.02], facecolor=axcolor)

sbright = Slider(axbr, 'Brightness', -35.0, 50.0, valinit=brightness)
scontr = Slider(axcontr, 'Contrast', -5.0, 25.0, valinit=contrast)
sthr = Slider(axthr, 'Threshold', 0.0, 255.0, valinit=threshold, valfmt="%i")
serd = Slider(axerd, 'Erosion', 0.0, 15.0, valinit=i_erode, valfmt="%i")
sdial = Slider(axdial, 'Dialation', 0.0, 15.0, valinit=i_dialate, valfmt="%i")

# BUTTONS
resetax = plt.axes([0.85, 0.92, 0.05, 0.02])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.875')

nextax = plt.axes([0.78, 0.92, 0.05, 0.02])
button_next = Button(nextax, 'Next', color=axcolor, hovercolor='0.875')

backax = plt.axes([0.71, 0.92, 0.05, 0.02])
button_back = Button(backax, 'Back', color=axcolor, hovercolor='0.875')

saveax = plt.axes([0.64, 0.92, 0.05, 0.02])
button_save = Button(saveax, 'Save', color=axcolor, hovercolor='0.875')

randax = plt.axes([0.57, 0.92, 0.05, 0.02])
button_rand = Button(randax, 'Random', color=axcolor, hovercolor='0.875')

# LABELS
imnumax = plt.axes([0.2, 0.88, 0.1, 0.02])
imnum_str = str(curr_image_num + 1) + "/" + str(len(images))
imnum_label = TextBox(imnumax, "Current Image ", imnum_str)

# update plots
def update(val, img, img_base):
    br = sbright.val
    cntr = scontr.val
    thr = int(sthr.val)
    i_e = int(serd.val)
    i_d = int(sdial.val)

    img_br, img_thr, img_erosion, img_dilation = process_image(img, cntr, br, thr, i_e, i_d, plot = True)
    
    img_out = draw_contours(img_dilation, img_base)

    image1.set_data(img)
    image2.set_data(img_br)
    image3.set_data(img_thr)
    image4.set_data(img_erosion)
    image5.set_data(img_dilation)
    image6.set_data(img_out)
    fig.canvas.flush_events()
sbright.on_changed(lambda val: update(val, img, img_base))
scontr.on_changed(lambda val: update(val, img, img_base))
sthr.on_changed(lambda val: update(val, img, img_base))
serd.on_changed(lambda val: update(val, img, img_base))
sdial.on_changed(lambda val: update(val, img, img_base))

# change to next image
def next(event, images):
    global curr_image_num
    global img, img_base
    if curr_image_num < (len(images)-1):
        curr_image_num += 1
    green_image_path = GREEN_PATH + images[curr_image_num]
    base_image_path = PHASE_PATH + images[curr_image_num]
    print(green_image_path)
    img, img_base = read_image(green_image_path, base_image_path)

    br = sbright.val
    cntr = scontr.val
    thr = int(sthr.val)
    i_e = int(serd.val)
    i_d = int(sdial.val)

    img_br, img_thr, img_erosion, img_dilation = process_image(img, cntr, br, thr, i_e, i_d, plot = True)
    
    img_out = draw_contours(img_dilation, img_base)

    image1.set_data(img)
    image2.set_data(img_br)
    image3.set_data(img_thr)
    image4.set_data(img_erosion)
    image5.set_data(img_dilation)
    image6.set_data(img_out)
    imnum_label.set_val(str(curr_image_num + 1) + "/" + str(len(images)))
    fig.canvas.flush_events()
    plt.draw()
button_next.on_clicked(lambda event: next(event, images))

# change to previous image
def back(event, images):
    global curr_image_num
    global img, img_base
    if curr_image_num > 0:
        curr_image_num -= 1
    green_image_path = GREEN_PATH + images[curr_image_num]
    base_image_path = PHASE_PATH + images[curr_image_num]
    print(green_image_path)
    img, img_base = read_image(green_image_path, base_image_path)

    br = sbright.val
    cntr = scontr.val
    thr = int(sthr.val)
    i_e = int(serd.val)
    i_d = int(sdial.val)

    img_br, img_thr, img_erosion, img_dilation = process_image(img, cntr, br, thr, i_e, i_d, plot = True)
    
    img_out = draw_contours(img_dilation, img_base)

    image1.set_data(img)
    image2.set_data(img_br)
    image3.set_data(img_thr)
    image4.set_data(img_erosion)
    image5.set_data(img_dilation)
    image6.set_data(img_out)
    imnum_label.set_val(str(curr_image_num + 1) + "/" + str(len(images)))
    fig.canvas.flush_events()
    plt.draw()
button_back.on_clicked(lambda event: back(event, images))

# save vars to file
def save(event):
    br = sbright.val
    cntr = scontr.val
    thr = int(sthr.val)
    i_e = int(serd.val)
    i_d = int(sdial.val)

    save_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    new_row = [save_time, br, cntr, thr, i_e, i_d]

    with open('params.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow(new_row)
button_save.on_clicked(save)

# rand image pick
def rand_pick(event, len_images):
    global curr_image_num
    global img, img_base
    curr_image_num = random.randint(0, len_images-1)
    green_image_path = GREEN_PATH + images[curr_image_num]
    base_image_path = PHASE_PATH + images[curr_image_num]
    print(green_image_path)
    img, img_base = read_image(green_image_path, base_image_path)

    br = sbright.val
    cntr = scontr.val
    thr = int(sthr.val)
    i_e = int(serd.val)
    i_d = int(sdial.val)

    img_br, img_thr, img_erosion, img_dilation = process_image(img, cntr, br, thr, i_e, i_d, plot = True)
    
    img_out = draw_contours(img_dilation, img_base)

    image1.set_data(img)
    image2.set_data(img_br)
    image3.set_data(img_thr)
    image4.set_data(img_erosion)
    image5.set_data(img_dilation)
    image6.set_data(img_out)
    imnum_label.set_val(str(curr_image_num + 1) + "/" + str(len(images)))
    fig.canvas.flush_events()
    plt.draw()
button_rand.on_clicked(lambda event: rand_pick(event, len_images))

# reset vars
def reset(event):
    sbright.reset()
    scontr.reset()
    sthr.reset()
    serd.reset()
    sdial.reset()
button.on_clicked(reset)

plt.show()
