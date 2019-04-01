from colorIdentifier import ColorBucketer
import cv2 as cv
import sys

class ColorAnalysis: 
    def __init__(self):
        self.bucketer = ColorBucketer()

    def colorBreakdown(self, image, outputImage=False):
        imageOut = []
        if outputImage:
            imageOut = image.copy()
            self.bucketer.reset_bias()
            print(self.bucketer.BIAS, self.bucketer.color_bases_bgr['white'], self.bucketer.color_bases_bgr['black'])

        histogram = dict.fromkeys(self.bucketer.color_bases_bgr.keys(), 0)
        rows, cols, depth = image.shape
        for r in range(rows):
            for c in range(cols):
                color = self.bucketer.bucket_color(image[r, c])
                histogram[color] += 1
                if outputImage:
                    imageOut[r, c] = self.bucketer.color_bases_bgr[color]
        total = float(sum(histogram.values()))
        # print(total)
        h2 = {}
        valid = []
        for color in histogram:
            print color, histogram[color]
            h2[color] = histogram[color]/total * 100
            if h2[color] > 5:
                valid.append(color)

        return (h2, valid, imageOut)

        
    def brightness_bgr(self, img):
        img_bnw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        brightness = img_bnw.mean()/255.0 * 100
        return brightness


def main():
    a = ColorAnalysis()

    img_bgr = cv.imread(sys.argv[1], cv.IMREAD_COLOR) #default BGR
    
    colBreakdown, colPresent, imgOut = a.colorBreakdown(img_bgr, True) 
    print(colBreakdown)
    cv.imshow('imageIn', img_bgr)
    cv.imshow('imageOut', imgOut)

    # cv.imshow("bnw", img_bnw)
    cv.waitKey(0)
    try:
        save = raw_input("To save, input file name. Else, press enter.\n")
        cv.imwrite(save, imgOut)
    except (EOFError, ValueError):
        pass
        
    cv.destroyAllWindows()
    # print(a.brightness_bgr(img_bgr))

    # img_hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)



main()