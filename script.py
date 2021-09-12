#!/usr/bin/python3

import cgi, cgitb, os

cgitb.enable()


print('Content-Type: text/plain')
print()

form = cgi.FieldStorage()


if "file" not in form:
    print("Put file argument in request")


elif os.path.isfile(form["file"].value):
    with open(form["file"].value) as file:
        for line in file:
            print(line)
else:
    print("This file doesn't exist!")
