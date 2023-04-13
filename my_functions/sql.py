from . import connect_db
import psycopg2


conn = connect_db.conn

def report(conn):
    """
    Veritabani işlemlerini gerçekleştiren ana fonksiyon
    """
    # veri tabanına bağlantı gerçekleştirilir
    cur = conn.cursor()

    # En büyük 3 tabloyu getiren sorgu.
    cur.execute("""
            SELECT
            relname AS tablo_adi,
            pg_size_pretty(pg_table_size(relid)) AS boyut,
            pg_size_pretty(pg_indexes_size(relid)) AS index_boyutu,
            pg_size_pretty(pg_total_relation_size(relid)) AS toplam_boyut,
            rolname AS owner
        FROM pg_catalog.pg_statio_user_tables AS st
            JOIN pg_catalog.pg_class AS c ON st.relid = c.oid
            JOIN pg_catalog.pg_roles AS r ON r.oid = c.relowner
        WHERE
            schemaname = 'public'
        ORDER BY pg_total_relation_size(relid) DESC
        LIMIT 3;

        """)
                

    # sorgudan elde edilen sonuçlar alınır
    results = cur.fetchall()

    # veri işleme işlemleri gerçekleştirilir
    for result in results:
        print(result)

    # cursor ve bağlantı kapatılır
    cur.close()
    conn.close()