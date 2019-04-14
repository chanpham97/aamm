from colorIdentifier import ColorBucketer
import cv2 as cv
import sys

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

def main():

    img_bgr = cv.imread(sys.argv[1], cv.IMREAD_COLOR) #default BGR
    try:
        max_val = raw_input("Image dimensions are {}. To resize, enter max dimension. Else, default is 300. ".format(img_bgr.shape))
        img_bgr = resize_image(img_bgr, max_val) if max_val else resize_image(img_bgr)
    except (EOFError, ValueError):
        pass
            
    # bgr_analysis(img_bgr)

    img_hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
    hsv_analysis(img_hsv)


main()