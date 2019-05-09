from colorIdentifier import ColorBucketer
import cv2 as cv
import sys
import math
<<<<<<< HEAD
import numpy as np
=======
from statistics import mean
>>>>>>> 1249780659909541637f89240b90496b7881ecc5

class ColorAnalysis: 
    def __init__(self):
        self.bucketer = ColorBucketer()
        self.PERC_MIN = 0.1


    def hist_to_percent(self, histogram):
        total = float(sum(histogram.values()))
        for val in histogram:
            histogram[val] = histogram[val]/total * 100

    def color_breakdown(self, image, outputImage=False):
        rows, cols, depth = image.shape
        
        imageOut = []
        if outputImage:
            imageOut = image.copy()
            self.bucketer.reset_bias()

        histogram = dict.fromkeys(self.bucketer.color_bases.keys(), 0)
        for r in range(rows):
            for c in range(cols):
                color = self.bucketer.bucket_color(image[r, c])
                histogram[color] += 1
                if outputImage:
                    imageOut[r, c] = self.bucketer.color_bases[color]
        
        self.hist_to_percent(histogram)
        present = []
        for col in histogram:
            if histogram[col] > 5:
                present.append(col)

        return (histogram, present, imageOut)
    
    def color_gradients(self, image, outputImage=False):
        rows, cols, depth = image.shape
        
        #imageOut = []
        if outputImage:
            #imageOut = image.copy()
            self.bucketer.reset_bias()

        b_gradients_horiz = []
        g_gradients_horiz = []
        r_gradients_horiz = []
        b_gradients_vert = []
        g_gradients_vert = []
        r_gradients_vert = []        
        
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                b, g, r = list(image[row, col])
                b_left, g_left, r_left = list(image[row, col-1])
                b_right, g_right, r_right = list(image[row, col+1])
                b_top, g_top, r_top = list(image[row-1, col])
                b_bottom, g_bottom, r_bottom = list(image[row+1, col]) 
                
                b_gradients_horiz.append(abs(b_right-b_left))
                g_gradients_horiz.append(abs(g_right-g_left))
                r_gradients_horiz.append(abs(r_right-r_left))
                b_gradients_vert.append(abs(b_top-b_bottom))
                g_gradients_vert.append(abs(g_top-g_bottom))
                r_gradients_vert.append(abs(r_top-r_bottom))
                
                #color = self.bucketer.bucket_color(image[row, col])
                #if outputImage:
                #    imageOut[row, col] = [abs(b_right-b_left), abs(g_right-g_left), abs(r_right-r_left)]

        b_gradients_horiz = [x for x in b_gradients_horiz if x > 0]
        g_gradients_horiz = [x for x in g_gradients_horiz if x > 0]
        r_gradients_horiz = [x for x in r_gradients_horiz if x > 0]
        b_gradients_vert = [x for x in b_gradients_vert if x > 0]
        g_gradients_vert = [x for x in g_gradients_vert if x > 0]
        r_gradients_vert = [x for x in r_gradients_vert if x > 0] 
        
        mean_b_gradients_horiz = mean(b_gradients_horiz)
        mean_g_gradients_horiz = mean(g_gradients_horiz)
        mean_r_gradients_horiz = mean(r_gradients_horiz)
        mean_b_gradients_vert = mean(b_gradients_vert)
        mean_g_gradients_vert = mean(g_gradients_vert)
        mean_r_gradients_vert = mean(r_gradients_vert)
        
        print(mean_b_gradients_horiz, mean_g_gradients_horiz, mean_r_gradients_horiz, 
              mean_b_gradients_vert, mean_g_gradients_vert, mean_r_gradients_vert)

        return (mean_b_gradients_horiz, mean_g_gradients_horiz, mean_r_gradients_horiz, 
              mean_b_gradients_vert, mean_g_gradients_vert, mean_r_gradients_vert)

        
    def brightness_bgr(self, img):
        img_bnw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        brightness = img_bnw.mean()/255.0 * 100
        return brightness

    
    # NOTE: seems less effective than BGR color identification but much faster
    def hue_breakdown(self, image, outputImage=False):
        histogram = dict.fromkeys(self.bucketer.hue_bases.keys(), 0)
        # histogram['white'] = 0
        # histogram['black'] = 0

        imageOut = []
        # if outputImage:
        #     imageOut = image.copy()

        rows, cols, depth = image.shape
        for r in range(rows):
            for c in range(cols):
                hue = self.bucketer.bucket_hue(image[r, c])
                if hue:
                    histogram[hue] += 1
                # if outputImage:
                #     imageOut[r, c] = 
        
        self.hist_to_percent(histogram)
        present = []
        for col in histogram:
            if histogram[col] > 5:
                present.append(col)

        return (histogram, present, imageOut)


    # source: https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
    def auto_canny(image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv.Canny(image, lower, upper)
        return edged


    def calc_perc_filled(img, img_filled):
        diff = img - img_filled
        h, w = diff.shape
        total = float(h * w)
        count = np.count_nonzero(diff)
        print count, count*100/total
        return count*100/total


    def count_blocks(self, img_bgr)
        blurred = cv.medianBlur(img_bgr, 7)
        edges = auto_canny(blurred)

        # cv.imshow('edges', edges)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        
        h, w = edges.shape
        # print (h, w)
        filled = edges.copy()
        mask = np.zeros((h+2, w+2), np.uint8)

        blocks = 0
        for row in range(h):
            for col in range(w):
                # print (row, col)
                # print filled[row][col]
                if filled[row][col] == 0:
                    filled_temp = filled.copy()
                    cv.floodFill(filled_temp, mask, (col, row), 255)
                    if calc_perc_filled(filled, filled_temp) > self.PERC_MIN:
                        blocks = blocks + 1
                    filled = filled_temp
                    # cv.imshow('filled' + str(blocks), filled)
                    # cv.waitKey(0)
                    # cv.destroyAllWindows()
        return blocks

    # def color_block_finder(self, img_bgr):


def resize_image(image, max_val=300):
    rows, cols, depth = image.shape
    if max([rows, cols]) > max_val:
        scale = max_val/float(max([rows, cols]))
        # print(scale)
        image = cv.resize(image, None, fx=scale, fy=scale)
    return image


def bgr_analysis(img_bgr):
    a = ColorAnalysis()

    colBreakdown, colPresent, imgOut = a.color_breakdown(img_bgr, True) 
    print("COLORS PRESENT:")
    for color in colPresent:
        print("{}: {}".format(color, round(colBreakdown[color], 2)))

    print("Average brightness: {}".format(a.brightness_bgr(img_bgr)))
    
    print("Color gradient values: {}".format(a.color_gradients(img_bgr)))

    cv.imshow('imageIn', img_bgr)
    cv.imshow('imageOut', imgOut)
    cv.waitKey(60)
    # cv.imshow("bnw", img_bnw)
    try:
        save = input("To save, input file name. Else, press enter. ")
        if save:
            cv.imwrite(save, imgOut)
    except (EOFError, ValueError):
        pass
        
    cv.destroyAllWindows()

def bgr_gradient_analysis(img_bgr):
    a = ColorAnalysis()

    num, imgOut = a.color_gradients(img_bgr, True) 
    
    cv.imshow('imageIn', img_bgr)
    cv.imshow('imageOut', imgOut)
    cv.waitKey(60)
    
    try:
        save = input("To save, input file name. Else, press enter. ")
        if save:
            cv.imwrite(save, imgOut)
    except (EOFError, ValueError):
        pass
        
    cv.destroyAllWindows()
    

def hsv_analysis(img_hsv):
    a = ColorAnalysis()

    hueBreakdown, huePresent, imgOut = a.hue_breakdown(img_hsv, True) 
    print("HUES PRESENT:")
    for hue in huePresent:
        print("{}: {}".format(hue, round(hueBreakdown[hue], 2)))


def get_scaled_color_breakdown(color_dict):
    colors_pos_negative = {
           'black': 1,
           'red': 3,
           'pink': 4,
           'white': 5,
           'green': 7,
           'blue': 9,
           'yellow': 10
    }
    total = 0
    for color, percent in color_dict.items():
        total += colors_pos_negative[color] * percent/100.0
        # print(color, colors_pos_negative[color], percent, colors_pos_negative[color] * percent)
        # print(total)
    return total
    

def get_scaled_num_colors(colors):
    num_colors = len(colors)
    if num_colors == 1:
        return 1
    if num_colors <= 2:
        return 2
    if num_colors <= 3:
        return 4
    if num_colors <= 4:
        return 6
    if num_colors <= 5:
        return 8
    return 10


def get_scaled_brightness(brightness):
    if brightness <= 30:
        return 1
    if brightness <= 35:
        return 2
    if brightness <= 40:
        return 3
    if brightness <= 45:
        return 4
    if brightness <= 50:
        return 5
    if brightness <= 55:
        return 6
    if brightness <= 60:
        return 7
    if brightness <= 65:
        return 8
    if brightness <= 75:
        return 9
    return 10


def get_scaled_values(img_bgr):
    a = ColorAnalysis()
    tup = a.color_breakdown(img_bgr)
    bright = a.brightness_bgr(img_bgr)
    print('color raw: ', tup[1], bright)
    return get_scaled_color_breakdown(tup[0]), get_scaled_num_colors(tup[1]), get_scaled_brightness(bright)


def read_bgr(path):
    img_bgr = cv.imread(path, cv.IMREAD_COLOR) #default BGR
    return img_bgr

    
def main():
    # for i in range(0, 16):
    #     a = ColorAnalysis()
    #     brightness = a.brightness_bgr(img_bgr)
    #     print(str(i), brightness, get_scaled_brightness(brightness))
    
    img_bgr = read_bgr(sys.argv[1]) #default BGR

    try:
        max_val = input("Image dimensions are {}. To resize, enter max dimension. Else, default is 300. ".format(img_bgr.shape))
        img_bgr = resize_image(img_bgr, max_val) if max_val else resize_image(img_bgr)
    except (EOFError, ValueError):
        pass
<<<<<<< HEAD
     
    # bgr_analysis(img_bgr)
=======
            
    bgr_analysis(img_bgr)
    #bgr_gradient_analysis(img_bgr)
>>>>>>> 1249780659909541637f89240b90496b7881ecc5

    # img_bgr = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
    #bgr_analysis(img_bgr)
    
<<<<<<< HEAD
    print("****")
    a = ColorAnalysis()
    
=======
#    print("****")
#    a = ColorAnalysis()
#    print(a.color_breakdown(img_bgr))
#    print(a.brightness_bgr(img_bgr))
    # print(get_scaled_values(img_bgr))
>>>>>>> 1249780659909541637f89240b90496b7881ecc5


main()