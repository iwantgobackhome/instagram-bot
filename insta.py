import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import random


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self, email, pw):
        # 인스타 로그인 페이지 열기
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(2)

        # 이름과 패스워드 입력
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys(email)
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(pw)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # 로그인 정보 저장 팝업 지우기
        login_data_save = self.driver.find_element(by=By.CSS_SELECTOR, value=".cmbtv button")
        login_data_save.click()
        time.sleep(2)

        # 알림 팝업 지우기
        notification_setting = self.driver.find_element(by=By.CSS_SELECTOR, value="._a9-v ._a9-z ._a9_1")
        notification_setting.click()
        time.sleep(2)

    def find_followers(self, find_value):
        # 검색창에 찾고 싶은계정 입력
        search_input = self.driver.find_element(by=By.CSS_SELECTOR, value="._aawf input")
        search_input.send_keys(find_value)
        time.sleep(2)

        # 검색결과 첫번째 누르기
        search_account = self.driver.find_element(by=By.CSS_SELECTOR, value="._abn- ._aa61 ._aeul div a")
        search_account.click()
        time.sleep(3)

        # 팔로워 버튼 누르기
        followers_button = self.driver.find_element(by=By.CSS_SELECTOR, value="._aa_7 li a")
        followers_button.click()
        time.sleep(3)

        # 스크롤 하기
        scoll = self.driver.find_element(by=By.CSS_SELECTOR, value="._ab8w ._aano")
        for i in range(15):
            self.driver.execute_script("arguments[0].scrollBy(0, 300)", scoll)
            time.sleep(2)

    def follow(self):
        # 팔로워 목록 가져오기
        followers_list = self.driver.find_elements(by=By.CSS_SELECTOR, value="._aano ul li ._aaes button")
        for followers in followers_list:
            try:
                followers.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                unfollower_cancel = self.driver.find_element(by=By.CSS_SELECTOR, value="._a9-z ._a9_1")
                unfollower_cancel.click()
            else:
                time.sleep(random.randint(1, 10))

        print(len(followers_list))