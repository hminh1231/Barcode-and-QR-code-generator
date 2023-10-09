import cv2

# Load image
img = cv2.imread('product_qr.png')

# Detect and decode
detector = cv2.QRCodeDetector()
data, bbox, rectified_img = detector.detectAndDecode(img)

print(data)