import pytest
from pathlib import Path

import sqlite3
from pathlib import Path


# Path to the SQLite database
def db_path():
    return Path(__file__).resolve().parents[1] / "python-package" / "employee_events" / "employee_events.db"


def test_db_exists():
    assert db_path().exists()


def test_employee_table_exists():
    conn = sqlite3.connect(db_path())
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='employee';"
    )
    result = cursor.fetchone()
    conn.close()
    assert result is not None


def test_team_table_exists():
    conn = sqlite3.connect(db_path())
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='team';"
    )
    result = cursor.fetchone()
    conn.close()
    assert result is not None


def test_employee_events_table_exists():
    conn = sqlite3.connect(db_path())
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='employee_events';"
    )
    result = cursor.fetchone()
    conn.close()
    assert result is not None
