import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

# 1. Naver 이동
browser.get("http://naver.com")

# 2. 로그인
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id/pw 입력
browser.find_element_by_id("id").send_keys("dongyulim")
browser.find_element_by_id("pw").send_keys("dladong102")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# # time.sleep(3)
# # # 5. id 새로 입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# 6. html 출력
print(browser.page_source)
# browser.close() # 현재탭만 종료
browser.quit()