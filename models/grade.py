from models.model import Model, Relation
from models.subject import Subject


class Grade(Model):
    def __init__(self):
        super().__init__(self)
        self.table = "grades"
        self.fillable = ['subject_id', 'student_id', 'note1', 'note2']
        self.subject = Relation(Subject, Grade, 'subject_id')

    def migrate(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS grades("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "student_id INTEGER NOT NULL,"
                            "subject_id INTEGER NOT NULL,"
                            "note1 REAL,"
                            "note2 REAL,"
                            "created_at DATE,"
                            "FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,"
                            "FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE)")
