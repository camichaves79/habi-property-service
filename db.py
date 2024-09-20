import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_properties(filters):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM properties WHERE status IN ('pre_venta', 'en_venta', 'vendido')"
    # Añadir filtros a la consulta según sea necesario
    cursor.execute(query)
    properties = cursor.fetchall()
    cursor.close()
    conn.close()
    return properties

def like_property(property_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO likes (property_id, user_id) VALUES (%s, %s)"
    cursor.execute(query, (property_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "success"}
