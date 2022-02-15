import cv2 as cv
import re

def mk_thumbnail(source):

    vid_cap = cv.VideoCapture(source)
    vid_cap.set(cv.CAP_PROP_POS_FRAMES, 1) # CAP_PROP_POS_FRAMES 동영상의 현재 프레임 수    현재 CAP_PROP_POS_FRAMES = 1 뒤에 1은 표시하고 싶은 프레임(장면)

    success, image = vid_cap.read() # success = true or false 반환  image = 해당 프레임 이미지
    vid_cap.release()

    name = re.split(r'[/.]', source)[-2]

    cv.imwrite("thumbnail/{}.png".format(name), image)
    return image

# video = "C:/Users/HSW-PC/Desktop/video_test/호랑이약방_광고.mp4"
# video = "C:/Users/HSW-PC/Desktop/video_test/호랑이약방_광고2.wmv"
# video = "http://t11.fiction-a.com:8121/app_files/FictionAFiles/2021/06/02/tiger_video.mp4"
# mk_thumbnail(video)







