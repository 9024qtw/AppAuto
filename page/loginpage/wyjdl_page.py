from base.basepage import BassPage
from selenium.webdriver.common.by import By
from base.start import Start
from selenium import webdriver
from time import sleep

class Wyjdl(BassPage):
    # 同意按钮
    btn_agree = (By.XPATH, '//*[@text=\'同意\']')
    # 不同意按钮
    btn_disagree = (By.XPATH, '//android.widget.TextView[@text=\'不同意\']')
    # 输入手机号
    enter_PhoneNumber = (By.XPATH, '//android.widget.EditText[@text=\'请输入手机号码\']')
    # 获取验证码按钮
    btn_GetCode = (By.XPATH, '//android.widget.TextView[@text=\'获取验证码\']')
    # 输入验证码
    enter_Code = (By.XPATH, '//android.widget.EditText[@text=\'请输入验证码\']')
    # 登录按钮
    btn_login = (By.XPATH, '//android.widget.TextView[@text=\'登录/注册\']')

    def login(self):
        # if self.find(self.btn_agree):
        self.click(self.btn_agree)
        self._input(self.enter_PhoneNumber, '13151565010')
        self.click(self.btn_GetCode)
        self._input(self.enter_Code, '5010')
        self.click(self.btn_login)


if __name__ == '__main__':
    driver = Start.start()
    sleep(5)
    a = Wyjdl(driver)
    a.login()
