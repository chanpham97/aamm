from colorIdentifier import ColorBucketer
import cv2 as cv
import sys
import math

class ColorAnalysis: 
    def __init__(self):
        self.bucketer = ColorBucketer()


    def convert_to_percent(self, histogram):
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
        
        self.convert_to_percent(histogram)
        present = []
        for col in histogram:
            if histogram[col] > 5:
                present.append(col)

        return (histogram, present, imageOut)

        
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
        
        self.convert_to_percent(histogram)
        present = []
        for col in histogram:
            if histogram[col] > 5:
                present.append(col)

        return (histogram, present, imageOut)


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

    cv.imshow('imageIn', img_bgr)
    cv.imshow('imageOut', imgOut)
    cv.waitKey(0)
    # cv.imshow("bnw", img_bnw)
    try:
        save = raw_input("To save, input file name. Else, press enter. ")
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


    # cv.imshow('imageIn', img_hsv)
    # cv.imshow('imageOut_hsv', imgOut)
    # cv.waitKey(0)

    # try:
    #     save = raw_input("To save, input file name. Else, press enter. ")
    #     if save:
    #         cv.imwrite(save, imgOut)
    # except (EOFError, ValueError):
    #     pass

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
    
    
    img_bgr = cv.imread(sys.argv[1], cv.IMREAD_COLOR) #default BGR

    try:
        max_val = raw_input("Image dimensions are {}. To resize, enter max dimension. Else, default is 300. ".format(img_bgr.shape))
        img_bgr = resize_image(img_bgr, max_val) if max_val else resize_image(img_bgr)
    except (EOFError, ValueError):
        pass
            
    bgr_analysis(img_bgr)

    # img_bgr = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
    #bgr_analysis(img_bgr)
    
    print("****")
    a = ColorAnalysis()
    print(a.color_breakdown(img_bgr))
    print(a.brightness_bgr(img_bgr))
    # print(get_scaled_values(img_bgr))


# main()