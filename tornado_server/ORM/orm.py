import tornado.web
from db import DB
class ORM():

    def save(self):
        table_name = (self.__class__.__name__).lower().split(".")[0]
        fs = fe="("
        for field in self.__dict__:
            fs +=(field+",")
            if isinstance(self.__dict__.get(field),str):
                fe+=("'"+self.__dict__.get(field)+"'"+",")
            else:
                fe+=(str(self.__dict__.get(field))+",")
        fs=fs[:len(fs)-1]+")"
        fe=fe[:len(fe)-1]+")"
        sql="insert into "+table_name+" "+fs+" values "+fe;
        db=DB()
        db.save(sql)

    def delete(self):
        table_name = (self.__class__.__name__).lower().split(".")[0]
        db = DB()
        pro_list = [name for name in self.__dict__]
        name  = self.__dict__[pro_list[1]]
        age = self.__dict__[pro_list[0]]
        sql = "delete from " + table_name + " where " + pro_list[0] + " = " + str(age) + " and " + pro_list[
            1] + " = '" + name+"'";
        print sql
    def update(self):
        pass
    def find_one(self,name,age):
        table_name = (self.__class__.__name__).lower().split(".")[0]
        db=DB()
        pro_list = [ name for name in self.__dict__]
        sql="select * from "+table_name+" where "+pro_list[0]+" = "+str(age)+" and "+pro_list[1]+" = "+name;
        print sql
        return db.find_one(sql)

    def find_all(self):
        table_name = (self.__class__.__name__).lower().split(".")[0]
        db=DB()
        sql="select * from "+table_name
        return  db.find_all(sql)
    def filter(self):
        pass