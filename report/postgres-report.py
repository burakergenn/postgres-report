from ..my_functions.read_conn_yaml import postgres_connection_string
from ..my_functions.read_conn_yaml import connect_db
from ..my_functions.sql import report
import psycopg2

connection_string = postgres_connection_string('/etc/postgres-report/db_conn.yaml')

rapor = report()



