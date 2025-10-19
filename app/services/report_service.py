from datetime import date, timedelta
from typing import List, Generator
import csv
import openpyxl
from io import StringIO, BytesIO

from app.domain.repositories.borrowing_repository import BorrowingRepository
from app.domain.repositories.book_repository import BookRepository
from app.domain.repositories.reader_repository import ReaderRepository

class ReportService:
    def __init__(
        self,
        borrowing_repository: BorrowingRepository,
        book_repository: BookRepository,
        reader_repository: ReaderRepository
    ):
        self.borrowing_repository = borrowing_repository
        self.book_repository = book_repository
        self.reader_repository = reader_repository

    def generate_report_data(self, report_date: date) -> Generator[dict, None, None]:
        """Генератор для построчной обработки данных отчета"""
        borrowings = self.borrowing_repository.get_all()

        for borrowing in borrowings:
            book = self.book_repository.get_by_id(borrowing.book_id)
            reader = self.reader_repository.get_by_id(borrowing.reader_id)

            if book and reader:
                due_date = borrowing.borrow_date + timedelta(days=20)
                is_overdue = report_date > due_date

                yield {
                    "reader_name": reader.full_name,
                    "book_title": book.title,
                    "borrow_date": borrowing.borrow_date,
                    "due_date": due_date,
                    "is_overdue": is_overdue
                }

    def generate_csv_report(self, report_date: date) -> StringIO:
        data_generator = self.generate_report_data(report_date)
        output = StringIO()
        writer = csv.writer(output)

        # Заголовки
        writer.writerow(["Reader Name", "Book Title", "Borrow Date", "Due Date", "Is Overdue"])

        # Используем генератор для построчной записи
        for row in data_generator:
            writer.writerow([
                row["reader_name"],
                row["book_title"],
                row["borrow_date"].isoformat(),
                row["due_date"].isoformat(),
                "Yes" if row["is_overdue"] else "No"
            ])

        output.seek(0)
        return output

    def generate_excel_report(self, report_date: date) -> BytesIO:
        data_generator = self.generate_report_data(report_date)
        output = BytesIO()

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Library Report"

        # Заголовки
        sheet.append(["Reader Name", "Book Title", "Borrow Date", "Due Date", "Is Overdue"])

        # Используем генератор для построчной записи
        for row in data_generator:
            sheet.append([
                row["reader_name"],
                row["book_title"],
                row["borrow_date"],
                row["due_date"],
                "Yes" if row["is_overdue"] else "No"
            ])

        workbook.save(output)
        output.seek(0)
        return output