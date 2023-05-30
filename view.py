import sqlite3 as lite

con = lite.connect('dados.db')


def inserirProduto(i):
  with con:
    cur = con.cursor()
    query = "INSERT INTO autopeca (nome, tipo, codigo, estoque) VALUES (?, ?, ?, ?)"
    cur.execute(query, i)


def exibirProduto():
  lista = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM autopeca"
    cur.execute(query)
    produto = cur.fetchall()

    for i in produto:
      lista.append(i)
  return lista


def atualizarProduto(i):
  with con:
    cur = con.cursor()
    query = "UPDATE autopeca SET nome=?, tipo=?, codigo=?, estoque=? WHERE id=?"
    cur.execute(query, i)


def deletarProduto(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM autopeca WHERE id=?"
    cur.execute(query, i)
