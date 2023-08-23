import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSH_HOST'),
            user=config('PGSH_USER'),
            password=config('PGSH_PASSWORD'),
            database=config('PGSH_DATABASE')
        )
    except DatabaseError as ex:
        raise ex
