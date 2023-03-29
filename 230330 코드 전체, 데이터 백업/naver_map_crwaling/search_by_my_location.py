from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(driver_path) # 크롬 경로 받아오는걸 자동으로 해주는 라이브러리 설치 후 적용.
# Chrome 드라이버 실행
driver.maximize_window()

# 네이버 지도 페이지 접속
driver.get('https://m.map.naver.com/')

# 검색창에 내 위치 정보 입력
search_box = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/form/fieldset/div[1]/div/input')
search_box.send_keys('내 위치')
time.sleep(1)
search_box.send_keys(Keys.RETURN)




# chromedriver = '/Users/datakim/workspace/selenium_learning/chromedriver' # 크롬드라이버의 경로를 써줘야 그걸 불러와서 씀. 절대경로 쓰는게 편하다. 컴퓨터마다 다르니까 경로 찾아보고 적용
# driver = webdriver.Chrome(chromedriver) 
