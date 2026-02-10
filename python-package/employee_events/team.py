from .query_base import QueryBase


class Team(QueryBase):
    """
    Class for querying team-level data.
    """

    def __init__(self, team_id, db_path):
        super().__init__(db_path)
        self.team_id = team_id

    def average_productivity(self):
        """
        Calculate average productivity for the team.
        """
        query = """
        SELECT
            AVG(positive_events - negative_events)
        FROM employee_events
        WHERE team_id = ?;
        """
        result = self.execute_query(query, (self.team_id,))
        return result[0][0]

    def team_events(self):
        """
        Return aggregated events per employee for the team.
        """
        query = """
        SELECT
            employee_id,
            SUM(positive_events),
            SUM(negative_events)
        FROM employee_events
        WHERE team_id = ?
        GROUP BY employee_id;
        """
        return self.execute_query(query, (self.team_id,))
