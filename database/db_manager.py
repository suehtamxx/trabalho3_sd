from sqlalchemy import create_engine, column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import declarative_base

# criando a conexao com o banco 
engine = create_engine('sqlite://simulador.db', echo=True)

# base declarativa para mapear classes da tabela
Base = declarative_base()

# criando a tabela principal do bando de dados
class Leituras(Base):
    __tablename__ = 'leituras'
    id = column(Integer, primary_key=True)
    sensor_id = column(Integer)
    temperatura = column(Float)
    status_logico = column(String)
    timestamp = column(DateTime, default=func.now())

Base.metadata.create_all(engine)
