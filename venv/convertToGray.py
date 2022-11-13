import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading the image and converting to gray scale
img_original = cv2.imread('Pictures/picture1.jpg',)
gray_scale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


plt.subplot(2,1,1),plt.imshow(img_original)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,1,2),plt.imshow(gray_scale)
plt.title('Gray'), plt.xticks([]), plt.yticks([])

plt.show()