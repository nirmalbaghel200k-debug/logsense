from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    format = Column(String)
    severity = Column(String)
    content = Column(Text)
