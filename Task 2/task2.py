import cv2

image = cv2.imread('download.jpg')

cv2.imshow("Original Image", image)
cv2.waitKey(0)

b_and_w_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Black and White Image", b_and_w_image)
cv2.waitKey(0)
inverted_image = 255 - b_and_w_image
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey()
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(b_and_w_image, inverted_blurred, scale=300.0)
cv2.imshow("Sketch Image", pencil_sketch)
cv2.waitKey(0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch Image", pencil_sketch)
cv2.waitKey(0)