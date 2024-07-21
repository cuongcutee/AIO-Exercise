import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
background = cv2.imread(r"Module_2/Week_2/GreenBackground.png")
new_back_ground = cv2.imread(r"Module_2\Week_2\NewBackground.jpg")
object = cv2.imread(r"Module_2\Week_2\Object.png")

# convert color from BGR to RGB
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
new_back_ground = cv2.cvtColor(new_back_ground, cv2.COLOR_BGR2RGB)
new_back_ground = cv2.resize(new_back_ground, (678, 381))
object = cv2.cvtColor(object, cv2.COLOR_BGR2RGB)

# type casting
background = background.astype("float")
new_back_ground = new_back_ground.astype("float")
object = object.astype("float")

# compute distance from background to object to know which pixel is background
distance = np.abs(background-object)
vector = np.array([1/3, 1/3, 1/3])
distance = np.dot(distance, vector)
distance = np.array(distance > 0.4)

# create a new picture
height, width, channel = background.shape
new_picture = np.zeros((height, width, channel))
for i in range(height):
    for j in range(width):
        if distance[i][j] == False:
            new_picture[i][j] = new_back_ground[i][j]
        else:
            new_picture[i][j] = object[i][j]
# astype int
new_picture = new_picture.astype(np.uint8)

plt.imshow(new_picture)
plt.show()
