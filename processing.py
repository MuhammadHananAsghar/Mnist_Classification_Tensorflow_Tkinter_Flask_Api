from PIL import Image
import cv2

image = cv2.imread("3fc0dd7770614b2daef725f2e066f5da.png", cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Image", im_bw)
cv2.waitKey(0)