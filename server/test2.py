#!/Python37/python


page_title = "OEE Studio"
head_html = open("main_head.html","r")
all_line_head = head_html.read()
all_line_head = all_line_head.replace('{pageTitle}',page_title)
head_html.close()
print(all_line_head)
print("Main Page")
bottom_html = open("main_bottom.html","r")
all_line_bottom = bottom_html.read()
bottom_html.close()
print(all_line_bottom)
