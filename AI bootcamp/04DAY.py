

import cv2
import imutils
img=cv2.imread('./images/on-bulb.jpg')

# 1) *******RESIZING THE IMAGE*******
# resizeImg=imutils.resize(img,width=100)
# filename="resizedimage.png"
# cv2.imwrite(filename,resizeImg)
# print("successful")


# 2) *******BLURRED IMAGES *******
guassianblurr=cv2.GaussianBlur(img ,(25,25),0)
filename="blurredImage.png"
cv2.imwrite(filename, guassianblurr)
print("successful")