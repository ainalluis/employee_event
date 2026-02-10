from employee_events import Employee
from report.utils import load_model
from report.base_components.base_component import BaseComponent
from report.base_components.data_table import DataTable
from report.base_components.matplotlib_viz import MatplotlibViz
from report.combined_components.combined_component import CombinedComponent
from fasthtml.common import Div, P, FastHTML
from uvicorn import run

import pandas as pd
import matplotlib.pyplot as plt


class ModelContext:
    def __init__(self, ml_model, db_path):
        self.ml_model = ml_model
        self.db_path = db_path
        self.name = "employee_dashboard"


model = ModelContext(
    ml_model=load_model(),
    db_path="python-package/employee_events/employee_events.db"
)


class EmployeeProductivity(BaseComponent):
    def build_component(self, entity_id, model):
        employee = Employee(entity_id, model.db_path)
        productivity = employee.productivity()

        return Div(
            P(f"Employee Productivity: {productivity}")
        )


class EmployeeProductivityTable(DataTable):
    columns = ["employee_id", "productivity"]

    def component_data(self, entity_id, model):
        employee = Employee(entity_id, model.db_path)
        productivity = employee.productivity()

        return pd.DataFrame([{
            "employee_id": entity_id,
            "productivity": productivity
        }])


class EmployeeProductivityChart(MatplotlibViz):
    def build_component(self, entity_id, model):
        employee = Employee(entity_id, model.db_path)

        # event_history devuelve lista de tuplas
        data = employee.event_history()

        df = pd.DataFrame(
            data,
            columns=["event_date", "positive_events", "negative_events"]
        )

        df["productivity"] = df["positive_events"] - df["negative_events"]

        fig, ax = plt.subplots()
        ax.plot(df["event_date"], df["productivity"])
        ax.set_title("Employee Productivity Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Productivity")

        return fig


class EmployeeDashboard(CombinedComponent):
    children = [
        EmployeeProductivity(),
        EmployeeProductivityTable(),
        EmployeeProductivityChart()
    ]

app = FastHTML()


@app.get("/employee/{employee_id}")
def employee_view(employee_id: int):
    page = EmployeeDashboard()
    components = page.call_children(employee_id, model)
    return page.outer_div(components, {"class": "container"})


if __name__ == "__main__":
    run(
        "report.dashboard:app",
        host="0.0.0.0",
        port=5001,
        reload=False
    )
