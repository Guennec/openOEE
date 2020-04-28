import m_Machine_init
import m_StatusList_init
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class m_Counter(Base):
    __tablename__ = 'm_Counter'
    counterId = Column(Integer, primary_key=True)
    counterDescription = Column(String(250))
    cycleMonitoring = Column(Boolean, nullable=False)
    yieldMonitoring = Column(Boolean, nullable=False)
    scrapMonitoring = Column(Boolean, nullable=False)
    machineId = Column(String(16), ForeignKey('m_Machine.machineId'))
    machine = relationship(m_Machine_init)
    statusId = Column(Integer, ForeignKey('m_StatusList.statusId'))
    status = relationship(m_StatusList_init)