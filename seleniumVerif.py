from time import sleep

from selenium.webdriver.common.by import By

from utils import UtilsDriver

url ="http://localhost/index.php"
driver = UtilsDriver.get_driver(url)
driver.get(url)
driver.find_element(By.PARTIAL_LINK_TEXT,"登录").click()
sleep(2)
driver.find_element(By.ID,"username").send_keys("13800138006 ")
driver.find_element(By.ID,"password").send_keys("123456 ")
sleep(5)
driver.find_element(By.NAME,"sbtbutton").click()
sleep(3)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div[1]/div/ul[1]/li[2]/a").click()
sleep(5)
# 捕获屏幕截图
screenshot = driver.get_screenshot_as_png()

# 保存截图到文件
with open("林浩杨作业截图.png", "wb") as file:
    file.write(screenshot)
driver.quit()