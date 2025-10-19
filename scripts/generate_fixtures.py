import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from datetime import date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.infrastructure.database.models import PublisherModel, BookModel, ReaderModel, BorrowingModel

def generate_fixtures():
    # Используем настройки из конфигурации
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        # Очистка таблиц (осторожно - удаляет все данные!)
        print("Cleaning existing data...")
        db.query(BorrowingModel).delete()
        db.query(BookModel).delete()
        db.query(PublisherModel).delete()
        db.query(ReaderModel).delete()
        db.commit()

        # Издательства
        print("Creating publishers...")
        publishers = [
            PublisherModel(name="Эксмо", city="Москва"),
            PublisherModel(name="Питер", city="Санкт-Петербург"),
            PublisherModel(name="Дрофа", city="Москва"),
        ]
        db.add_all(publishers)
        db.commit()

        # Книги
        print("Creating books...")
        books = [
            BookModel(cipher="ISBN-001", title="Война и мир", first_author="Лев Толстой", publication_year=2010, price=500.0, copies_available=3, publisher_id=1),
            BookModel(cipher="ISBN-002", title="Преступление и наказание", first_author="Федор Достоевский", publication_year=2015, price=450.0, copies_available=2, publisher_id=1),
            BookModel(cipher="ISBN-003", title="Мастер и Маргарита", first_author="Михаил Булгаков", publication_year=2012, price=400.0, copies_available=1, publisher_id=2),
            BookModel(cipher="ISBN-004", title="1984", first_author="Джордж Оруэлл", publication_year=2018, price=350.0, copies_available=4, publisher_id=3),
        ]
        db.add_all(books)
        db.commit()

        # Читатели
        print("Creating readers...")
        readers = [
            ReaderModel(full_name="Иванов Иван Иванович", address="ул. Ленина, д. 1", phone="+79123456789"),
            ReaderModel(full_name="Петров Петр Петрович", address="ул. Пушкина, д. 2", phone="+79123456780"),
            ReaderModel(full_name="Сидорова Мария Ивановна", address="ул. Гагарина, д. 3", phone="+79123456781"),
        ]
        db.add_all(readers)
        db.commit()

        # Выдачи
        print("Creating borrowings...")
        borrowings = [
            BorrowingModel(reader_id=1, book_id=1, borrow_date=date.today() - timedelta(days=10)),
            BorrowingModel(reader_id=1, book_id=2, borrow_date=date.today() - timedelta(days=5)),
            BorrowingModel(reader_id=2, book_id=3, borrow_date=date.today() - timedelta(days=25)),  # Просрочена
            BorrowingModel(reader_id=3, book_id=4, borrow_date=date.today() - timedelta(days=15)),
        ]
        db.add_all(borrowings)
        db.commit()

        print("✅ Фикстуры успешно созданы!")

    except Exception as e:
        print(f"❌ Ошибка при создании фикстур: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    generate_fixtures()