import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

data = ("Robson","rf852286@gmail.com")
#cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT,none VARCHAR(100),email VARCHAR(150))")
cursor.execute("INSERT INTO clientes(nome,email) VALUES (?,?);", data)
conexao.commit()