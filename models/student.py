from datetime import datetime

from models.model import Model, Relation
from models.grade import Grade


class Student(Model):
    def __init__(self):
        super().__init__(self)
        self.table = "students"
        self.fillable = ['first_name', 'last_name', 'uniqId', 'gender', 'birthdate', 'created_at']
        self.grades = Relation(Grade, Student, 'student_id')

    def generate_uniqId(self):
        last_uniqId = self.select('uniqId', order_by='uniqId DESC', limit=1)
        new_uniqId = int(last_uniqId[0]['uniqId']) + 1 if last_uniqId else 1
        return str(new_uniqId).zfill(8)

    def migrate(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "first_name TEXT NOT NULL,"
                            "last_name TEXT NOT NULL,"
                            "uniqId TEXT NULL,"
                            "gender TEXT NULL,"
                            "birthdate DATE,"
                            "created_at DATE)")
