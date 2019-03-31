from colorIdentifier import ColorBucketer
import cv2 as cv

class ColorAnalysis: 
    def __init__(self):
        self.bucketer = ColorBucketer()

    def evalHistogram(self, image):
        histogram = dict.fromkeys(self.bucketer.color_bases.keys(), 0)
        rows, cols, depth = image.shape
        for r in range(rows):
            for c in range(cols):
                histogram[self.bucketer.bucket_color(image[r, c])] += 1
        return histogram

a = ColorAnalysis()

img = cv.imread('rainbow.png', cv.IMREAD_COLOR) #default BGR
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #colAn needs RGB

hist = a.evalHistogram(img)
print(hist)