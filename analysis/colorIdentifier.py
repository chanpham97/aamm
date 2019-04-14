from math import sqrt
import sys

'''
sources: https://www.compuphase.com/cmetric.htm
'''
class ColorBucketer:
    def __init__(self):
        self.BIAS = 0 # so only very white or very black colors identified as black
        self.MAX_DISTANCE = sqrt(255**2 + 255**2 + 255**2)

        self.color_bases = {
           'red': [0, 0, 255],
           'green': [0, 255, 0],
           'blue': [255, 0, 0],
           'yellow': [0, 255, 255],
           'pink': [255, 0, 255],
           'white': [255, 255, 255],
           'black': [0, 0, 0]
        }

        self.HUE_DIST = 10
        self.HUE_SV_MIN = 100
        self.HUE_SV_MAX = 255

        self.WHITE_S_MAX = 50
        self.BLACK_V_MAX = 50
        self.hue_bases = {
            'red': 0,
            'yellow': 30,
            'green': 60,
            'cyan': 90, 
            'blue': 120, 
            'magenta': 150
        }


    def set_bias(self, val=30):
        self.BIAS = val
        self.color_bases['white'] = [255 + self.BIAS, 255 + self.BIAS, 255 + self.BIAS]
        self.color_bases['black'] = [0 - self.BIAS, 0 - self.BIAS, 0 - self.BIAS]


    def reset_bias(self):
        self.BIAS = 0
        self.color_bases['white'] = [255, 255, 255]
        self.color_bases['black'] = [0, 0, 0]


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
        self.set_bias()
        min_color = ''
        min_distance = self.MAX_DISTANCE
        for cb in self.color_bases:
            color_base = self.color_bases[cb]
            if self.d(color_base, color_in) <= min_distance:
                min_color = cb
                min_distance = self.d(color_base, color_in)
        self.reset_bias()
        return min_color


    def bucket_hue(self, hue_in):
        h, s, v = hue_in
        if self.HUE_SV_MIN <= s <= self.HUE_SV_MAX and self.HUE_SV_MIN <= v <= self.HUE_SV_MAX:
            if (self.hue_bases['red'] - self.HUE_DIST) % 180 <= h or h <= self.hue_bases['red'] + self.HUE_DIST:
                return 'red'
            for hue in self.hue_bases:
                if self.hue_bases[hue] - self.HUE_DIST <= h <= self.hue_bases[hue] + self.HUE_DIST:
                    return hue
        # if s <= self.WHITE_S_MAX:
        #     return 'white'
        # if v <= self.BLACK_V_MAX:
        #     return 'black'
        return None
        

def main():
    b = ColorBucketer()
    input_col = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
    col = b.bucket_color(input_col)
    print(col)
    print(b.d(input_col, b.color_bases[sys.argv[4]]), b.d(input_col, b.color_bases[col]))
  