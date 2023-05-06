import sqlite3
from datetime import datetime


class Model:
    def __init__(self, this):
        self.conn = sqlite3.connect('etudiants.sqlite')
        self.cursor = self.conn.cursor()
        this.migrate()
        self.this = this

    def create(self, data):
        data['created_at'] = datetime.now().strftime("%Y-%m-%d")
        columns = ','.join(data.keys())
        values = ', '.join(['?' for _ in range(len(data.keys()))])
        sql = f"INSERT INTO {self.this.table} ({columns}) VALUES ({values})"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()

    def select(self, *columns, order_by=None, limit=None):
        columns_str = ", ".join(columns) if columns else "*"
        sql = f"SELECT {columns_str} FROM {self.this.table}"
        if order_by:
            sql += f" ORDER BY {order_by}"
        if limit:
            sql += f" LIMIT {limit}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        columns = [col[0] for col in self.cursor.description]
        results = []
        for row in rows:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col] = row[i]
            results.append(row_dict)
        return results

    def where(self, **conditions):
        conditions_str = " AND ".join([f"{key}='{value}'" for key, value in conditions.items()])
        sql = f"SELECT * FROM {self.this.table} WHERE {conditions_str}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [self.this(*row) for row in rows]

    def get(self, pk=None):
        if pk is not None:
            sql = f"SELECT * FROM {self.this.table} WHERE id = ?"
            self.cursor.execute(sql, (pk,))
        else:
            sql = f"SELECT * FROM {self.this.table}"
            self.cursor.execute(sql)

        result = self.cursor.fetchall()
        columns = [col[0] for col in self.cursor.description]
        results = []
        for row in result:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col] = row[i]
            results.append(row_dict)
        return results

    def update(self, pk, data):
        columns = ' '.join(data.keys())
        values = ', '.join(['?' for _ in range(len(data.values()))])
        sql = f"UPDATE {self.this.table} SET {columns} = ({values}) WHERE id = ?"
        self.cursor.execute(sql, tuple(data.values()) + (pk,))
        self.conn.commit()

    def delete(self):
        sql = f"DELETE FROM {self.this.table} WHERE id = ?"
        self.cursor.execute(sql, (self.this.id,))
        self.conn.commit()


class Relation:
    def __init__(self, model, related_model, foreign_key):
        self.model = model
        self.related_model = related_model
        self.foreign_key = foreign_key

    def __get__(self, instance, owner):
        if instance is None:
            return self
        related_instances = self.related_model.select().where(
            getattr(self.related_model, self.foreign_key) == instance.id
        )
        setattr(instance, self.model.__name__.lower(), related_instances)
        return related_instances
