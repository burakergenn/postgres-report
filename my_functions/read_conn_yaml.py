import yaml
import psycopg2


def postgres_connection_string(yaml_file):
    """
    fonksiyon ile PostgreSQL veritabanına YAML dosyasından bağlantı bilgilerini alabilir 
    """
    with open(yaml_file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    db_name = data['database']
    db_user = data['user']
    db_password = data['password']
    db_host = data['host']
    db_port = data['port']



def connect_db():
    """
    PostgreSQL veritabanına bağlanır ve connection nesnesini döndürür
    """
    conn = psycopg2.connect(
        host= postgres_connection_string.db_host ,
        database= postgres_connection_string.db_name ,
        user= postgres_connection_string.db_user ,
        port= postgres_connection_string.db_port ,
        password=postgres_connection_string.db_password
    )
    return conn

