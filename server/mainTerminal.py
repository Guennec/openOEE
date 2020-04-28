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
print('<div class="container>"')
print('<h2>Terminal list</h2>')
print('<table class="table table-hover">')
print('<thead><tr><th>Terminal id</th><th>IP</th><th>Terminal name</th></tr></thead>')
print('<tbody>')
for row in query:
    print('<tr>')
    print('<td>{}</td><td>{}</td><td>{}</td>'.format(row.terminalId, row.IP, row.name))
    print('</tr>')
print('</tbody></table></div>')
bottom_html = open("main_bottom.html","r")
all_line_bottom = bottom_html.read()
bottom_html.close()
print(all_line_bottom)
