from sqlalchemy import Column, create_engine, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///simulador.db', echo=True)

Base = declarative_base()

class Leituras(Base):
    __tablename__ = 'leituras'
    id = Column(String, primary_key=True)
    sensor_id = Column(String)
    temperatura = Column(Float)
    status_logico = Column(String)
    timestamp = Column(String)

Base.metadata.create_all(engine)
