from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)
    vacation_days = Column(Integer, default=30)  # Dias de férias padrão

# Criação da base de dados
def create_database():
    engine = create_engine('sqlite:///appferias.db')
    Base.metadata.create_all(engine)
    print("Base de dados e tabela 'users' criadas com sucesso!")  # Mensagem de sucesso

    return sessionmaker(bind=engine)()

if __name__ == "__main__":
    create_database()