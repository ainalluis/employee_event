import sqlite3


class SQLExecutionMixin:
    """
    Mixin class for executing SQL queries against the employee_events database.
    """

    def execute_query(self, query, params=None):
        """
        Execute a SQL query and return the results.

        Parameters
        ----------
        query : str
            SQL query to execute
        params : tuple, optional
            Parameters to pass to the SQL query

        Returns
        -------
        list
            Query results
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        results = cursor.fetchall()
        conn.close()
        return results
