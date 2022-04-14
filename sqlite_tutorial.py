# Importando sqlite
import sqlite3

# Criando conexão com banco de dados (Existente ou não existente)
conexao = sqlite3.connect("clientes.db")

# Caso queiramos criar um banco de dados momentâneo em memória
# conexao = sqlite3.connect(":memory:")

# Criando cursor que nos permite interagir com o banco de dados
c = conexao.cursor()

# Criando uma tabela, lembrando que sqlite é case sensitive
# Tipos de dados do sqlite: NULL, INTEGER, REAL, TEXT, BLOB
#c.execute("""
#        CREATE TABLE clientes(
#        primeiro_nome TEXT,
#        ultimo_nome TEXT,
#        email TEXT
#        )
#""")

## Adicionando dados a nossa tabela
#c.execute("""
#    INSERT INTO clientes 
#    VALUES ("John","Textor", "glorioso_2022@botafogo.com.br")
#""")

# Ao invés de adicionarmos um registro por vez podemos usar listas de python para adicionar vários registros
#varios_clientes = [
#    ("nome_1", "sobrenome_1", "nome_1@sobrenome_1"),
#    ("nome_2", "sobrenome_2", "nome_2@sobrenome_2"),
#    ("nome_3", "sobrenome_3", "nome_3@sobrenome_3"),
#]
#c.executemany("""
#    INSERT INTO clientes 
#    VALUES (?,?,?)
#""", varios_clientes )

# Realizando query sobre tabela criada
#c.execute("SELECT * FROM clientes")
# Query que retorna apenas a primeira linha da tabela: c.fetchone()
# Query que retorna apenas as três primeiras linhas da tabela: c.fetchmany(3)
# Query que retorna todas as linhas da tabela
# O retorno da query é feita através de uma lista python
#print(c.fetchall())

# Por baixo dos panos o sqlite define uma chave primária chamada rowid
#c.execute("SELECT rowid, * FROM clientes")
#print(c.fetchall())

# Criando uma cláusula com WHERE
c.execute("SELECT rowid, * FROM clientes WHERE primeiro_nome='John' ")
print(c.fetchall())

# Commitando os comandos associados ao cursor através da nossa conexao
conexao.commit()
 
# Fechando a conexão
conexao.close()