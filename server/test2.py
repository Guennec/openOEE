#!/Python37/python
from t_Terminal_init import t_Terminal
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

page_title = "Terminal list"
engine = create_engine('sqlite:///openOEE.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
query = session.query(t_Terminal).all()
head_html = open("main_head.html","r")
all_line_head = head_html.read()
all_line_head = all_line_head.replace('{pageTitle}',page_title)
head_html.close()
print(all_line_head)
print("List of terminals:<BR>")
for row in query:
    print("Terminal Id: {} | IP: {} | Name: {} <BR>".format(row.terminalId, row.IP, row.name))
print("</body></html>")
