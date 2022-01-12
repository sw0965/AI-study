from PIL import Image
import matplotlib.pyplot as plt

dog = Image.open('D:/8dnjf5/sambong_small.png')   # 이미지 불러오기 (이미지 사이즈 = 446, 552)

row = 1     # 이미지 보여줄때 행 수
column = 2  # 이미지 보여줄때 열 수
index = 1   # 이미지 순번

# 이미지 한개
title = "dog image"     # 이미지 제목
plt.subplot(row, column, index) # 이미지 배치
plt.title(title)    # 이미지 타이틀 설정
plt.imshow(dog)

plt.show()

# 이미지 두개
dog = Image.open('D:/8dnjf5/sambong_small.png')   # 이미지 불러오기 (이미지 사이즈 = 446, 552)
pentagon = Image.open('D:/img_project/cosmetic_img/test_img/5253.png')   # 이미지 불러오기 (이미지 사이즈 = 446, 552)

title = "dog image"     # 이미지 제목
plt.subplot(row, column, 2) # 이미지 배치
plt.title(title)    # 이미지 타이틀 설정
plt.imshow(dog)

title = "pentagon image"     # 이미지 제목
plt.subplot(row, column, 1) # 이미지 배치
plt.title(title)    # 이미지 타이틀 설정
plt.imshow(pentagon)

plt.show()


# title = "resize_big_image1 \n(200x200)"
# plt.subplot(1, 3, 2)
# plt.title(title)
# plt.imshow(image)
#
# title = "resize_big_image2 \n(200x200) \nANTIALIAS"
# plt.subplot(1, 3, 3)
# plt.title(title)
# plt.imshow(image)