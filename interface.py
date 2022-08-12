from tkinter import *
from tkinter import ttk


class Interface:

    def __init__(self):
        self.window = Tk()
        self.window.title("instagram bot ver 1.0")
        self.window.geometry("620x460")
        self.insta_img = PhotoImage(file="image/insta_color.png")
        self.window.iconbitmap("image/insta_color.ico")

        # 상단
        self.top_frame = Frame(width=620, height=60, relief="raised", borderwidth=1, bg="white")
        self.top_label = Label(self.top_frame, text="Instagram", font=("Ebrima", 24, "bold"), fg="#E1306C", bg="white")
        self.top_label.place(x=245, y=0)
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
        self.pw_box = Entry(self.login_frame, width=20)
        self.pw_box.place(x=55, y=43)
            # login button
        self.login_button = Button(self.login_frame, text="login", width=8, height=3)
        self.login_button.place(x=205, y=10)
        self.login_frame.place(x=25, y=70)

        # 출력
        self.print_frame = Frame()
            # scroll
        self.list_box_scroll = Scrollbar(self.print_frame)
        self.list_box_scroll.pack(side="right", fill="y")
            # print_box
        self.list_box = Listbox(self.print_frame, width=30, height=23, yscrollcommand=self.list_box_scroll.set)
        self.list_box.pack(side="left")
        self.list_box_scroll.config(command=self.list_box.yview)
        self.print_frame.place(x=360, y=77)

        # 설정
        self.setting_frame = LabelFrame(text="setting", relief="raised", borderwidth=1, padx=10, pady=10)
            # follow
        self.follow_check = Checkbutton(self.setting_frame, text="팔로우")
        self.follow_check.grid(row=0, column=0, pady=5)
        self.follow_mode = ["태그로 팔로우", "계정으로 팔로우"]
        self.follow_combo = ttk.Combobox(self.setting_frame, width=15, values=self.follow_mode)
        self.follow_combo.current(0)     # 기본 값
        self.follow_combo.grid(row=0, column=1, sticky="w")

            # like
        self.like_check = Checkbutton(self.setting_frame, text="좋아요")
        self.like_check.grid(row=1, column=0, pady=5)

            # tag
        self.tag_entry = Entry(self.setting_frame, width=20, fg="gray")
        self.tag_entry.insert(END, "태그나 계정을 입력하세요")
        self.tag_entry.grid(row=1, column=1, sticky="w")
        self.tag_entry.bind('<Button-1>', self.tag_clear)       # 클릭하면 지워짐

            # comment
        self.comment_check = Checkbutton(self.setting_frame, text="댓글   ")
        self.comment_check.grid(row=2, column=0)
        self.comment_entry = Text(self.setting_frame, width=30, height=5, fg="gray")
        self.comment_entry.insert(END, "댓글 내용을 입력하세요")
        self.comment_entry.bind('<Button-1>', self.comment_clear)
        self.comment_entry.grid(row=2, column=1, rowspan=5, pady=15)

            # count
        self.count_label = Label(self.setting_frame, text="개수")
        self.count_label.grid(row=7, column=0)
        self.count_entry = Entry(self.setting_frame, width=24, fg="gray")
        self.count_entry.insert(0, "하루 100개 이하를 추천합니다")
        self.count_entry.bind('<Button-1>', self.count_clear)
        self.count_entry.grid(row=7, column=1, sticky="w", pady=5)

            # delay
        self.delay_label = Label(self.setting_frame, text="  딜레이")
        self.delay_label.grid(row=8, column=0)
        self.delay_entry = Entry(self.setting_frame, width=13, fg="gray")
        self.delay_entry.insert(0, "초단위로 입력")
        self.delay_entry.bind('<Button-1>', self.delay_clear)
        self.delay_entry.grid(row=8, column=1, sticky="w")

            # delay mode
        self.delay_safe_mode = Checkbutton(self.setting_frame, text="봇감지 회피")
        self.delay_safe_mode.grid(row=8, column=1, sticky="e")

        self.setting_frame.place(x=25, y=190)

        self.window.mainloop()

    def tag_clear(self, event):     # 매개변수 event 안써주면 안됨
        self.tag_entry.delete(0, END)
        self.tag_entry.config(fg="black")

    def comment_clear(self, event):
        self.comment_entry.delete(0.0, END)
        self.comment_entry.config(fg="black")

    def count_clear(self, event):
        self.count_entry.delete(0, END)
        self.count_entry.config(fg="black")

    def delay_clear(self, event):
        self.delay_entry.delete(0, END)
        self.delay_entry.config(fg="black")

    def follow_mode(self):
        if self.follow_combo.get() == self.follow_mode[0]:
            pass

    def get_id(self):
        return self.id_box.get()

    def get_pw(self):
        return  self.pw_box.get()

    def click_login(self):
        id = self.get_id()
        pw = self.get_pw()