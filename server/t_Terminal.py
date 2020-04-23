from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class t_Terminal(Base):
    __tablename__ = 't_Terminal'
    terminalId = Column(Integer, primary_key=True)
    IP = Column(String(11))
    name = Column(String(32), nullable=False)