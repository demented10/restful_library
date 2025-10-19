from pydantic import BaseModel
from datetime import date
from typing import List

class ReportRow(BaseModel):
    reader_name: str
    book_title: str
    borrow_date: date
    due_date: date
    is_overdue: bool

class Report(BaseModel):
    report_date: date
    rows: List[ReportRow]