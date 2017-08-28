import pytesseract
import cv2
from PIL import Image
import os

def OCRFunc(frame=None,path=None):
    if path is None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        text=pytesseract.image_to_string(Image.fromarray(gray))
        return text

    if frame is None:
        frame==cv2.imread(path)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        text=pytesseract.image_to_string(Image.fromarray(gray))
        return text
        
        
        

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    cv2.imshow("Capture",frame)
    
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('s')):
        break

cap.release()
cv2.destroyAllWindows()


# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray = cv2.medianBlur(gray, 3)
# filename = "temp.png"
# cv2.imwrite(filename,gray)

# text=pytesseract.image_to_string(Image.fromarray(gray))
text=OCRFunc(frame=frame)
# text=pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
print(text)
cv2.imshow("Image",frame)
# cv2.imshow("Output",gray)
cv2.waitKey(0)