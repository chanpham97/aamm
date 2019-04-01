from colorIdentifier import ColorBucketer
import cv2 as cv
import sys

class ColorAnalysis: 
    def __init__(self):
        self.bucketer = ColorBucketer()

    def colorBreakdown(self, image):
        histogram = dict.fromkeys(self.bucketer.color_bases.keys(), 0)
        rows, cols, depth = image.shape
        for r in range(rows):
            for c in range(cols):
                histogram[self.bucketer.bucket_color(image[r, c])] += 1
        total = float(sum(histogram.values()))
        print(total)
        h2 = {}
        valid = 0
        for color in histogram:
            print color, histogram[color]
            h2[color] = histogram[color]/total * 100
            if h2[color] > 5:
                valid += 1

        return (h2, valid)

        
    def brightness(self, img):
        img_bnw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        brightness = img_bnw.mean()/255.0 * 100
        return brightness


def main():
    a = ColorAnalysis()

    img = cv.imread(sys.argv[1], cv.IMREAD_COLOR) #default BGR
    colSummary = a.colorBreakdown(img) 
    print(colSummary)

    # cv.imshow("bnw", img_bnw)
    # cv.waitKey(0)
    print(a.brightness(img))


main()