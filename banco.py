import sqlite3 as lite

con = lite.connect('dados.db')

with con:
  cur = con.cursor()
  cur.execute(
    "CREATE TABLE autopeca (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, tipo TEXT, codigo TEXT, estoque TEXT)"
  )

con = lite.connect('login.db')
