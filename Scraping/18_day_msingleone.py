import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "http://m.singleone.co.kr/fom/fomobile/authority/viewLoginPage.fo"
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_id("text1").send_keys("201016")
browser.find_element_by_id("pass1").send_keys("cjfw110650")
browser.find_element_by_id("loginBtn").click()

time.sleep(2)
browser.find_element_by_xpath("//*[@id='container']/section/article/section[2]/ul/li[1]/a/span").click()
browser.find_element_by_link_text("주문 진행").click()

now = datetime.now()

file_name = os.path.join(r"C:\Users\dongyul.im\Desktop\result", "mso_sap_" + now.strftime("%m%d") + ".html")
with open(file_name, "w", encoding="utf8") as f:
    f.write(browser.page_source)

time.sleep(3)
browser.find_element_by_xpath("//*[@id='page47']/header/nav/span[2]").click()
alert = browser.switch_to.alert
alert.accept()

browser.find_element_by_xpath("//*[@id='container']/section/article/section[2]/ul/li[7]/a/span").click()
browser.find_element_by_id("searchInput").send_keys("백설 밀가루")
browser.find_element_by_class_name("btn-searh").click()

try:
    WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='itemList']/li[1]")))
    browser.find_element_by_xpath("//*[@id='itemList']/li[1]").click()

    WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.ID, "atImgSys3")))

    file_name = os.path.join(r"C:\Users\dongyul.im\Desktop\result", "mso_nas_" + now.strftime("%m%d") + ".html")
    with open(file_name, "w", encoding="utf8") as f:
        f.write(browser.page_source)

finally:
    browser.quit()
