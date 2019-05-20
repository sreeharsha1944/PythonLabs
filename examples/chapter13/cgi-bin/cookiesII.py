#!/usr/bin/env python3
#!/usr/bin/env python3
import cgi
import os
import datetime
from http.cookies import SimpleCookie, Morsel
bgcolor_form = """
    <form>
    <div>Please choose your a background color</div>
    <div><input type='color' name='bgcolor' value='#EEEEEE' />
    <div><input type='submit' /> <input type='reset'/></div>
    </form>
"""
reset_all_cookies_form = """
    <form>
    <div>Click below to delete all cookies for this domain</div>
    <div><input type='submit' value="Delete All Cookies" /></div>
    </form>
"""
show_bgcolor_form = True

cookie_ = SimpleCookie(os.environ["HTTP_COOKIE"])
fields = cgi.FieldStorage()
if "bgcolor" in fields:
    bgcolor = fields['bgcolor']
    cookie_["bgcolor"] = bgcolor
    show_bgcolor_form = False
default = ""
expiration = datetime.datetime.now() + datetime.timedelta(days=30)

m1 = Morsel()
m1.key="visits"
m1.value="1"
visits = int(cookie_.get("visits", m1).value) + 1
m2 = Morsel()
m2.key="bgcolor"
m2.value="#DDDDDD"
bgcolor = cookie_.get("bgcolor", m2).value
cookie_["visits"] = str(visits)
cookie_["visits"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
cookie_["bgcolor"] = fields.getvalue('bgcolor', "inherit")


styles = "body {{ background:{} }}".format(bgcolor)

print("Content-type: text/html")
print(cookie_.output(), "\n")
print("<html><head><style>")
print(styles)
print("</style><title>Cookies</title></head>")
print("<body>")
print("<h1>Cookie Example</h1>")
print("<b>",os.environ["HTTP_COOKIE"], "</b><br/>")
print(cookie_.output(), "\n")
print(os.environ["HTTP_COOKIE"])
print("<div><h3># of visits: ", visits, "</h3></div><hr />")
if show_bgcolor_form:
    print(bgcolor_form)
else
    print(reset_all_cookies_form)
print("</body></html>")
