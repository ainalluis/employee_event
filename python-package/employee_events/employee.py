from .query_base import QueryBase


class Employee(QueryBase):
    """
    Class for querying employee-level data.
    """

    def __init__(self, employee_id, db_path):
        super().__init__(db_path)
        self.employee_id = employee_id

    def productivity(self):
        """
        Calculate employee productivity as
        total positive events minus total negative events.
        """
        query = """
        SELECT
            SUM(positive_events),
            SUM(negative_events)
        FROM employee_events
        WHERE employee_id = ?;
        """
        result = self.execute_query(query, (self.employee_id,))

        total_positive, total_negative = result[0]
        return total_positive - total_negative

    def event_history(self):
        """
        Return the event history for the employee.
        """
        query = """
        SELECT
            event_date,
            positive_events,
            negative_events
        FROM employee_events
        WHERE employee_id = ?
        ORDER BY event_date;
        """
        return self.execute_query(query, (self.employee_id,))
