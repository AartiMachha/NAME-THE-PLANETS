import cv2

img = cv2.imread("solar-system.jpg")


text_show = "Sun"
cv2.putText(img, text_show, (100,80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255, 255, 255))

text_show = "Mercury"
cv2.putText(img, text_show, (110,180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255, 255, 255))

text_show = "Venus"
cv2.putText(img, text_show, (190, 270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Earth"
cv2.putText(img, text_show, (300,270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Mars"
cv2.putText(img, text_show, (400,270), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Jupiter"
cv2.putText(img, text_show, (500,90), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Saturn"
cv2.putText(img, text_show, (720,110), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Uranus"
cv2.putText(img, text_show, (950,130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

text_show = "Neptune"
cv2.putText(img, text_show, (1080,130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(255,255,255))

cv2.imshow("displayImage", img)
print(img)
cv2.waitKey(0)

