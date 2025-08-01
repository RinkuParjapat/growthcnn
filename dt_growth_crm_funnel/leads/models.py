from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    source = Column(String)
    stage = Column(String, default="New")
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Lead(name={self.name}, email={self.email}, stage={self.stage})>"
