#  1) *******to read and display image  *******

# import cv2
# img=cv2.imread('./images/on-bulb.jpg')
# cv2.imshow('New logo',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#   2) *******to read and display and SAVE the  image  *******

# import cv2
# img=cv2.imread('./images/on-bulb.jpg')
# filename='savedImageTest.png'
# cv2.imwrite(filename,img)
# print("iamge is successfully saved")


# 3) *******to convert coloured image in gray colour image *******

# import cv2
# img=cv2.imread('./images/on-bulb.jpg')
# grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("orig",img)
# cv2.imshow("Gray",grayImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# filename='savedImageTestGray.png'
# cv2.imwrite(filename,img)
# print("iamge is successfully saved")


# 4) *******to convert thresold(colour density) *******

# import cv2
# img=cv2.imread('./images/on-bulb.jpg')
# grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# thresImg=cv2.threshold(grayImg,100,255,cv2.THRESH_BINARY)[1]
# filename='ThresoldImg2.png'
# cv2.imwrite(filename ,thresImg)
# print("image is successfully saved")

# 5) *******IMAGE PROPERTIES *******
import cv2
img=cv2.imread('./images/on-bulb.jpg')
print(img.shape)
print(img.size)
print(img.dtype)


