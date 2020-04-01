# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from DbManager import DbManager
from Assistant import WatchDiary, WriteDiary, AccountManager, Setup
import arrow
import re
import sys


# 주의: 레이아웃 코드 복붙할때 기존 코드 안날라가게 조심!
###########################################################################
## Class StartMenu
###########################################################################

class StartMenu(wx.Frame):

    def __init__(self, parent, size):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.login_button = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.login_button, 1, wx.ALL | wx.EXPAND, 5)

        self.signup_button = wx.Button(self, wx.ID_ANY, u"회원가입", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.signup_button, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.login_button.Bind(wx.EVT_BUTTON, self.loginButtonClicked)
        self.signup_button.Bind(wx.EVT_BUTTON, self.signUpButtonClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onClose(self, event):
        a = DbManager()
        a.closeDb()
        self.Destroy()
        sys.exit()

    def loginButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = LoginMenu(parent=None, size=frameSize)
        frame1.Show(True)
        self.Show(False)

    def signUpButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = SignUpMenu(parent=None, size=frameSize)
        frame1.Show(True)
        self.Show(False)


###########################################################################
## Class DiaryMainMenu
###########################################################################

class DiaryMainMenu(wx.Frame):

    def __init__(self, parent, size, userId):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.watch_button = wx.Button(self, wx.ID_ANY, u"일기보기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.watch_button, 1, wx.ALL | wx.EXPAND, 5)

        self.write_button = wx.Button(self, wx.ID_ANY, u"일기쓰기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.write_button, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.watch_button.Bind(wx.EVT_BUTTON, self.watchButtonClicked)
        self.write_button.Bind(wx.EVT_BUTTON, self.writeButtonClicked)

        self.DbManager = DbManager()
        self.userId = userId

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onClose(self, event):
        self.DbManager.closeDb()
        self.Destroy()
        sys.exit()

    def watchButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = WatchDiaryMenu(parent=None, size=frameSize, userId=self.userId)
        frame1.Show(True)
        self.Show(False)

    def writeButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = WriteDiaryMenu(parent=None, mode='w', size=frameSize, userId=self.userId)
        frame1.Show(True)
        self.Show(False)


###########################################################################
## Class LoginMenu
###########################################################################

class LoginMenu(wx.Frame):

    def __init__(self, parent, size):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(300, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.go_back_button = wx.Button(self, wx.ID_ANY, u"뒤로가기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.go_back_button, 0, wx.ALL, 5)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        self.id_input_box = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.id_input_box, 0, wx.ALL, 5)

        self.pw_input_box = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        bSizer19.Add(self.pw_input_box, 0, wx.ALL, 5)

        self.m_panel7.SetSizer(bSizer19)
        self.m_panel7.Layout()
        bSizer19.Fit(self.m_panel7)
        bSizer2.Add(self.m_panel7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.login_button = wx.Button(self, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.login_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.go_back_button.Bind(wx.EVT_BUTTON, self.goBackButtonClicked)
        self.pw_input_box.Bind(wx.EVT_TEXT_ENTER, self.pwInputFinished)
        self.login_button.Bind(wx.EVT_BUTTON, self.loginButtonClicked)

        self.DbManager = DbManager()
        self.accountManager = AccountManager()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onClose(self, event):
        self.DbManager.closeDb()
        self.Destroy()
        sys.exit()

    def goBackButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = StartMenu(parent=None, size=frameSize)
        frame1.Show(True)
        self.Show(False)

    def pwInputFinished(self, event):
        self.loginButtonClicked(event=None)

    def loginButtonClicked(self, event):
        id = self.id_input_box.GetValue()
        pw = self.pw_input_box.GetValue()

        pwFollowRule = True
        try:
            if re.findall('[a-zA-Z0-9]+', pw)[0] != pw:
                pwFollowRule = False
        except:
            if len(re.findall('[^a-zA-Z0-9]+', pw)[0]) > 0:
                pwFollowRule = False
            else:
                raise BaseException

        idFollowRule = True
        try:
            if re.findall('[a-zA-Z0-9]+', id)[0] != id:
                idFollowRule = False
        except:
            if len(re.findall('[^a-zA-Z0-9]+', id)[0]) > 0:
                idFollowRule = False
            else:
                raise BaseException

        if pwFollowRule and idFollowRule:
            loginAccepted = self.accountManager.logIn(id, pw)
        else:
            loginAccepted = False

        if loginAccepted:
            if self.IsMaximized():
                frameSize = 'max'
            else:
                frameSize = self.GetSize()
            frame1 = DiaryMainMenu(parent=None, size=frameSize, userId=self.id_input_box.GetValue())
            frame1.Show(True)
            self.Show(False)
        else:
            wx.MessageBox("로그인 실패!")

        return loginAccepted


###########################################################################
## Class SignUpMenu
###########################################################################

class SignUpMenu(wx.Frame):

    def __init__(self, parent, size):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.goBackButton = wx.Button(self.m_panel6, wx.ID_ANY, u"뒤로가기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.goBackButton, 0, wx.ALL, 5)

        gSizer7.Add(bSizer17, 1, wx.EXPAND, 5)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.id_confirm_button = wx.Button(self.m_panel6, wx.ID_ANY, u"ID중복확인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.id_confirm_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer7.Add(bSizer18, 1, wx.EXPAND, 5)

        self.m_panel6.SetSizer(gSizer7)
        self.m_panel6.Layout()
        gSizer7.Fit(self.m_panel6)
        bSizer7.Add(self.m_panel6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.id_input_text = wx.StaticText(self.m_panel5, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.id_input_text.Wrap(-1)

        bSizer13.Add(self.id_input_text, 0, wx.ALL | wx.EXPAND, 5)

        self.id_input_box = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.id_input_box, 0, wx.ALL | wx.EXPAND, 5)

        self.pw_input_text = wx.StaticText(self.m_panel5, wx.ID_ANY, u"비밀번호", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pw_input_text.Wrap(-1)

        bSizer13.Add(self.pw_input_text, 0, wx.ALL | wx.EXPAND, 5)

        self.pw_input_box = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD)
        bSizer13.Add(self.pw_input_box, 0, wx.ALL | wx.EXPAND, 5)

        self.pw_re_input_text = wx.StaticText(self.m_panel5, wx.ID_ANY, u"비밀번호 재입력", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.pw_re_input_text.Wrap(-1)

        bSizer13.Add(self.pw_re_input_text, 0, wx.ALL | wx.EXPAND, 5)

        self.pw_re_input_box = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TE_PASSWORD)
        bSizer13.Add(self.pw_re_input_box, 0, wx.ALL | wx.EXPAND, 5)

        gSizer5.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.pw_check_text = wx.StaticText(self.m_panel5, wx.ID_ANY,
                                           u"id,비밀번호 둘다\n영어 대소문자, \n숫자만 가능\n\n비밀번호는\n10자 이상\n영어,숫자 필수",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.pw_check_text.Wrap(-1)

        bSizer15.Add(self.pw_check_text, 1, wx.ALL | wx.EXPAND, 5)

        self.pw_confirm_img = wx.StaticBitmap(self.m_panel5, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        bSizer15.Add(self.pw_confirm_img, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer15.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer5.Add(bSizer15, 1, wx.EXPAND, 5)

        self.m_panel5.SetSizer(gSizer5)
        self.m_panel5.Layout()
        gSizer5.Fit(self.m_panel5)
        bSizer7.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.re_pw_correct_text = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.re_pw_correct_text.Wrap(-1)

        bSizer7.Add(self.re_pw_correct_text, 0, wx.ALL, 5)

        gSizer2.Add(bSizer7, 1, wx.EXPAND | wx.RIGHT, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.account_repair_question_text = wx.StaticText(self, wx.ID_ANY, u"보안질문", wx.DefaultPosition, wx.DefaultSize,
                                                          0)
        self.account_repair_question_text.Wrap(-1)

        bSizer8.Add(self.account_repair_question_text, 0, wx.ALL | wx.EXPAND, 5)

        account_repair_question_choiceChoices = [u"가장 아끼는 물건은?", u"가장 좋아했던 선생님 성함은?", u"가장 감명깊게 읽은 책은?", u"가장 어려웠던 책은?"]
        self.account_repair_question_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                        account_repair_question_choiceChoices, 0)
        self.account_repair_question_choice.SetSelection(0)
        bSizer8.Add(self.account_repair_question_choice, 0, wx.ALL | wx.EXPAND, 5)

        self.answer_text = wx.StaticText(self, wx.ID_ANY, u"답변", wx.DefaultPosition, wx.DefaultSize, 0)
        self.answer_text.Wrap(-1)

        bSizer8.Add(self.answer_text, 0, wx.ALL | wx.EXPAND, 5)

        self.answer_input_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.answer_input_box, 0, wx.ALL | wx.EXPAND, 5)

        self.sign_up_button = wx.Button(self, wx.ID_ANY, u"회원가입", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.sign_up_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer2.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.goBackButton.Bind(wx.EVT_BUTTON, self.goBackButtonClicked)
        self.id_confirm_button.Bind(wx.EVT_BUTTON, self.idConfirmButtonClicked)
        self.id_input_box.Bind(wx.EVT_TEXT, self.textInputedOnId)
        self.pw_input_box.Bind(wx.EVT_TEXT, self.textInputedOnPw)
        self.pw_re_input_box.Bind(wx.EVT_TEXT, self.textInputedOnRePw)
        self.account_repair_question_choice.Bind(wx.EVT_CHOICE, self.choiced)
        self.sign_up_button.Bind(wx.EVT_BUTTON, self.signUpButtonClicked)

        self.accountManager = AccountManager()
        self.sQuestionNum = 0
        self.dbManager = DbManager()
        self.correctSymbolPng = wx.Image('tick.png', wx.BITMAP_TYPE_ANY)
        self.correctSymbolPng.Rescale(32, 32)
        self.correctSymbolPng = self.correctSymbolPng.ConvertToBitmap()
        self.incorrectSymbolPng = wx.Image('close.png', wx.BITMAP_TYPE_ANY)
        self.incorrectSymbolPng.Rescale(32, 32)
        self.incorrectSymbolPng = self.incorrectSymbolPng.ConvertToBitmap()
        self.pw_confirm_img.SetBitmap(self.incorrectSymbolPng)
        self.idFlag = -1

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def onClose(self, event):
        self.dbManager.closeDb()
        self.Destroy()
        sys.exit()

    def goBackButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = StartMenu(parent=None, size=frameSize)
        frame1.Show(True)
        self.Show(False)

    def idConfirmButtonClicked(self, event):
        allId = self.dbManager.readAllId()
        id = (self.id_input_box.GetValue(),)
        self.idFlag = False
        if not (id in allId):
            self.idFlag = True
        if self.idFlag:
            wx.MessageBox(f"'{id[0]}': 사용가능한 아이디 입니다.")
        else:
            wx.MessageBox(f"'{id[0]}': 사용불가능한 아이디 입니다.")

    def textInputedOnId(self, event):
        self.idFlag = -1

    def textInputedOnPw(self, event):
        pw = self.pw_input_box.GetValue()

        self.pwFollowRule = True
        if len(pw) < 9:
            self.pwFollowRule = False
        elif re.findall('[a-zA-Z0-9]+', pw)[0] != pw:  # re에서 영어, 숫자만 찾기. 만약 다른 문자가 있다면 중간에 끊김 -> 본래 문자열과 달라짐 -> 구별 가능.
            self.pwFollowRule = False
        elif len(re.findall('[a-zA-Z]', pw)) == 0:
            self.pwFollowRule = False
        elif len(re.findall('\d', pw)) == 0:
            self.pwFollowRule = False

        if self.pwFollowRule:
            self.pw_confirm_img.SetBitmap(self.correctSymbolPng)
        else:
            self.pw_confirm_img.SetBitmap(self.incorrectSymbolPng)

    def textInputedOnRePw(self, event):
        self.pwFlag = self.pw_input_box.GetValue() == self.pw_re_input_box.GetValue()
        if self.pwFlag:
            self.re_pw_correct_text.SetLabel("비밀번호가 일치합니다!")
        else:
            self.re_pw_correct_text.SetLabel("비밀번호가 일치하지 않습니다.")

    def choiced(self, event):
        self.sQuestionNum = self.account_repair_question_choice.GetSelection()
        print(self.sQuestionNum)
        return self.sQuestionNum

    def signUpButtonClicked(self, event):
        if self.idFlag == -1:
            wx.MessageBox("아이디 중복확인 해주세요!")
        try:
            if re.findall('[a-zA-Z0-9]+', self.id_input_box.GetValue())[0] != self.id_input_box.GetValue():
                wx.MessageBox("이 아이디는 사용할 수 없습니다(영어 대소문자,숫자로 이루어지지 않음)")
                self.idFlag = False
        except:
            if len(re.findall('[^a-zA-Z0-9]+', self.id_input_box.GetValue())[0]) > 0:
                wx.MessageBox("이 아이디는 사용할 수 없습니다(영어 대소문자,숫자로 이루어지지 않음)")
                self.idFlag = False
            else:
                raise BaseException
        if not (
                self.id_input_box.GetValue() == None and self.pw_input_box.GetValue() == None and self.answer_input_box.GetValue() == None):
            if self.idFlag == True and self.pwFlag == True and self.pwFollowRule == True:
                loginSuccess = self.accountManager.registerUser(self.id_input_box.GetValue(),
                                                                self.pw_input_box.GetValue(), self.sQuestionNum,
                                                                self.answer_input_box.GetValue())
                if loginSuccess:
                    wx.MessageBox(f"회원가입 성공! 아이디는 '{self.id_input_box.GetValue()}'")
                    if self.IsMaximized():
                        frameSize = 'max'
                    else:
                        frameSize = self.GetSize()
                    frame1 = DiaryMainMenu(parent=None, size=frameSize, userId=self.id_input_box.GetValue())
                    frame1.Show(True)
                    self.Show(False)
                else:
                    wx.MessageBox(f"회원가입 실패ㅜㅜ")
        else:
            wx.MessageBox('공란이 있으면 안됨')
        return self.id_input_box.GetValue(), self.pw_input_box.GetValue(), self.sQuestionNum, self.answer_input_box.GetValue()


###########################################################################
## Class WriteDiaryMenu
###########################################################################

class WriteDiaryMenu(wx.Frame):

    def __init__(self, parent, mode, size, userId, diaryContent=None, todayFeel=5, todayThoughts=None):
        if size == 'max':
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            self.Maximize()
        else:
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(size), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.go_back_button = wx.Button(self, wx.ID_ANY, u"뒤로가기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.go_back_button, 0, wx.ALL, 5)

        if mode == "w":
            if diaryContent == None:
                self.diary_input_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.TE_MULTILINE)
            else:
                self.diary_input_box = wx.TextCtrl(self, wx.ID_ANY, u"{0}".format(diaryContent), wx.DefaultPosition,
                                                   wx.DefaultSize, wx.TE_MULTILINE)
        else:
            self.diary_input_box = wx.TextCtrl(self, wx.ID_ANY, u'{0}'.format(diaryContent), wx.DefaultPosition,
                                               wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer7.Add(self.diary_input_box, 1, wx.ALL | wx.EXPAND, 5)

        gSizer3.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.today_feel_text = wx.StaticText(self.m_panel1, wx.ID_ANY, u"오늘 기분1/5", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.today_feel_text.Wrap(-1)

        bSizer9.Add(self.today_feel_text, 0, wx.ALL, 5)
        if mode == 'w':
            self.today_feel_slider = wx.Slider(self.m_panel1, wx.ID_ANY, todayFeel, 1, 5, wx.DefaultPosition,
                                               wx.DefaultSize, wx.SL_HORIZONTAL | wx.SL_SELRANGE | wx.SL_VALUE_LABEL)
            bSizer9.Add(self.today_feel_slider, 0, wx.ALL | wx.EXPAND, 5)
        else:
            self.today_feel_text = wx.StaticText(self.m_panel1, wx.ID_ANY, u"{0}".format(todayFeel), wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.today_feel_text.Wrap(-1)
            bSizer9.Add(self.today_feel_text, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer9)
        self.m_panel1.Layout()
        bSizer9.Fit(self.m_panel1)
        bSizer8.Add(self.m_panel1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.today_thoughts_text = wx.StaticText(self.m_panel2, wx.ID_ANY, u"오늘 생각한것", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.today_thoughts_text.Wrap(-1)

        bSizer10.Add(self.today_thoughts_text, 0, wx.ALL, 5)

        if mode == 'w':
            if todayThoughts == None:
                self.today_thoughts_input_box = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString,
                                                            wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
            else:
                self.today_thoughts_input_box = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"{0}".format(todayThoughts),
                                                            wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        else:
            self.today_thoughts_input_box = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"{0}".format(todayThoughts),
                                                        wx.DefaultPosition, wx.DefaultSize,
                                                        wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer10.Add(self.today_thoughts_input_box, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer10)
        self.m_panel2.Layout()
        bSizer10.Fit(self.m_panel2)
        bSizer8.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        if mode == 'w':
            self.save_diary_button = wx.Button(self, wx.ID_ANY, u"일기 저장", wx.DefaultPosition, wx.DefaultSize, 0)
            bSizer8.Add(self.save_diary_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.save_diary_button.Bind(wx.EVT_BUTTON, self.saveButtonClicked)

        gSizer3.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.go_back_button.Bind(wx.EVT_BUTTON, self.goBackButtonClicked)

        self.dbManager = DbManager()
        self.WriteDiary = WriteDiary()
        self.userId = userId

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onClose(self, event):
        self.dbManager.closeDb()
        self.Destroy()
        sys.exit()

    def goBackButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = DiaryMainMenu(parent=None, size=frameSize, userId=self.userId)
        frame1.Show(True)
        self.Show(False)

    def saveButtonClicked(self, event):
        self.WriteDiary.saveDiaryTxt(arrow.now().date(), self.diary_input_box.GetValue())
        self.WriteDiary.saveTodayThoughtsTxt(arrow.now().date(), self.today_thoughts_input_box.GetValue())
        self.dbManager.saveDiaryInfo(arrow.now().date(), str(arrow.now().time())[:5], self.today_feel_slider.GetValue(),
                                     self.today_thoughts_input_box.GetValue(), self.userId)
        wx.MessageBox("일기 저장 성공!")

        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = DiaryMainMenu(parent=None, size=frameSize, userId=self.userId)
        frame1.Show(True)
        self.Show(False)


###########################################################################
## Class WatchDiaryMenu
###########################################################################

class WatchDiaryMenu(wx.Frame):

    def __init__(self, parent, size, userId):
        if size == 'max':
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            self.Maximize()
        else:
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                              size=wx.Size(size), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.go_back_button = wx.Button(self, wx.ID_ANY, u"뒤로가기", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.go_back_button, 0, wx.ALL, 5)

        self.m_panel81 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer31 = wx.GridBagSizer(0, 0)
        gbSizer31.SetFlexibleDirection(wx.BOTH)
        gbSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.range_text = wx.StaticText(self.m_panel81, wx.ID_ANY, u"범위", wx.DefaultPosition, wx.DefaultSize, 0)
        self.range_text.Wrap(-1)

        gbSizer31.Add(self.range_text, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        range_choiceChoices = [u"전체", u"선택"]
        self.range_choice = wx.Choice(self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      range_choiceChoices, 0)
        self.range_choice.SetSelection(0)
        gbSizer31.Add(self.range_choice, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.feel_text = wx.StaticText(self.m_panel81, wx.ID_ANY, u"기분", wx.DefaultPosition, wx.DefaultSize, 0)
        self.feel_text.Wrap(-1)

        gbSizer31.Add(self.feel_text, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        feel_range_choiceChoices = [u"전체", u"선택"]
        self.feel_range_choice = wx.Choice(self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           feel_range_choiceChoices, 0)
        self.feel_range_choice.SetSelection(0)
        gbSizer31.Add(self.feel_range_choice, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.thoughts_count_text = wx.StaticText(self.m_panel81, wx.ID_ANY, u"생각개수", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        self.thoughts_count_text.Wrap(-1)

        gbSizer31.Add(self.thoughts_count_text, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        feel_range_choice1Choices = [u"전체", u"선택"]
        self.feel_range_choice1 = wx.Choice(self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            feel_range_choice1Choices, 0)
        self.feel_range_choice1.SetSelection(0)
        gbSizer31.Add(self.feel_range_choice1, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.search_button = wx.Button(self.m_panel81, wx.ID_ANY, u"검색", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer31.Add(self.search_button, wx.GBPosition(0, 6), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_panel81.SetSizer(gbSizer31)
        self.m_panel81.Layout()
        gbSizer31.Fit(self.m_panel81)
        bSizer12.Add(self.m_panel81, 0, wx.ALL | wx.EXPAND, 5)

        self.m_scrolledWindow2 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow2.SetScrollRate(5, 5)
        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.starPng = wx.Image('star.png', wx.BITMAP_TYPE_ANY)
        frameSizeX, frameSizeY = self.GetSize()
        self.starPng.Rescale(16, 16)
        self.starPng = self.starPng.ConvertToBitmap()
        del frameSizeX, frameSizeY

        self.DbManager = DbManager()
        self.userId = userId

        diary = self.DbManager.findDiaryWithCondition(startDate='1970-01-01', finishDate='2099-01-01', startFeelRange=1,
                                                      finishFeelRange=5, thoughtsStartRange=0, thoughtsFinishRange=100,
                                                      userId=self.userId)
        for i in range(len(diary)):
            date = diary[i][0]
            time = diary[i][1]
            todayFeel = diary[i][2]
            todayThoughtsCount = diary[i][3]

            diaryPanel = self.makeDiaryPanel(date, time, todayFeel, todayThoughtsCount, len(diary),
                                             self.m_scrolledWindow2)
            bSizer22.Add(diaryPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.m_scrolledWindow2.SetSizer(bSizer22)
        self.m_scrolledWindow2.Layout()
        bSizer22.Fit(self.m_scrolledWindow2)
        bSizer12.Add(self.m_scrolledWindow2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.range_choice.Bind(wx.EVT_CHOICE, self.rangeChoiced)
        self.feel_range_choice.Bind(wx.EVT_CHOICE, self.feelRangeChoiced)
        self.feel_range_choice1.Bind(wx.EVT_CHOICE, self.thoughtsRangeChoiced)
        self.search_button.Bind(wx.EVT_BUTTON, self.searchButtonClicked)
        self.go_back_button.Bind(wx.EVT_BUTTON, self.goBackButtonClicked)

    def __del__(self):
        pass

    def makeDiaryPanel(self, date, time, star, thoughtsCount, diaryCount, m_scrolledWindow2):
        m_panel8 = wx.Panel(m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        date_text = wx.StaticText(m_panel8, wx.ID_ANY, u'{0}'.format(date), wx.DefaultPosition, wx.DefaultSize, 0)
        date_text.Wrap(-1)

        gbSizer3.Add(date_text, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        time_text = wx.StaticText(m_panel8, wx.ID_ANY, u"{0}".format(time), wx.DefaultPosition, wx.DefaultSize, 0)
        time_text.Wrap(-1)

        gbSizer3.Add(time_text, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        thoughts_count = wx.StaticText(m_panel8, wx.ID_ANY, u"{0}".format(thoughtsCount), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        thoughts_count.Wrap(-1)

        gbSizer3.Add(thoughts_count, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        diary_show_button = wx.Button(m_panel8, wx.ID_ANY, u"일기보기", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer3.Add(diary_show_button, wx.GBPosition(0, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        m_panel18 = wx.Panel(m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        for i in range(int(star)):
            star = wx.StaticBitmap(m_panel18, wx.ID_ANY, self.starPng, wx.DefaultPosition, wx.DefaultSize, 0)
            gbSizer4.Add(star, wx.GBPosition(0, i), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_panel18.SetSizer(gbSizer4)
        m_panel18.Layout()
        gbSizer4.Fit(m_panel18)
        gbSizer3.Add(m_panel18, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        m_panel8.SetSizer(gbSizer3)
        m_panel8.Layout()
        gbSizer3.Fit(m_panel8)

        diary_show_button.Bind(wx.EVT_BUTTON, lambda event: self.diaryShowButtonClicked(event, date))
        return m_panel8

    # Virtual event handlers, overide them in your derived class
    def onClose(self, event):
        self.DbManager.closeDb()
        self.Destroy()
        sys.exit()

    def rangeChoiced(self, event):
        event.Skip()

    def feelRangeChoiced(self, event):
        event.Skip()

    def thoughtsRangeChoiced(self, event):
        event.Skip()

    def searchButtonClicked(self, event):
        event.Skip()

    def goBackButtonClicked(self, event):
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        frame1 = DiaryMainMenu(parent=None, size=frameSize, userId=self.userId)
        frame1.Show(True)
        self.Show(False)

    def diaryShowButtonClicked(self, event, date):
        watchDiary = WatchDiary()
        diaryContent = watchDiary.readCorrectDiaryTxt(date)
        todayThoughtsContent = watchDiary.readCorrectTodayThoughtsTxt(date)
        diaryInfo = self.DbManager.readDiaryInfo(date, self.userId)
        if self.IsMaximized():
            frameSize = 'max'
        else:
            frameSize = self.GetSize()
        if date == str(arrow.now().date()):
            frame1 = WriteDiaryMenu(parent=None, mode='w', size=frameSize, userId=self.userId,
                                    diaryContent=diaryContent, todayFeel=diaryInfo[2],
                                    todayThoughts=todayThoughtsContent)
        else:
            frame1 = WriteDiaryMenu(parent=None, mode='r', size=frameSize, userId=self.userId,
                                    diaryContent=diaryContent, todayFeel=diaryInfo[2],
                                    todayThoughts=todayThoughtsContent)
        frame1.Show(True)
        self.Show(False)


if __name__ == "__main__":
    a = Setup()
    app = wx.App()
    frame = StartMenu(parent=None, size=(500, 300))
    frame.Show(True)
    app.MainLoop()
