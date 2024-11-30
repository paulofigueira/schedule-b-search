from .db import Base, engine
from .models import ScheduleB

def init_db():
    """Cria as tabelas no banco de dados."""
    Base.metadata.create_all(bind=engine)

# População inicial de dados será implementada aqui futuramente.
if __name__ == "__main__":
    init_db()