import pymysql as pymysql

from model.project import Project
import pymysql.cursors

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self. password = password
        self.connection = pymysql.connect(host=host, database = name  , user = user, password=password, autocommit = True)

    def get_project_list(self):
        project_list = []
        status_list = {
            10: "development",
            30: "release",
            50: "stable",
            70: "obsolete",
        }
        view_state_list = {
            10: "public",
            50: "private"
        }
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name, status, view_state, description FROM mantis_project_table")
            for row in cursor:
                (id, name, status_num, view_state_num, description) = row
                project_list.append(Project(id=id, name=name, status=status_list[status_num],
                                            view_state=view_state_list[view_state_num], description=description))
        finally:
            cursor.close()
        return project_list

    def destroy(self):
        self.connection.close()
