from DbManager import DbManager 
import os
import arrow
import hashlib
import sqlite3

class WatchDiary:
    def readCorrectDiaryTxt(self, date):
        directory = os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'DiaryStorage', str(date) + '.txt')
        if os.path.isfile(directory):   
            with open(directory, 'r') as f:
                return f.read()
        else:
            return -1
    def readCorrectTodayThoughtsTxt(self, date):
        directory = os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'TodayThoughtsStorage', str(date) + '.txt')
        if os.path.isfile(directory):
            with open(directory, 'r') as f:
                return f.read()
        else:
            return -1
        

class WriteDiary:
    def saveDiaryTxt(self, date, content):
        directory = os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'DiaryStorage', str(date) + '.txt')
        with open(directory, 'w+t') as f:
            f.write(content)
        return f.closed
    def saveTodayThoughtsTxt(self, date,content):
        directory = os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'TodayThoughtsStorage', str(date) + '.txt')
        with open(directory, 'w+t') as f:
            f.write(content)
        return f.closed

class AccountManager:
    def __init__(self):
        self.DbManager = DbManager()

    def makeHash(self, inputText):
        inputText = inputText.encode()
        hashObject = hashlib.sha256()
        hashObject.update(inputText)
        hexDig = hashObject.hexdigest()
        return hexDig

    def logIn(self, id, pw):

        hexDig = self.makeHash(pw)
        userPw = self.DbManager.readUserPw(id)

        if userPw == (hexDig,): #userPw가 튜플임.
            return True
        else: 
            return False

    def registerUser(self, id, pw, sQuestionNum, answer):
        pw = self.makeHash(pw)
        
        answer = self.makeHash(answer)
        self.DbManager.saveUserInfo(id = id, pw = pw, sQuestionNum = sQuestionNum, answer = answer)
        return True

    def deleteId(self, id):
        self.DbManager.deleteUserInfo(id)

    def findId(self, sQuestionNum, answer):
        answer = self.makeHash(answer)

        id = self.DbManager.readUserIdByQA(sQuestionNum, answer) 
        if len(id) == 1:
            id = id[0]
        else:
            return -1
        return id
        

    def resetPw(self, id):
        newPw = 'aXeYCQV'
        newPw = newPw.encode()
        hashObject = hashlib.sha256()
        hashObject.update(newPw)
        hexDig = hashObject.hexdigest()
        newPw = hexDig

        self.DbManager.updatePw(id, newPw)

class Setup:
    def __init__(self):
        if os.path.isdir(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'DiaryStorage')):
            pass
        else:
            os.makedirs(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'DiaryStorage'))
        
        if os.path.isdir(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'TodayThoughtsStorage')):
            pass
        else:
            os.makedirs(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'TodayThoughtsStorage'))

        if os.path.isfile(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'Diary.db')):
            pass
        else:
            conn = sqlite3.connect(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'Diary.db'))
            c = conn.cursor()
            c.execute('''CREATE TABLE "Diary" ("Date"
                TEXT NOT NULL,"Time"
                TEXT NOT NULL,"todayFeel"
                INTEGER NOT NULL,"TodayThoughtsCount"
                TEXT,"Writer"
                TEXT NOT NULL,PRIMARY KEY("Date"));''')
            c.execute('''CREATE TABLE "User" (
    	        "ID"	TEXT NOT NULL UNIQUE,
	            "PW"	TEXT NOT NULL,
	            "sQuestionNum"	INTEGER NOT NULL,
	            "answer"	TEXT NOT NULL,
        	    PRIMARY KEY("ID"));''')

if __name__ == "__main__":
    #일기 저장 버튼 누르면 일기는 txt파일로, 나머지는 db에 저장
    #일기보기 누르면 DB로 정렬하고 txt파일 따로 읽기
    #if click view diary Button-> readCorrectDiaryTxt(DbManager.Read(date))
    z = Setup()
    a = WatchDiary()
    b = WriteDiary()
    c = AccountManager()
    d = c.findId(3,'qwerty')
    print(d)
    c.registerUser('asdfgg', 'asdfgzxdcvz1', 3, 'a')
    b.saveDiaryTxt(arrow.now().date(), input("일기입력"))
    f = a.readCorrectDiaryTxt(arrow.now().date())
    print(f)