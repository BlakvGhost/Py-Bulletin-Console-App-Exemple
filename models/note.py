from datetime import datetime
from models.model import Model, Relation
from models.student import Student
from models.grade import Grade


class Note(Model):
    def __init__(self):
        super().__init__(self)
        self.table = "notes"
        self.fillable = ['student_id', 'grade_id', 'value', 'date']

        self.student = Relation(Student, Note, foreign_key="student_id")

        self.grade = Relation(Grade, Note, foreign_key="grade_id")

    def migrate(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "student_id INTEGER NOT NULL,"
                            "grade_id INTEGER NOT NULL,"
                            "value REAL NOT NULL,"
                            "date DATE NOT NULL,"
                            "created_at DATE,"
                            "FOREIGN KEY (student_id) REFERENCES students(id),"
                            "FOREIGN KEY (grade_id) REFERENCES grades(id))")

    def create(self, data):
        data['date'] = datetime.now().strftime("%Y-%m-%d")
        return super().create(data)
