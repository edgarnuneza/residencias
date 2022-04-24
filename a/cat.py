from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  

base = declarative_base()

class Empleado(base):  
    __tablename__ = 'empleado'

    nombre = Column(String, primary_key=True)
    apellidoPaterno = Column(String, nullable=False)
    apellidoMaterno = Column(String, nullable=False)
    matricula = Column(String)
    puesto = Column(String)