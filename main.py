import  pytesseract
import PIL.Image
import cv2
from pytesseract import Output
""""
Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
                        bypassing hacks that are Tesseract-specific."""

"""
OCR Engine Mode
0 Legacy engine only.
1 Neural nets LTSM engine only.
2 Legacy +LTSM engine.
3 Default ,based on what is available 
"""
myconfig = r"--psm 11  --oem 3"

# text = pytesseract.image_to_string(PIL.Image.open("street_sign.jpg"),config = myconfig)
# print(text)

img = cv2.imread("logos.jpg")
height ,width ,_ = img.shape

data = pytesseract.image_to_data(img, config=myconfig,output_type = Output.DICT)
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i])>20:
        (x,y,width,height) =(data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        img = cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
        img = cv2.putText(img , data['text'][i],(x,y+height+20), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)

         


# print(data['text'])
# boxes = pytesseract.image_to_boxes(img,config = myconfig)

# for box in boxes.splitlines():
#     box = box.split(" ")
#     img = cv2.rectangle(img,(int(box[1]),height - int(box[2])),(int(box[3]),height - int(box[4])),(0,0,255),2)

cv2.imshow("img",img)
cv2.waitKey(0)


