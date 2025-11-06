import pytest
from app.db import create_connection, create_table, insert_data, select_data


@pytest.fixture
def db_connection():
    conn = create_connection(
        db_name="testdb",
        db_user="testuser",
        db_password="testpassword",
        db_host="localhost",
        db_port="5432",
    )
    yield conn
    conn.close()


def test_connection(db_connection):
    assert db_connection is not None


def test_create_table(db_connection):
    create_table(db_connection)
    # Verifica se a tabela existe
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'test_table');"
    )
    assert cursor.fetchone()[0] is True


def test_insert_and_select(db_connection):
    create_table(db_connection)
    insert_data(db_connection, "Teste GitHub Actions")
    records = select_data(db_connection)
    assert len(records) > 0
    assert records[0][1] == "Teste GitHub Actions"
