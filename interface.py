from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from insta import *


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("instagram bot ver 1.0")
        self.window.geometry("618x485")
        self.insta_img = PhotoImage(file="image/insta_color2.png")
        self.window.iconbitmap("image/insta_color.ico")

        # 상단
        self.top_frame = Frame(width=620, height=60, relief="raised", borderwidth=1, bg="white")
        self.top_label = Label(self.top_frame, text="Instagram", font=("Ebrima", 24, "bold"), fg="#E1306C", bg="white")
        self.top_label.place(x=255, y=0)
        self.top_canvas = Canvas(self.top_frame, width=40, height=40, bg="white", highlightthickness=0)
        self.top_logo = self.top_canvas.create_image(21, 21, image=self.insta_img)
        self.top_canvas.place(x=205, y=6)
        self.top_frame.grid(row=0, column=0, columnspan=2)

        # 로그인
        self.login_frame = LabelFrame(text="login", relief="raised", borderwidth=1, width=300, height=100)
            # id
        self.id_label = Label(self.login_frame, text="ID:")
        self.id_label.place(x=35, y=13)
        self.id_box = Entry(self.login_frame, width=20)
        self.id_box.place(x=55, y=13)
            # pw
        self.pw_label = Label(self.login_frame, text="PW:")
        self.pw_label.place(x=30, y=43)
        self.pw_box = Entry(self.login_frame, width=20, show="*")
        self.pw_box.place(x=55, y=43)
            # login button
        self.login_button = Button(self.login_frame, text="login", width=8, height=3, command=self.click_login)
        self.login_button.place(x=205, y=10)
        self.login_frame.place(x=25, y=70)

        # 출력
        self.print_frame = Frame()
            # scroll
        self.list_box_scroll = Scrollbar(self.print_frame)
        self.list_box_scroll.pack(side="right", fill="y")
            # print_box
        self.list_box = Listbox(self.print_frame, width=30, height=25, yscrollcommand=self.list_box_scroll.set)
        self.list_box.pack(side="left")
        self.list_box_scroll.config(command=self.list_box.yview)
        self.print_frame.place(x=360, y=77)

        # 설정
        self.setting_frame = LabelFrame(text="setting", relief="raised", borderwidth=1, padx=10, pady=10)
            # show_window
        self.show_window_value = IntVar()
        self.show_window_check = Checkbutton(self.setting_frame, text="관측 모드", variable=self.show_window_value)
        self.show_window_check.grid(row=0, column=0, columnspan=2, sticky="w")
            # follow
        self.follow_check_value = IntVar()                  # 체크 상태 확인 변수
        self.follow_check = Checkbutton(self.setting_frame, text="팔로우", variable=self.follow_check_value)
        self.follow_check.grid(row=1, column=0, pady=5)
        self.follow_mode = ["태그로 팔로우", "계정으로 팔로우"]
        self.follow_combo = ttk.Combobox(self.setting_frame, width=15, values=self.follow_mode, postcommand=self.follow_combo_check)
        self.follow_combo.current(0)     # 기본 값
        self.follow_combo.grid(row=1, column=1, sticky="w")
        # self.follow_combo.bind('<Button-1>', self.follow_combo_check)

            # like
        self.like_check_value = IntVar()
        self.like_check = Checkbutton(self.setting_frame, text="좋아요", variable=self.like_check_value)
        self.like_check.grid(row=2, column=0, pady=5)

            # tag
        self.tag_entry = Entry(self.setting_frame, width=20, fg="gray")
        self.tag_entry.insert(END, "태그나 계정을 입력하세요")
        self.tag_entry.grid(row=2, column=1, sticky="w")
        self.tag_entry.bind('<Button-1>', self.tag_clear)       # 클릭하면 지워짐

            # comment
        self.comment_check_value = IntVar()
        self.comment_check = Checkbutton(self.setting_frame, text="댓글   ", variable=self.comment_check_value)
        self.comment_check.grid(row=3, column=0)
        self.comment_entry = Text(self.setting_frame, width=30, height=5, fg="gray")
        self.comment_entry.insert(0.0, "댓글 내용을 입력하세요")
        self.comment_entry.bind('<Button-1>', self.comment_clear)
        self.comment_entry.grid(row=3, column=1, rowspan=5, pady=15)

            # count
        self.count_label = Label(self.setting_frame, text="개수")
        self.count_label.grid(row=8, column=0)
        self.count_entry = Entry(self.setting_frame, width=24, fg="gray")
        self.count_entry.insert(0, "하루 100개 이하를 추천합니다")
        self.count_entry.bind('<Button-1>', self.count_clear)
        self.count_entry.grid(row=8, column=1, sticky="w", pady=5)

            # delay
        self.delay_label = Label(self.setting_frame, text="  딜레이")
        self.delay_label.grid(row=9, column=0)
        self.delay_entry = Entry(self.setting_frame, width=15, fg="gray")
        self.delay_entry.insert(0, "10초 이상(초단위)")
        self.delay_entry.bind('<Button-1>', self.delay_clear)
        self.delay_entry.grid(row=9, column=1, sticky="w")

            # delay mode
        self.delay_safe_mode_value = IntVar()
        self.delay_safe_mode = Checkbutton(self.setting_frame, text="봇감지 회피", variable=self.delay_safe_mode_value)
        self.delay_safe_mode.grid(row=9, column=1, sticky="e")

        self.setting_frame.place(x=25, y=193)

        self.window.mainloop()

        self.mode_num = 0

    # clear 매서드는 각 입력창의 기본값을 클릭하면 지우고 쓰는 역할
    def tag_clear(self, event):     # 매개변수 event 안써주면 안됨
        if self.tag_entry.get() == "태그나 계정을 입력하세요":
            self.tag_entry.delete(0, END)
            self.tag_entry.config(fg="black")
        if self.comment_entry.get(0.0, END) == "\n":
            self.comment_entry.insert(0.0, "댓글 내용을 입력하세요")
            self.comment_entry.config(fg="gray")
        if self.count_entry.get() == "":
            self.count_entry.insert(0, "하루 100개 이하를 추천합니다")
            self.count_entry.config(fg="gray")
        if self.delay_entry.get() == "":
            self.delay_entry.insert(0, "10초 이상(초단위)")
            self.delay_entry.config(fg="gray")
        self.follow_combo_check()

    def comment_clear(self, event):
        if self.comment_entry.get(0.0, END) == "댓글 내용을 입력하세요\n":        # text박스는 insert하면 끝에 \n 들어감
            self.comment_entry.delete(0.0, END)
            self.comment_entry.config(fg="black")
        if self.tag_entry.get() == "":
            self.tag_entry.insert(0, "태그나 계정을 입력하세요")
            self.tag_entry.config(fg="gray")
        if self.count_entry.get() == "":
            self.count_entry.insert(0, "하루 100개 이하를 추천합니다")
            self.count_entry.config(fg="gray")
        if self.delay_entry.get() == "":
            self.delay_entry.insert(0, "10초 이상(초단위)")
            self.delay_entry.config(fg="gray")
        self.follow_combo_check()

    def count_clear(self, event):
        if self.count_entry.get() == "하루 100개 이하를 추천합니다":
            self.count_entry.delete(0, END)
            self.count_entry.config(fg="black")
        if self.tag_entry.get() == "":
            self.tag_entry.insert(0, "태그나 계정을 입력하세요")
            self.tag_entry.config(fg="gray")
        if self.comment_entry.get(0.0, END) == "\n":
            self.comment_entry.insert(0.0, "댓글 내용을 입력하세요")
            self.comment_entry.config(fg="gray")
        if self.delay_entry.get() == "":
            self.delay_entry.insert(0, "10초 이상(초단위)")
            self.delay_entry.config(fg="gray")

    def delay_clear(self, event):
        if self.delay_entry.get() == "10초 이상(초단위)":
            self.delay_entry.delete(0, END)
            self.delay_entry.config(fg="black")
        if self.tag_entry.get() == "":
            self.tag_entry.insert(0, "태그나 계정을 입력하세요")
            self.tag_entry.config(fg="gray")
        if self.comment_entry.get(0.0, END) == "\n":
            self.comment_entry.insert(0.0, "댓글 내용을 입력하세요")
            self.comment_entry.config(fg="gray")
        if self.count_entry.get() == "":
            self.count_entry.insert(0, "하루 100개 이하를 추천합니다")
            self.count_entry.config(fg="gray")


# 팔로우 모드에 따른 체크버튼 비활성화
    def follow_combo_check(self):
        if self.follow_combo.get() == "계정으로 팔로우":
            self.comment_check.deselect()
            self.like_check.deselect()
            self.comment_check.config(state="disabled")
            self.like_check.config(state="disabled")
        else:
            self.comment_check.config(state="active")
            self.like_check.config(state="active")

# 리스트박스(출력창)에 넣는 메서드
    def insert_list_box(self, do_list):
        for i in do_list:
            self.list_box.insert(END, i)

    def click_login(self):
        user_id = self.id_box.get()
        user_pw = self.pw_box.get()
        count_value = self.count_entry.get()
        delay_value = self.delay_entry.get()
        tag_value = self.tag_entry.get()
        comment_value = self.comment_entry.get(0.0, END)

        follow_check = self.follow_check_value.get()        # 0이면 체크해제, 1이면 체크
        like_check = self.like_check_value.get()
        comment_check = self.comment_check_value.get()
        delay_check = self.delay_safe_mode_value.get()
        show_window_check = self.show_window_value.get()
        account_follow = self.follow_combo.get() == "계정으로 팔로우"

        # 모드 bool 변수
        account_follow_mode = account_follow and follow_check == 1 and like_check == 0 and comment_check == 0
        only_follow_mode = follow_check == 1 and like_check == 0 and comment_check == 0 and not account_follow
        only_like_mode = follow_check == 0 and like_check == 1 and comment_check == 0 and not account_follow
        only_comment_mode = follow_check == 0 and like_check == 0 and comment_check == 1 and not account_follow
        follow_like_mode = follow_check == 1 and like_check == 1 and comment_check == 0 and not account_follow
        follow_comment_mode = follow_check == 1 and like_check == 0 and comment_check == 1 and not account_follow
        like_comment_mode = follow_check == 0 and like_check == 1 and comment_check == 1 and not account_follow
        all_mode = follow_check == 1 and like_check == 1 and comment_check == 1 and not account_follow

        # 각 모드별 숫자를 매겨서 함수 호출시에 관리
        if only_follow_mode:
            self.mode_num = 1
        elif only_like_mode:
            self.mode_num = 2
        elif only_comment_mode:
            self.mode_num = 3
        elif follow_like_mode:
            self.mode_num = 4
        elif follow_comment_mode:
            self.mode_num = 5
        elif like_comment_mode:
            self.mode_num = 6
        elif all_mode:
            self.mode_num = 7

        # 아이디하고 비밀번호 공백인지 확인
        if user_id != "" and user_pw != "":
            # 실행버튼 하나도 안눌렀는지 확인
            if follow_check != 0 or like_check != 0 or comment_check != 0:
                # 태그와 개수와 딜레이 공백인지 확인
                if count_value != "하루 100개 이하를 추천합니다" and count_value != ""\
                        and delay_value != "10초 이상(초단위)" and delay_value != ""\
                        and tag_value != "태그나 계정을 입력하세요" and tag_value != "":
                    delay_value = int(delay_value)
                    count_value = int(count_value)

                    insta = Insta()
                    self.list_box.insert(END, "로그인 중")
                    login_success = insta.login(user_id, user_pw, show_window_check)
                    # 로그인 성공 확인
                    if login_success:
                        self.list_box.insert(END, "로그인 성공")
                        insta.search(tag_value)

                        # 태그 모드
                        if 1 <= self.mode_num <= 7:
                            self.list_box.insert(END, "수행 중")
                            do_tag_mode = insta.use_tag_mode(count_value, delay_value, delay_check, comment_value, self.mode_num)
                            self.insert_list_box(do_tag_mode)
                            self.list_box.insert(f"{len(do_tag_mode)}개 수행완료")
                        # 계정 팔로우 모드
                        elif account_follow_mode:
                            self.list_box.insert(END, "팔로우 중")
                            insta.click_follow_button()
                            followed = insta.account_follow(count_value, delay_value, delay_check)
                            self.insert_list_box(followed)
                            self.list_box.insert(f"{len(followed)}개 팔로우 완료")
                        else:
                            insta.close_insta()
                            messagebox.showerror(title="Error", message="계정으로 팔로우모드는 다른 모드와 같이 실행 할 수 없습니다!\n다른 모드"
                                                                        "체크를 해제해주세요!")
                    else:
                        self.list_box.insert(END, "로그인 실패")
                        messagebox.showerror(title="Login Error", message="로그인 중에 문제가 발생했습니다\n아이디나 비밀번호를 다시 한 번 확인해주세요.")
                else:
                    messagebox.showerror(title="Error", message="태그(계정) 또는 개수 또는 딜레이를 입력해주세요!\n"
                                                                "태그(계정), 개수, 딜레이는 필수 값입니다!")
            else:
                messagebox.showerror(title="Error", message="실행 모드를 하나 이상 체크해주세요!")

        else:
            messagebox.showerror(title="Error", message="아이디와 비밀번호를 입력해주세요!")


