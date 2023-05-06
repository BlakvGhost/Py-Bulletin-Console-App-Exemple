from datetime import datetime
from models.model import Model


class Subject(Model):
    def __init__(self):
        super().__init__(self)
        self.table = "subjects"
        self.fillable = ['name']

    def migrate(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subjects("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "name TEXT NOT NULL,"
                            "created_at DATE)")

