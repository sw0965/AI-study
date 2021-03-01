from selenium import webdriver
import time
from urllib import request
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

work_driver_path = "C:/Users/user/chromedriver.exe"
home_driver_path = "C:/Users/sangwoo/chromedriver.exe"
driver = webdriver.Chrome(home_driver_path)


driver.get("https://search.shopping.naver.com/search/all?query=%ED%99%94%EC%9E%A5%ED%92%88&frm=NVSHATC&prevQuery=%ED%99%94%EC%9E%A5%ED%92%88/")
driver.implicitly_wait(5)



page = driver.find_elements_by_css_selector('.pagination_btn_page__FuJaU')
print(len(page))


src = []

for i in map(str, range(1,30)):
    if driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div/div[2]/div[1]/a').is_displayed:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div/div[2]/div[1]/a').click()
    else:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div['+i+']/li/div[1]/div[2]/div[1]/a').click()
            

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(3)
    time.sleep(1)



    try:
        if driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/img'):
            imgs = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/img').get_attribute("src")
        
            # imgs.get_attribute("src")
        # src.append(imgs)
        


        elif driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div[1]/img'):
            imgs = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div[1]/img').get_attribute("src")

            # imgs.get_attribute("src")
        # src.append(imgs)
            
            

        else:
            imgs = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[2]/div[1]/div[3]/ul/li[1]/img').get_attribute("src")



        # imgs.get_attribute("src")
        
    except:
        pass
        
    src.append(imgs)

    print("포문 횟수:", i)
    print("길이:", len(src))
    print("이미지 소스:", src)
    time.sleep(1)

    driver.close()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# src.append(imgs)
