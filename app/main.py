from fastapi import FastAPI
from app.core.config import settings
from app.infrastructure.database import engine, Base
from app.api.routes.books import router as books_router
from app.api.routes.publishers import router as publishers_router
from app.api.routes.readers import router as readers_router
from app.api.routes.borrowings import router as borrowings_router
from app.api.routes.reports import router as reports_router

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Library Management System API",
)


app.include_router(books_router, prefix="/api/books", tags=["books"])
app.include_router(publishers_router, prefix="/api/publishers", tags=["publishers"])
app.include_router(readers_router, prefix="/api/readers", tags=["readers"])
app.include_router(borrowings_router, prefix="/api/borrowings", tags=["borrowings"])
app.include_router(reports_router, prefix="/api", tags=["reports"])


@app.get("/")
async def root():
    return {"message": "Library Management System API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
