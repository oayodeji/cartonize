# import the package
import cv2
 
image = cv2.imread('images/dog.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray  = cv2.medianBlur(image_gray, 5)

edges = cv2.Laplacian(grayimg , cv2.CV_8U, ksize=5)
r,mask =cv2.threshold(edges,100,255,cv2.THRESH_BINARY_INV)
masked_image = cv2.bitwise_and(image, image, mask=mask)
masked_image = cv2.medianBlur(img2, 5)
 
cv2.imwrite("dog_cartoon.jpg", mask)
