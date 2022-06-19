def get_postgres_uri():
    host = 'localhost'
    port = 5432
    password = 'vk185a4'
    user, db_name = 'serhiikazmiruk', 'graph_notes'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
