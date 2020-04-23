import m_StatusClass
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class m_Status(Base):
    __tablename__ = 'm_Status'
    statusId = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    statusClassId = Column(String(16), ForeignKey('m_StatusClass.statusClassId'))
    statusClass = relationship(m_StatusClass)