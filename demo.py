from PIL import Image
import cv2
import numpy as np
img=Image.open("C:/Users/DELL/Desktop/images/1.jpg")
img0=Image.open("C:/Users/DELL/Desktop/images/2.jpg")
img1 = Image.open("C:/Users/DELL/Desktop/images/3.jpg")
img2 = Image.open("C:/Users/DELL/Desktop/images/4.jpg")
img3=Image.open("C:/Users/DELL/Desktop/images/5.jpg")
img4=Image.open("C:/Users/DELL/Desktop/images/6.jpg")
img5=Image.open("C:/Users/DELL/Desktop/images/7.jpg")
img6=Image.open("C:/Users/DELL/Desktop/images/8.jpg")
img7=Image.open("C:/Users/DELL/Desktop/images/9.jpg")
img8=Image.open("C:/Users/DELL/Desktop/images/10.jpg")
img9=Image.open("C:/Users/DELL/Desktop/images/11.jpg")
img10=Image.open("C:/Users/DELL/Desktop/images/12.jpg")
result_img = Image.new('RGB', (img.width + img0.width, max(img.height, img0.height)))
result_img.paste(img, (0, 0))
result_img.paste(img0, (img.width, 0))
result_img.save('result.png')
result_img1 = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
result_img1.paste(img1, (0, 0))
result_img1.paste(img2, (img1.width, 0))
result_img1.save('result1.png')
result_img2=Image.new('RGB', (img3.width + img4.width, max(img3.height, img4.height)))
result_img2.paste(img3, (0, 0))
result_img2.paste(img4, (img3.width, 0))
result_img2.save('result2.png')
result_img3=Image.new('RGB', (img5.width + img6.width, max(img5.height, img6.height)))
result_img3.paste(img5, (0, 0))
result_img3.paste(img6, (img5.width, 0))
result_img3.save('result3.png')
result_img4=Image.new('RGB', (img7.width + img8.width, max(img7.height, img8.height)))
result_img4.paste(img7, (0, 0))
result_img4.paste(img8, (img7.width, 0))
result_img4.save('result4.png')
result_img5=Image.new('RGB', (img9.width + img10.width, max(img9.height, img10.height)))
result_img5.paste(img9, (0, 0))
result_img5.paste(img10, (img9.width, 0))
result_img5.save('result5.png')
cv2.waitKey()


