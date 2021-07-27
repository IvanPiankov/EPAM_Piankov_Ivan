"""
Task
====
Write a wrapper class TableData for database table, that when initialized with database name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')
then
 -  `len(presidents)` will give current amount of rows in presidents table in database
 -  `presidents['Yeltsin']` should return single data row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president with same name exists in table
 -  object implements iteration protocol. i.e. you could use it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data. If data in table changed after you created collection instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always necessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.
"""


import os
import sqlite3


class TableData:
    """
    Wrapper class TableData for database table,
    that when initialized with database name and table acts as collection object (implements Collection protocol)
    """

    def __init__(self, database_name, table_name):
        self.database_name = self._check_path_to_db(database_name)
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self._check_table_in_db()
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def _check_path_to_db(self, database_name):
        """
        Function check exist database or not
        :param database_name: name_data_base
        :return: path to data_base
        """
        file_path = os.path.join(os.path.dirname(__file__), database_name)
        if os.path.isfile(file_path):
            return file_path
        else:
            raise FileNotFoundError

    def _check_table_in_db(self):
        """
        Function check exist table in database or not
        :return: error if table not exist
        """
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'"
        )
        if cursor.fetchone() is None:
            raise sqlite3.DatabaseError("No such table")

    def __del__(self):
        if hasattr(self, "conn"):
            self.conn.close()

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name}")
        return self.cursor.fetchone()[0]

    def _check_element_in_table(self, item):
        """
        Function extract element from table
        :param item: name
        :return: result of requests from table
        """
        data = self.cursor.execute(
            f"SELECT * FROM '{self.table_name}' WHERE name='{item}'"
        )
        return data.fetchone()

    def __getitem__(self, item):
        element = self._check_element_in_table(item)
        if element is None:
            raise KeyError(item)
        return dict(element)

    def __contains__(self, item):
        return bool(self._check_element_in_table(item))

    def __iter__(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self

    def __next__(self):
        str_pr = self.cursor.fetchone()
        if not str_pr:
            raise StopIteration
        else:
            return str_pr
