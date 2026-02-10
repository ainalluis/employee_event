from .sql_execution import SQLExecutionMixin


class QueryBase(SQLExecutionMixin):
    """
    Base class for shared SQL queries.
    """

    def __init__(self, db_path):
        self.db_path = db_path

    def get_all_employees(self):
        """
        Return all employees.
        """
        query = """
        SELECT employee_id, first_name, last_name
        FROM employee;
        """
        return self.execute_query(query)

    def get_all_teams(self):
        """
        Return all teams.
        """
        query = """
        SELECT team_id
        FROM team;
        """
        return self.execute_query(query)
