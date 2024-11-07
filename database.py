# Código para ver as tabelas

import sqlite3

# Conecte-se ao banco de dados
conn = sqlite3.connect('Dimitri.db') # Troque entre ORM.db e Dimitri.db para ver os diferentes bancos de dados
cursor = conn.cursor()

# Listar as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
print("Tabelas no banco de dados:", tabelas)

# Para cada tabela, liste as colunas
for tabela in tabelas:
    tabela_nome = tabela[0]
    print(f"\nEstrutura da tabela '{tabela_nome}':")
    cursor.execute(f"PRAGMA table_info({tabela_nome});")
    colunas = cursor.fetchall()
    for coluna in colunas:
        print(coluna)

# Fechar a conexão
conn.close()
