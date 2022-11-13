import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading the image
img = cv2.imread('Pictures/picture1.jpg')

# Apply log transformation method
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))
log_image = np.array(log_image, dtype=np.uint8)


plt.subplot(2,1,1),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,1,2),plt.imshow(log_image)
plt.title('Log Image'), plt.xticks([]), plt.yticks([])

plt.show()