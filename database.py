import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='',
                                  port=3306,
                                  user='',
                                  password='',
                                  db='',
                                  charset='utf8')

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def db_close(self):
        self.cursor.close()
        self.db.close()

    def execute(self, query, args):
        self.cursor.execute(query, args)

    def executemany(self, query, args):
        self.cursor.executemany(query, args)

    def executeOne(self, query, args=None):
        if args is None:
            args = {}
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args=None):
        if args is None:
            args = {}
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows

    def commit(self):
        self.db.commit()