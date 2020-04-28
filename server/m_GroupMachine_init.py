from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class m_GroupMachine(Base):
    __tablename__ = 'm_GroupMachine'
    groupId = Column(String(16), primary_key=True)
    name = Column(String(32), nullable=False)