import random

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker
from tenacity import retry, stop_after_delay

from notes import config
from notes.infrastructure.orm import metadata, start_mappers


@pytest.fixture(autouse=True)
def faker_seed():
    return random.randint(0, 9999)


@pytest.fixture
def mappers():
    start_mappers()

    yield

    clear_mappers()


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    connection = engine.connect()
    return connection


@pytest.fixture(scope='session')
def connection():
    engine = create_engine(
        config.get_postgres_uri(), isolation_level='SERIALIZABLE'
    )
    connection = wait_for_postgres_to_come_up(engine)
    metadata.create_all(connection)

    yield connection

    connection.close()


@pytest.fixture
def session(connection):
    transaction = connection.begin()
    session = sessionmaker()(bind=connection)

    yield session

    session.close()
    transaction.rollback()
