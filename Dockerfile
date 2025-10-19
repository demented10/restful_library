FROM python:3.12-slim


WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./


# Устанавливаем Poetry
RUN pip install poetry


# Настраиваем Poetry не создавать виртуальное окружение
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости (без dev-зависимостей)
RUN poetry install --without dev --no-interaction --no-ansi --no-root

# Копируем исходный код
COPY . .

# Создаем директорию для логов
RUN mkdir -p /app/logs

# Открываем порт
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]