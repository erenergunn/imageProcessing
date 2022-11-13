import cv2
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('Pictures/picture1.jpg')

# Invert the image using cv2.bitwise_not
img_neg = cv2.bitwise_not(img)

plt.subplot(2,1,1),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,1,2),plt.imshow(img_neg)
plt.title('Negative'), plt.xticks([]), plt.yticks([])

plt.show()