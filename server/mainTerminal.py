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
print('<div class="collapse navbar-collapse" id="navbarSupportedContent">')
print('<h3>Terminal list</h3>')
print('<ul class="nav navbar-nav ml-auto">')
print('<li class="nav-item active">')
print('<div class="btn-group" align="right">')
print('<button type="button" class="btn btn-success">Add terminal</button>')
print('</div>')
print('</li>')
print('</ul></div></div></nav>')
print('<div class="container">')
print('<h2>Filter</h2> ')
print('<input class="form-control" id="myFilter" type="text" placeholder="Search..">')
print('<br>')
print('<table class="table table-hover">')
print('<thead><tr><th>Terminal id</th><th>IP</th><th>Terminal name</th><th></th></tr></thead>')
print('<tbody id="tb_list">')
for row in query:
    print('<tr>')
    print('<td>{}</td><td>{}</td><td>{}</td>'.format(row.terminalId, row.IP, row.name))
    print('<td><div class="btn-group btn-group-sm">')
    print('<button type="button" class="btn btn-danger">Delete</button>')
    print('<button type="button" class="btn btn-warning">Modify</button>')
    print('</div></td>')
    print('</tr>')
print('</tbody></table></div>')
print('<script>')
print('$(document).ready(function(){')
print('$("#myFilter").on("keyup", function() {')
print('var value = $(this).val().toLowerCase();')
print('$("#tb_list tr").filter(function() {')
print('$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)')
print('});')
print('});')
print('});')
print('</script>')
bottom_html = open("main_bottom.html","r")
all_line_bottom = bottom_html.read()
bottom_html.close()
print(all_line_bottom)
