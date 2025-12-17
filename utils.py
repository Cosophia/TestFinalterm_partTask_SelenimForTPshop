
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class UtilsDriver:
    driver = None
    @classmethod
    def get_driver(cls,url):
        cls.driver = webdriver.Firefox(service=Service("geckodriver.exe"))
        cls.driver.maximize_window()
        cls.driver.get(url)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        cls.get_driver().quit()
    @classmethod
    def get_android_driver(cls, url):
        huawei_user_agent = (
            "Mozilla/5.0 (Linux; Android 10; LIO-AN00) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/86.0.4240.185 Mobile Safari/537.36"
        )
        viewport_width = 360
        viewport_height = 780  # 视口高度（逻辑像素）
        # 配置 Firefox 选项
        options = webdriver.FirefoxOptions()
        options.set_preference("general.useragent.override", huawei_user_agent)
        # 启动浏览器
        cls.driver = webdriver.Firefox(options=options,service=Service("geckodriver.exe"))
        cls.driver.set_window_size(viewport_width, viewport_height)
        cls.driver.get(url)
        return cls.driver
