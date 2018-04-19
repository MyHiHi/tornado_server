from config import mysql
import pymysql

def singleton(cls,*args,**kwargs):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls];
    return _singleton

@singleton
class DB():
    def __init__(self):
        self.con=None
    def connect(self):
        host=mysql.get('host')
        user=mysql.get("user")
        pwd=mysql.get("pwd")
        dbName=mysql.get("dbName")
        self.con = pymysql.connect(host=host, port=3306, user=user, passwd=pwd, db=dbName)
        return self.con.cursor()
    def save(self,sql):
        cursor=self.connect()
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        self.con.close()
    def find_all(self,sql):
        cursor = self.connect()
        cursor.execute(sql)
        return cursor.fetchall()
    def find_one(self,sql):
        cursor = self.connect()
        cursor.execute(sql)
        return cursor.fetchone()
    def delete(self,sql):
        cursor = self.connect()
        cursor.execute(sql)
        # cursor.execute("delete from students where age = 13 and name = 'ss'")
        self.con.commit()





