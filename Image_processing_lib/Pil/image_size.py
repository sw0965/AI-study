from PIL import Image
import matplotlib.pyplot as plt

image = Image.open('D:/8dnjf5/sambong_small.png')   # 이미지 불러오기 (이미지 사이즈 = 446, 552)

width, height = image.size   # 이미지 사이즈 보기 width, height

print(width, height)    # 466, 552

# 이미지 사이즈 변경하기
resize_image = image.resize((500, 500)) # 500, 500 사이즈로 변경

width, height = resize_image.size   # 사이즈 보기

print(width, height)    # 500, 500

# 큰 사이즈 이미지에서 작은 사이즈 이미지로 변경시 이미지 깨지지 않게 저장하기

big_size_image = Image.open('D:/8dnjf5/sambong.jpg')    # 2000, 2000 사이즈 이미지

# big_size_image.show()   # 큰 원본 이미지 보기

resize_big_image1 = image.resize((200, 200))    # 100, 100 으로 사이즈 변경
resize_big_image1 = resize_big_image1.convert("RGB")
resize_big_image1.save("./resize_big_image1.jpg", format='jpeg', quality=100)

# resize_big_image1.show()    # 100, 100 사이즈로 변경한 이미지 보기

resize_big_image2 = image.resize((200, 200), Image.ANTIALIAS)   # 안티엘리싱 추가
resize_big_image2 = resize_big_image2.convert("RGB")
resize_big_image2.save("./resize_big_image2.jpg", format='jpeg', quality=100)

# resize_big_image2.show()

# matplotlib 를 이용해 이미지 여러장 한번에 보기

title = "big_size_image \n(2000x2000)"
plt.subplot(1, 3, 1)
plt.title(title)
plt.imshow(big_size_image)

title = "resize_big_image1 \n(200x200)"
plt.subplot(1, 3, 2)
plt.title(title)
plt.imshow(resize_big_image1)

title = "resize_big_image2 \n(200x200) \nANTIALIAS"
plt.subplot(1, 3, 3)
plt.title(title)
plt.imshow(resize_big_image2)

plt.show()

