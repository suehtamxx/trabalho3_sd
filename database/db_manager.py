from sqlalchemy import Column, create_engine, String, Float
from sqlalchemy.orm import declarative_base

# criando a conexao com o banco 
engine = create_engine('sqlite:///simulador.db', echo=True)

# base declarativa para mapear classes da tabela
Base = declarative_base()

# criando a tabela principal do bando de dados
class Leituras(Base):
    __tablename__ = 'leituras'
    id = Column(String, primary_key=True)
    sensor_id = Column(String)
    temperatura = Column(Float)
    status_logico = Column(String)
    timestamp = Column(String)

Base.metadata.create_all(engine)
