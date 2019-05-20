#!/usr/bin/env python3
import cgi
import os
import datetime
from http.cookies import SimpleCookie, Morsel

fields = cgi.FieldStorage()
default = ""
expiration = datetime.datetime.now() + datetime.timedelta(days=30)

cookie_ = SimpleCookie(os.environ["HTTP_COOKIE"])
data = os.environ["HTTP_COOKIE"]
visits = 1
visits = int(cookie_.get("visits", "1").value) + 1
bgcolor = cookie_["bgcolor"].value
cookie_["visits"] = str(visits)
cookie_["visits"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
cookie_["bgcolor"] = bgcolor


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
print("<form>")
print("<div>Please choose your a background color</div>")
print("<div><input type='color' name='bgcolor' />")
print("<div><input type='submit' /> <input type='reset'/></div>")
print("</form>")
print("</body></html>")
