#!/Python37/python


page_title = "OEE Studio"
head_html = open("main_head.html","r")
all_line_head = head_html.read()
all_line_head = all_line_head.replace('{pageTitle}',page_title)
head_html.close()
print(all_line_head)
print('<div class="collapse navbar-collapse" id="navbarSupportedContent">')
print('<ul class="nav navbar-nav ml-auto">')
print('<li class="nav-item active">')
print('<a class="nav-link" href="#">Page</a>')
print('</li>')
print('<li class="nav-item">')
print('<a class="nav-link" href="#">Page</a>')
print('</li>')
print('</ul></div></div></nav>')
print("Main Page")
bottom_html = open("main_bottom.html","r")
all_line_bottom = bottom_html.read()
bottom_html.close()
print(all_line_bottom)
