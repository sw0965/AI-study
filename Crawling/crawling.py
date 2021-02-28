from selenium import webdriver
import time
from urllib import request

work_driver_path = "C:/Users/user/chromedriver.exe"
home_driver_path = "C:/Users/sangwoo/chromedriver.exe"
driver = webdriver.Chrome(home_driver_path)


driver.get("https://search.shopping.naver.com/search/all?query=%ED%99%94%EC%9E%A5%ED%92%88&frm=NVSHATC&prevQuery=%ED%99%94%EC%9E%A5%ED%92%88/")
driver.implicitly_wait(5)


# '//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div/div[2]/div[1]/a'
# '//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div[1]/div[2]/div[1]/a'
src = []
# title = driver.find_elements_by_css_selector(".basicList_title__3P9Q7")
# print(len(title))
for i in map(str, range(1,49)):
    if i==i:
        title = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div/div[2]/div[1]/a').click()
    else:
        title = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div[1]/div[2]/div[1]/a').click()
# //*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[6]/li/div/div[2]/div[1]/a

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(3)
    time.sleep(1)

    try:
        imgs = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/img').get_attribute("src")
    except:
        imgs = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div[1]/img').get_attribute(
            "src")
        

    src.append(imgs)

    print("포문 횟수:", i)
    print("이미지 소스:", src)
    print("길이:", len(src))
    time.sleep(1)

    driver.close()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)





'''
click_item = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a').click()
driver.switch_to.window(driver.window_handles[-1])
print(driver.window_handles)

time.sleep(3)
img_area = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/img').get_attribute("src")     #소스값 따오기
                                        //*[@id="content"]/div/div[2]/div[1]/div[1]/div[1]/img
                                        //*[@id="content"]/div/div[2]/div[1]/div[1]/div[1]/img
time.sleep(3)
urllib.request.urlretrieve(img_area, "C:/Users/user/Desktop/imgs/test.jpg")     # 사진 저장
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)




//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[2]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[3]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[4]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[6]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[7]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[8]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[9]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[6]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[8]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[0]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div[1]/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[2]/li/div/div[2]/div[1]/a
//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[3]/li/div[1]/div[2]/div[1]/a


'''