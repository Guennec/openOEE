import m_Machine
import m_Status
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class m_StatusList(Base):
    __tablename__ = 'm_StatusList'
    machineId = Column(String(16), ForeignKey('m_Machine.machineId'), primary_key=True)
    machine = relationship(m_Machine)
    statusId = Column(Integer, ForeignKey('m_Status.statusId'), primary_key=True)
    status = relationship(m_Status)