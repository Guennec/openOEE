import t_Terminal_init
import m_GroupMachine_init
import m_Machine_init
import m_StatusClass_init
import m_Status_init
import m_Counter_init
from base import Base
from sqlalchemy import create_engine


engine = create_engine('sqlite:///openOEE.db')
Base.metadata.create_all(engine)

