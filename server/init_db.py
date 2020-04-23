import t_Terminal
import m_GroupMachine
import m_Machine
import m_StatusClass
import m_Status
import m_Counter
from base import Base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///openOEE.db')
Base.metadata.create_all(engine)

