import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')

 # criando tabela de categoria
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT )')


 # criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT,categoria TEXT, adicionando_em DATE, valor DECIMAl)')


 # criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT,categoria TEXT, retirado_em DATE, valor DECIMAl)')
