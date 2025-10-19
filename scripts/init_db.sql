-- Создаем расширение для UUID если нужно
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Создаем таблицу издательств
CREATE TABLE IF NOT EXISTS publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    city VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем таблицу книг
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    cipher VARCHAR(255) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    first_author VARCHAR(255) NOT NULL,
    publication_year INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    copies_available INTEGER NOT NULL DEFAULT 0,
    publisher_id INTEGER NOT NULL REFERENCES publishers(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем таблицу читателей
CREATE TABLE IF NOT EXISTS readers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем таблицу выдач
CREATE TABLE IF NOT EXISTS borrowings (
    id SERIAL PRIMARY KEY,
    reader_id INTEGER NOT NULL REFERENCES readers(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL REFERENCES books(id) ON DELETE CASCADE,
    borrow_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создаем индексы для улучшения производительности
CREATE INDEX IF NOT EXISTS idx_books_cipher ON books(cipher);
CREATE INDEX IF NOT EXISTS idx_books_publisher_id ON books(publisher_id);
CREATE INDEX IF NOT EXISTS idx_borrowings_reader_id ON borrowings(reader_id);
CREATE INDEX IF NOT EXISTS idx_borrowings_book_id ON borrowings(book_id);
CREATE INDEX IF NOT EXISTS idx_borrowings_borrow_date ON borrowings(borrow_date);

-- Вставляем тестовые данные
INSERT INTO publishers (name, city) VALUES
    ('Эксмо', 'Москва'),
    ('Питер', 'Санкт-Петербург'),
    ('Дрофа', 'Москва')
ON CONFLICT (name) DO NOTHING;

INSERT INTO books (cipher, title, first_author, publication_year, price, copies_available, publisher_id) VALUES
    ('ISBN-001', 'Война и мир', 'Лев Толстой', 2010, 500.00, 3, 1),
    ('ISBN-002', 'Преступление и наказание', 'Федор Достоевский', 2015, 450.00, 2, 1),
    ('ISBN-003', 'Мастер и Маргарита', 'Михаил Булгаков', 2012, 400.00, 1, 2),
    ('ISBN-004', '1984', 'Джордж Оруэлл', 2018, 350.00, 4, 3)
ON CONFLICT (cipher) DO NOTHING;

INSERT INTO readers (full_name, address, phone) VALUES
    ('Иванов Иван Иванович', 'ул. Ленина, д. 1', '+79123456789'),
    ('Петров Петр Петрович', 'ул. Пушкина, д. 2', '+79123456780'),
    ('Сидорова Мария Ивановна', 'ул. Гагарина, д. 3', '+79123456781')
ON CONFLICT DO NOTHING;