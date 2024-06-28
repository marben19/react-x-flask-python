import json

class Employees:
    def __init__(self, content, sql):
        self.content = content
        self.sql = sql

    def show_employees(self):
        self.sql.execute('SELECT * FROM tbl_employees')
        users = self.sql.fetchall()
        return json.dumps( users )
