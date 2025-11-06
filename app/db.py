import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Conexão com o PostgreSQL realizada com sucesso!")
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS test_table(id SERIAL PRIMARY KEY, name TEXT);"
    )
    connection.commit()
    print("Tabela criada com sucesso!")


def insert_data(connection, name):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO test_table(name) VALUES(%s) RETURNING id;", (name,)
    )
    id = cursor.fetchone()[0]
    connection.commit()
    print(f"Dados inseridos com ID: {id}")
    return id


def select_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test_table;")
    records = cursor.fetchall()
    print("Dados na tabela:")
    for row in records:
        print(row)
    return records
