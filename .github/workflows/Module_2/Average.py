import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread(r".github\workflows\Module_2\Week_1\dog.jpeg")
height, width, channel = img.shape
gray_img_01 = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        gray_img_01[i][j] = sum(img[i][j])/3
print(gray_img_01[0][0])
