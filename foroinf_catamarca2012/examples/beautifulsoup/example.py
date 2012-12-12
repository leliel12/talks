#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import bs4

html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>titulo</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>

<body>
    <p>este es un codigo feo<b>

    <a href="http://google.com">to google</a>
    <a href="http://www.google.com" id="unico">to google</a>
    <a href="http://yahoo.com">to yahoo</a>

    <ul class="elgroso">
        <li>something</li>
    </ul>

    <ul class="elgroso">
        <li>something</li>
    </ul>

    <ul class="elflaco">
        <li>something</li>
    </ul>

</body>

</html>
"""

soup = bs4.BeautifulSoup(html)

print soup.find_all("a")
print soup.find("a", href="http://yahoo.com")

print soup.find_all("a", href=re.compile(".*google[.]com"))
print soup.find("a", href=re.compile(".*google[.]com"), id="unico")

print soup.find("ul", class_="elgroso").find_all("li")
