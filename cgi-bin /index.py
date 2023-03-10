#!/bin/python3

print("Content-Type: text/html")    # Хидеры ответа
print()                             # Пустая строка сразу после хидеров
# А потом текст ответа
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")