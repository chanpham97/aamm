from math import sqrt
import sys

'''
sources: https://www.compuphase.com/cmetric.htm
'''
class ColorBucketer:
    def __init__(self):
        #assumes bgr
        self.color_bases = {
           'red': [0, 0, 255],
           'green': [0, 255, 0],
           'blue': [255, 0, 0],
           'yellow': [0, 255, 255],
           'pink': [255, 0, 255],
           'white': [255, 255, 255],
           'black': [0, 0, 0]
           #'light-blue': [0, 255, 255] #potentially remove later
        }
        self.MAX_DISTANCE = sqrt(255**2 + 255**2 + 255**2)


    def d(self, c1, c2):
        # select weighting based on red presence
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        # return sqrt(((r1-r2)**2) + ((g1-g2)**2) + ((b1-b2)**2))

        if r1 >= 128 and r2 >= 128:
            return sqrt(3*((r1-r2)**2) + 4*((g1-g2)**2) + 2*((b1-b2)**2))
        else:
            return sqrt(2*((r1-r2)**2) + 4*((g1-g2)**2) + 3*((b1-b2)**2))


    def bucket_color(self, color_in):
        min_color = ''
        min_distance = self.MAX_DISTANCE
        for cb in self.color_bases:
            color_base = self.color_bases[cb]
            if self.d(color_base, color_in) <= min_distance:
                min_color = cb
                min_distance = self.d(color_base, color_in)
        return min_color


    def main(self):
        b = ColorBucketer()
        input_col = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
        col = b.bucket_color(input_col)
        print(col)
        print(b.d(input_col, b.color_bases[sys.argv[4]]), b.d(input_col, b.color_bases[col]))
  
  
    # def show_colormap(self):


