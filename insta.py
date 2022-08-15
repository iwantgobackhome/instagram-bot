import selenium.common.exceptions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from random_user_agent.user_agent import UserAgent          # 랜덤 유저 에이전트 패키지
from random_user_agent.params import SoftwareName, OperatingSystem


class Insta:
    def __init__(self):
        self.user_agent = None
        self.options = Options()
        self.driver = None

    def login(self, email, pw, show_window_mode):
        # self.get_user_agent()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        # 관측모드 확인
        if show_window_mode == 0:
            self.options.add_argument("headless")
            self.options.add_argument("no-sandbox")

        self.options.add_argument("--start-maximized")
        self.options.add_argument("disabled-gpu")
        self.options.add_argument('user-agent='+self.user_agent)     # 크롤링 차단 방지 user-agent 추가
        self.options.add_argument("lang=ko_KR")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        # 인스타 로그인 페이지 열기
        self.driver.get("https://www.instagram.com/accounts/login/",)
        self.driver.implicitly_wait(10)

        # 이름과 패스워드 입력
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys(email)
        print("id입력")
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(pw)
        print("패스워드 입력")
        password.send_keys(Keys.ENTER)
        print("로그인")
        self.driver.implicitly_wait(10)

        try:
            # 로그인 정보 저장 팝업 지우기
            print("로그인 성공")
            login_data_save = self.driver.find_element(by=By.CSS_SELECTOR, value=".cmbtv button")
            login_data_save.click()
            print("로그인 팝업 지우기")

            if show_window_mode == 1:
                # 알림 팝업 지우기
                notification_setting = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._a9-v ._a9-z ._a9_1")))
                notification_setting.click()
                print("알림 팝업 지우기")
                time.sleep(2)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            self.driver.close()
            return False

    def search(self, find_value):
        # 검색창에 찾고 싶은계정 입력
        search_input = self.driver.find_element(by=By.CSS_SELECTOR, value="._aawf input")
        search_input.send_keys(find_value)
        time.sleep(2)

        # 검색결과 첫번째 누르기
        search_account = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._abn- ._aa61 ._aeul div a")))
        # search_account = self.driver.find_element(by=By.CSS_SELECTOR, value="._abn- ._aa61 ._aeul div a")
        search_account.click()
        self.driver.implicitly_wait(10)

    def click_follow_button(self):
        # 팔로워 버튼 누르기
        followers_button = self.driver.find_element(by=By.CSS_SELECTOR, value="._aa_7 li a")
        followers_button.click()
        time.sleep(3)

        # 스크롤 하기
        scoll = self.driver.find_element(by=By.CSS_SELECTOR, value="._ab8w ._aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollBy(0, 620)", scoll)
            time.sleep(4)

    def account_follow(self, count, delay, delay_check):
        # 팔로워 목록 가져오기
        followers_list = self.driver.find_elements(by=By.CSS_SELECTOR, value="._ab8w ._aano ._ab94 ._abb0 ._acap")
        followers_id = self.driver.find_elements(by=By.CSS_SELECTOR, value="._ab8w ._aano ._ab94 ._ab9o a")

        followed_list = []
        counter = 0
        for index in range(0, len(followers_list)):
            if followers_list[index].text == "팔로우":         # 아직 팔로우 안한 계정 확인
                followers_list[index].click()
                counter += 1
                print(f"ID: {followers_id[index+1].text}      count: {counter}")
                followed_list.append(followers_id[index+1].text)
                if delay_check == 0:
                    time.sleep(delay)
                else:
                    time.sleep(random.randint(10, delay + 1))
                if counter == count:
                    break
            else:                                             # 이미 팔로우 한 계정이라 언팔 안하기 위해 pass
                pass

        return followed_list

    def use_tag_mode(self, count, delay, delay_check, comment_value, mode_num):
        counter = 0
        account_id_list = []
        # 첫번째 피드
        first_newest_pids = self.driver.find_element(by=By.CSS_SELECTOR,
                                                     value=".rq0escxv ._a993 ._aao7 div ._ac7v ._aabd")
        first_newest_pids.click()

        for i in range(0, count):
            # 피드 계정이 로드 될때까지 최대 5초 기다림, 즉 피드가 로드 될때까지 기다림
            account_id = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rq0escxv ._aata ._aasw ._aasi ._aaqy .futnfnd5 a")))
            account_id_list.append(account_id.text)

            if mode_num in (1, 4, 5, 7):
                # 팔로우 버튼
                follow_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv ._aata ._aasw ._aasi ._aaqy ._aar2 button ._ab8w")
                if follow_button.text == "팔로우":
                    follow_button.click()
                    time.sleep(1)

            if mode_num in (2, 4, 6, 7):
                # 좋아요 버튼
                like_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv .pi61vmqs ._aata ._aasx ._aamw button")
                like_button.click()

            if mode_num in (3, 5, 6, 7):
                # 댓글
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rq0escxv ._aata ._aasw ._aasx textarea")))
                    comment_area = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv ._aata ._aasw ._aasx textarea")
                    comment_area.click()
                    # StaleElementReferenceException 에러 발생하여 다시 가져오기
                    comment_area = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv ._aata ._aasw ._aasx ._aaoe ._aao9 ._ablz")
                    comment_area.send_keys(comment_value)
                    # 댓글 전송 버튼
                    send_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv ._aata ._aasw ._aasx ._aaoe ._aao9 ._acan")
                    send_button.click()
                    # comment_area.send_keys(Keys.ENTER)
                except selenium.common.exceptions.TimeoutException:     # 간혹 댓글 차단 게시글 있으면 넘어가기
                    pass
                except selenium.common.exceptions.ElementClickInterceptedException:     # 마지막 댓글 전송하면 계속 해당 오류발생하기에 pass처리
                    pass
            counter += 1
            print(f"계정: {account_id_list[i]} 횟수: {counter}")

            # 딜레이
            if delay_check == 0:
                time.sleep(delay)
            else:
                time.sleep(random.randint(10, delay + 1))

            # 지정한 개수만큼 수행하면 피드 닫기
            if counter == count:
                close_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv .o9tjht9c .futnfnd5")
                close_button.click()
                break
            # 다음 게시글
            try:
                next_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".rq0escxv ._a3gq ._aank ._aaqg ._abl-")
                next_button.click()
            except selenium.common.exceptions.NoSuchElementException:
                # 간혹 더 이상의 게시글이 없을때
                account_id_list.append("더 이상의 게시물이 없습니다.")
                break

        return account_id_list

    def close_insta(self):
        self.driver.close()

    def get_user_agent(self):               # 랜덤으로 유저 에이전트 가져오는 메서드
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value]

        user_agent_rotator = UserAgent(software_names=software_names,operating_systems=operating_systems, limit=100)
        self.user_agent = user_agent_rotator.get_random_user_agent()