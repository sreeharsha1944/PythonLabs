#!/usr/bin/env python3

import cgi
import os
import datetime
from http.cookies import SimpleCookie, Morsel

cookie_ = SimpleCookie(os.environ["HTTP_COOKIE"])
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
morsel = Morsel()
morsel.key="visits"
morsel.value="0"
visits = int(cookie_.get("visits", morsel).value) + 1
cookie_["visits"] = str(visits)
date_format = "%a, %d-%b-%Y %H:%M:%S %Z"
cookie_["visits"]["expires"] = expiration.strftime(date_format)


print("Content-type: text/html")
print(cookie_.output(), "\n")
print("<html><head><title>Cookies</title></head>")
print("<body>")
print("<h1>Cookie Example</h1>")
print("<b>The Following header was sent:<br />",
       cookie_.output(), "</b><br/>")
print("<div><h3># of visits: ", visits, "</h3></div><hr />")
print("</body></html>")
