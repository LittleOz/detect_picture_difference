# import the necessary packages
import cv2

# load the two input images
imageA = cv2.imread("dog.png")
imageB = cv2.imread("dog_dif.png")

# resize to 420 x 420
resA = cv2.resize(imageA,(680, 512), interpolation = cv2.INTER_CUBIC)
resB = cv2.resize(imageB,(680, 512), interpolation = cv2.INTER_CUBIC)

# convert the images to grayscale
grayA = cv2.cvtColor(resA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(resB, cv2.COLOR_BGR2GRAY)

# Subtraction two picture
dif = cv2.absdiff(grayA, grayB)
dif = cv2.blur(dif,(4,4))

# use threshold to high light the different pixel
thresh = 25
im_bw = cv2.threshold(dif, thresh, 255, cv2.THRESH_BINARY)[1]

# detect the edge
canny = cv2.Canny(im_bw, 50, 150)

# draw the result to original image
result = cv2.add(canny,grayB)

# show the image
cv2.imshow("A",grayA)
cv2.imshow("B",grayB)
cv2.imshow("result",result)
cv2.imshow("dif",dif)
cv2.imshow("im_bw",im_bw)
cv2.imshow("canny",canny)
cv2.waitKey(0)