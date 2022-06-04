def get_postgres_uri():
    host = 'localhost'
    port = 5432
    password = 'pass'
    user, db_name = 'user', 'db'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
