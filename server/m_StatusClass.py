from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class m_StatusClass(Base):
    __tablename__ = 'm_StatusClass'
    statusClassId = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)