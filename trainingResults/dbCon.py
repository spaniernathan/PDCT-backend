import psycopg2
'''
Can be used to connect to local database, and store training metrics.
Columns to fill: 'name' (varChar), data (json), hyperparameters (json), comments (text)
'''
class PGCON:
    def __init__(self):
        self.pgSql = None

    def connect(self):
        self.pgSql = psycopg2.connect(user="californium",
                                  password="cal1forniumPDCT",
                                  host="192.168.0.18",
                                  port="5432",
                                  database="postgres")

    def close(self):
        self.pgSql.close()

    def fetchAll(self, sql):
        self.connect()
        cur = self.pgSql.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        self.close()
        return rows
    
    def insertRow(self, sql):
        self.connect()
        cur = self.pgSql.cursor()
        cur.execute(sql)
        self.pgSql.commit()
        return cur.rowcount
