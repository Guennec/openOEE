import t_Terminal
import m_GroupMachine
import m_Machine
from base import Base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///openOEE.db')
Base.metadata.create_all(engine)

