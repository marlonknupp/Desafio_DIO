import sqlite3

conexao = sqlite3.connect("Meu_banco.sqlite")
cursor = conexao.cursor()

def criar_tabela (cursor):
    cursor.execute('CREATE TABLE Clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100), email VARCHAR (150))')

    conexao.commit ()
 

def inserir_registro (conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit() 


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def inserir_lotes (conexao, cursor, dados):
    cursor.executemany(" INSERT INTO clientes (nome, email) VALUES (?,?)",dados)
    conexao.commit()

dados = [
    (" Milena", "milena@gmail.com"),
    ("rodrigo", "rodrigo@gmail.com"),
    ("maria", "maria@gmail.com"),
]
inserir_lotes(conexao, cursor, dados)