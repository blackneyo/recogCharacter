# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# '''
# tesseract 경로 등록
# pytesseract.image_to_string('대상')
# 이미지로부터 텍스트 추출
# '''
# print(pytesseract.image_to_string('IMG_1.png'))

import cv2
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# 설치한 tesseract 프로그램 경로
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# 이미지 불러오기, Gray 프로세싱
image = cv2.imread("IMG_1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장.
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# 이미지를 문자로
text = pytesseract.image_to_string(Image.open(filename), lang='KOR')
os.remove(filename)

print(text)

cv2.imshow("Image", image)
cv2.waitKey(0)
