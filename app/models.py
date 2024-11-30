from sqlalchemy import Column, Integer, String
from .db import Base

class ScheduleB(Base):
    """Modelo para armazenar os códigos Schedule B."""
    __tablename__ = "schedule_b"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True, nullable=False)
    descricao = Column(String, nullable=False)
    capitulo = Column(Integer, nullable=False)
    palavras_chave = Column(String, nullable=True)