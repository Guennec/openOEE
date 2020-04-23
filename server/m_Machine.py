import t_Terminal
import m_GroupMachine
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class m_Machine(Base):
    __tablename__ = 'm_Machine'
    machineId = Column(String(16), primary_key=True)
    name = Column(String(32), nullable=False)
    description = Column(String(250))
    terminalId = Column(Integer, ForeignKey('t_Terminal.terminalId'))
    terminal = relationship(t_Terminal)
    groupId = Column(String(16), ForeignKey('m_GroupMachine.groupId'))
    groupMachine = relationship(m_GroupMachine)