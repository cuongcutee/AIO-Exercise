import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread(r".github\workflows\Module_2\Week_1\dog.jpeg")
gray_img_01 = np.dot(img, [0.21, 0.72, 0.07])
print(gray_img_01[0][0])
