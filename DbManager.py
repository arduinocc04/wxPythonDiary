import sqlite3
import arrow
import os

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.expanduser('~'), 'documents', 'Diary', 'Diary.db'))
        self.c = self.conn.cursor()

    def saveDiaryInfo(self, date, time, todayFeel, todayThoughtsCount, writer):
        sql = f'INSERT INTO Diary (date, time, todayFeel, TodayThoughtsCount, Writer) VALUES ("{date}","{time}", {todayFeel}, "{todayThoughtsCount}", "{writer}")'
        try:
            self.c.execute(sql)
        except:
            self.deleteDiaryInfo(date)
            self.c.execute(sql)
        self.conn.commit()
        
    def readDiaryInfo(self, date, userId):
        sql = f'SELECT * FROM Diary WHERE date = "{date}" and Writer = "{userId}"'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchone()

    def deleteDiaryInfo(self, date):
        sql = f'DELETE FROM Diary WHERE date = "{date}"'
        self.c.execute(sql)
        self.conn.commit()

    def closeDb(self):
        self.conn.commit()
        self.c.close()
        self.conn.close()
    
    def saveUserInfo(self, id, pw, sQuestionNum, answer):
        sql = 'INSERT INTO User (ID, PW, sQuestionNum, answer) VALUES ("{0}","{1}", {2}, "{3}")'.format(id, pw, sQuestionNum, answer)
        try:
           self.c.execute(sql)
        except:
            print("이 계정은 이미 있습니다.")
            return -1
        self.conn.commit()
        return 0

    def readAllId(self):
        sql = f'SELECT ID FROM User'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchall()

    def findDiaryWithCondition(self, startDate, finishDate, startFeelRange, finishFeelRange, thoughtsStartRange, thoughtsFinishRange, userId):
        sql = f'SELECT * FROM Diary WHERE Writer = "{userId}" and todayFeel >={startFeelRange} and todayFeel<={finishFeelRange} and TodayThoughtsCount>={thoughtsStartRange} and TodayThoughtsCount<={thoughtsFinishRange} '#and CAST(strftime("%s", Date) AS integer )>=CAST(strftime("%s", {startDate}) AS integer ) and CAST(strftime("%s", Date) AS integer )<=CAST(strftime("%s", {finishDate}) AS integer )'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchall()

    def readUserPw(self, id):
        sql = f'SELECT PW FROM User WHERE ID = "{id}"'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchone()

    def readUsersQuestionNum(self, id):
        sql = f'SELECT sQuestionNum FROM User WHERE ID = "{id}"'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchone()

    def readUserAnswer(self, id):
        sql = f'SELECT answer FROM User WHERE ID = "{id}"'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchone()

    def deleteUserInfo(self, id):
        sql = f'DELETE FROM User WHERE ID = "{id}"'
        self.c.execute(sql)
        self.conn.commit()

    def readUserIdByQA(self, sQuestionNum, answer):#sQuestionNum이랑 answer로 id찾는 함수
        sql = f'SELECT id FROM User WHERE answer = "{answer}" AND sQuestionNum = "{sQuestionNum}"'
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchone()
        
    
    def updatePw(self, id, newPw):
        sql = f'UPDATE Diary SET PW = "{newPw}" WHERE ID = "{id}"'
        self.c.execute(sql)
        self.conn.commit()
    
        
if __name__ == "__main__":
    #TestCase
    a = DbManager()
    a.saveDiaryInfo(arrow.now().date(), str(arrow.now().time())[:5], 1, 4)    
    print(a.readDiaryInfo(arrow.now().date()))
    a.saveUserInfo('qwerty', 'qwertyuiop1', 1, 'qwerty')
    print(a.readAllID())
    print(a.readUserPw('qwerty'))
    print(a.readUsersQuestionNum('qwerty'))
    print(a.readUserAnswer('qwerty'))
    '''
    for i in range(400):
        a.deleteDiaryInfo(str(i))
        a.deleteUserInfo(str(i))
    
    for i in range(400):
        a.saveDiaryInfo(str(i), str(i), i, i)
        a.saveUserInfo(str(i), str(i), i, str(i))
    '''
    a.closeDb()
    #TestCase