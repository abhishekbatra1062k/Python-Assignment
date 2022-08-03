import cv2
import numpy as np

image=cv2.imread("./input.jpg")
mask=cv2.imread("./mask.png")

scale_percent=10
width=int(image.shape[1]*scale_percent/100)
height=int(image.shape[0]*scale_percent/100)
dim=(width, height)

resized_image=cv2.resize(image, dim)
resized_mask=cv2.resize(mask, dim)

result=cv2.bitwise_and(resized_image, resized_mask)

cv2.imwrite('./myResult.jpg',result)

cv2.imshow("Input Image", resized_image)
cv2.imshow("Input Mask", resized_mask)
cv2.imshow("Mask", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
