import os
from statistics import mean, stdev

from PIL import Image


ROOT_DIR = '/home/sihui/Documents/home_office_resize'
R = []
G = []
B = []

# a = [1, 2, 3]
# b = [0.1, 0.2, 0.3]
# print(stdev(a)/100)
# print(stdev(b))

def averagePixels(pic):
    # r, g, b = 0, 0, 0
    # count = 0
    for x in range(pic.size[0]):
        for y in range(pic.size[1]):
            tempr, tempg, tempb = pic.getpixel((x, y))
            # r += tempr
            # g += tempg
            # b += tempb
            # count += 1
            R.append(tempr)
            B.append(tempb)
            G.append(tempg)
    # return (r / count), (g / count), (b / count), count


lst = os.listdir(ROOT_DIR)
lst.sort()
num_img = 0

for subdir in lst:
    subdir_input = ROOT_DIR + "/" + subdir
    img_lst = os.listdir(subdir_input)
    img_lst.sort()
    for image_filename in img_lst:
        image_full_path = subdir_input + "/" + image_filename
        img = Image.open(image_full_path)
        # data = img.getdata()
        averagePixels(img)
        # R = R+r
        # B = B+b
        # G = G+g
        # print(r)
        # print(g)
        # print(b)
        num_img += 1
R_mean = mean(R)/256.0
B_mean = mean(B)/256.0
G_mean = mean(G)/256.0
R_std = stdev(R)/256.0
B_std = stdev(B)/256.0
G_std = stdev(G)/256.0
print(R_mean)
print(G_mean)
print(B_mean)
print(R_std)
print(G_std)
print(B_std)
print(num_img)
