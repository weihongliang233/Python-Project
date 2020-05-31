# 导入包

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pag
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 登录
driver = webdriver.Edge('G:\\Edge浏览器下载\\edgedriver_win64\\msedgedriver.exe')
driver.get("http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn")
name = driver.find_element(By.NAME, 'username')
name.clear()
name.send_keys('weihl18')
password = driver.find_element(By.NAME, 'password')
password.clear()
password.send_keys('wei199903')
button_login = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div[3]/button')
button_login.click()

# 打开健康打卡小程序
button_app = driver.find_element_by_xpath('//*[@id="my-apps"]/li[5]')
ActionChains(driver).click(button_app).perform()

# 切换到frame中
driver.switch_to_frame('iframe')

# 判断是否已打卡
time.sleep(2)
xpath_of_concern = '/html/body/uni-app/uni-modal/div[2]/div[3]/div'
try:
    try:
        driver.find_element_by_xpath(
            xpath_of_concern).get_attribute('innerText') == '确定'
        print('已打卡')
        driver.find_element_by_xpath(xpath_of_concern).click()
    except:
        print('未打卡')
        tempretrue='/html/body/uni-app/div/div[2]/uni-picker-view/div/uni-picker-view-column[1]/div/div[3]/div[4]'
        concern_tempretrue='/html/body/uni-app/div/div[2]/div/div[2]'
        tempretrue_selector='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[8]/uni-view/uni-picker/div[2]/uni-view'

        driver.find_element_by_xpath(tempretrue_selector).click()
        driver.find_element_by_xpath(tempretrue).click()
        driver.find_element_by_xpath(concern_tempretrue).click()
except:
    print('过程失败')

tempretrue='/html/body/uni-app/div/div[2]/uni-picker-view/div/uni-picker-view-column[1]/div/div[3]/div[4]'
concern_tempretrue='/html/body/uni-app/div/div[2]/div/div[2]'
tempretrue_selector='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[9]/uni-view/uni-picker'
xpath_of_commit='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[12]/uni-button'


tempretrue_selector2='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[8]/uni-view/uni-picker'
driver.find_element_by_xpath(tempretrue_selector2).click()
time.sleep(2)
driver.find_element_by_xpath(tempretrue).click()
time.sleep(2)
driver.find_element_by_xpath(concern_tempretrue).click()
driver.find_element_by_xpath(xpath_of_commit).click()
print('执行完毕')


driver.find_element_by_xpath(tempretrue_selector).click()

/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[9]