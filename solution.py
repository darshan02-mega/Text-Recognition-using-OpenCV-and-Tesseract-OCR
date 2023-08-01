import cv2
import pytesseract

# Read image from which text needs to be extracted
image_var = cv2.imread("Capture1234df.jpg")

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Convert the image to gray scale
gray_scale = cv2.cvtColor(image_var, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret_var, threshold = cv2.threshold(gray_scale, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(threshold, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
image = image_var.copy()

file_var = open("recognized.txt", "w+")
file_var.write("")
file_var.close()

for cnt in contours:
	x, y, w, h = cv2.boundingRect(cnt)
	
	# Drawing a rectangle on copied image
	rect = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	cropped = image[y:y + h, x:x + w]
	
	file_var = open("recognized.txt", "a")
	
	text = pytesseract.image_to_string(cropped)

	file_var.write(text)
	file_var.write("\n")
	file_var.close
