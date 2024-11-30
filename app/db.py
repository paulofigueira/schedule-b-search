from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost:5432/schedule_b_db"

# Configurando o SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Cria e retorna uma sessão com o banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()