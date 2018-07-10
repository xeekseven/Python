import os
import sqlite3

class SQLite3(object):
    def __init__(self,connectStr):
        self.conn = sqlite3.connect(connectStr)
        
    
    def execute(self,sqlText):
        if self.conn is not None:
            cur = self.conn.cursor()
            return cur.execute(sqlText)

    def commit(self):
        self.conn.commit()

    def executeSelect(self,sqlText):
        if self.conn is not None:
            cur = self.conn.cursor()
            return cur.execute(sqlText)

if __name__ == '__main__':
    boolen = False
    if not os.path.exists('poiid.db'):
        boolen = True
    SqlHelper = SQLite3('poiid.db')
    if boolen:
        SqlHelper.execute('create table poiid_info( poiid nvarchar(50),regionPts Text )')
    # #Add
    # SqlHelper.execute('insert into ip values("127.0.0.1")')
    # SqlHelper.commit()
    # #update
    # SqlHelper.execute('update ip set ipaddress = "192.168.0.1" where ipaddress ="127.0.0.1"')
    # SqlHelper.commit()
    # #select
    # resultList =  SqlHelper.execute('select * from ip')

    # for row in resultList:
    #     print(row[0])
    # #delete
    # SqlHelper.execute('delete from ip where ipaddress = "192.168.0.1"')
    # SqlHelper.commit()
    
